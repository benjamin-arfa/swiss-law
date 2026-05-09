"""SR 837.174 Art. 3 – Grundlage zur Bestimmung des koordinierten Lohnes

Generated from: ch/837/de/837.174.md

Die Grenzbeträge nach BVG Art. 2, 7 und 8 werden durch 260.4 geteilt
(Tagesgrenzbeträge). Bei Teilinvalidität werden Grenzbeträge entsprechend
dem prozentualen Anteil des Teilrentenanspruchs gekürzt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Divisor for converting BVG annual thresholds to daily thresholds
BVG_TAGE_DIVISOR = 260.4


class bvg_eintrittsschwelle_jahresbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "BVG-Eintrittsschwelle Jahresbetrag (Art. 2 BVG, CHF)"
    reference = "SR 837.174 Art. 3 Abs. 1"


class bvg_koordinationsabzug_jahresbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "BVG-Koordinationsabzug Jahresbetrag (Art. 8 BVG, CHF)"
    reference = "SR 837.174 Art. 3 Abs. 1"


class bvg_oberer_grenzbetrag_jahresbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "BVG oberer Grenzbetrag Jahresbetrag (Art. 8 BVG, CHF)"
    reference = "SR 837.174 Art. 3 Abs. 1"


class iv_teilrentenanspruch_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Prozentualer Anteil des IV-Teilrentenanspruchs"
    reference = "SR 837.174 Art. 3 Abs. 1"
    default_value = 0.0


class tages_eintrittsschwelle(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Tageseintrittsschwelle BVG für arbeitslose Personen (CHF)"
    reference = "SR 837.174 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        jahresbetrag = person('bvg_eintrittsschwelle_jahresbetrag', period.this_year)
        iv_anteil = person('iv_teilrentenanspruch_prozent', period)

        tagesbetrag = jahresbetrag / BVG_TAGE_DIVISOR

        # Bei Teilinvalidität: Kürzung entsprechend dem Rentenanteil
        import numpy as np
        return np.where(
            iv_anteil > 0,
            tagesbetrag * (1 - iv_anteil / 100),
            tagesbetrag
        )


class tages_koordinationsabzug(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Tageskoordinationsabzug BVG für arbeitslose Personen (CHF)"
    reference = "SR 837.174 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        jahresbetrag = person('bvg_koordinationsabzug_jahresbetrag', period.this_year)
        iv_anteil = person('iv_teilrentenanspruch_prozent', period)

        tagesbetrag = jahresbetrag / BVG_TAGE_DIVISOR

        import numpy as np
        return np.where(
            iv_anteil > 0,
            tagesbetrag * (1 - iv_anteil / 100),
            tagesbetrag
        )
