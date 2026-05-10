"""SR 313.32 Art. 13

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class photokopie_gebuehr_pro_seite(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer Photokopien pro Seite (0.50 CHF)"
    reference = "SR 313.32 Art. 13 Abs. 1"
    default_value = 0.50


class anzahl_photokopie_seiten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Seiten Photokopien"
    reference = "SR 313.32 Art. 13"


class photokopie_gebuehr_total(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Totale Gebuehr fuer Photokopien"
    reference = "SR 313.32 Art. 13"

    def formula(person, period, parameters):
        seiten = person('anzahl_photokopie_seiten', period)
        return seiten * 0.50
