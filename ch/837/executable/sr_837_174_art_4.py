"""SR 837.174 Art. 4 – Koordinierter Tageslohn

Generated from: ch/837/de/837.174.md

Der koordinierte Tageslohn ist die positive Differenz aus dem
Arbeitslosentaggeld abzüglich des Tages-Koordinationsabzugs.
Mindestens der Betrag nach Art. 8 Abs. 2 BVG (auf den Tag umgerechnet).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

BVG_TAGE_DIVISOR = 260.4


class arbeitslosentaggeld(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Arbeitslosentaggeld (CHF)"
    reference = "SR 837.174 Art. 4 Abs. 2"


class bvg_mindestlohn_jahresbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "BVG Mindest-koordinierter Lohn Jahresbetrag (Art. 8 Abs. 2 BVG, CHF)"
    reference = "SR 837.174 Art. 4 Abs. 3"


class koordinierter_tageslohn_berechnet(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Berechneter koordinierter Tageslohn (CHF)"
    reference = "SR 837.174 Art. 4"

    def formula(person, period, parameters):
        import numpy as np

        taggeld = person('arbeitslosentaggeld', period)
        koord_abzug = person('tages_koordinationsabzug', period)
        mindestlohn_jahr = person('bvg_mindestlohn_jahresbetrag', period.this_year)

        # Abs. 2: Positive Differenz aus Taggeld minus Koordinationsabzug
        koord_tageslohn = np.maximum(taggeld - koord_abzug, 0)

        # Abs. 3: Mindestens der auf den Tag umgerechnete Betrag nach Art. 8 Abs. 2 BVG
        mindestlohn_tag = mindestlohn_jahr / BVG_TAGE_DIVISOR

        return np.where(
            koord_tageslohn > 0,
            np.maximum(koord_tageslohn, mindestlohn_tag),
            0  # If no positive difference, person is not insured
        )
