"""SR 366.1 Art. 14

Generated from: ch/366/de/366.1.md

Loeschung der Daten im polizeilichen Informationssystem von Interpol.
Aufbewahrung laengstens bis Ablauf der Verfolgungs- und Vollstreckungsverjaehrung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class interpol_daten_nicht_mehr_benoetigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten im polizeilichen Informationssystem von Interpol werden nicht mehr benoetigt"
    reference = "SR 366.1 Art. 14 Abs. 1"


class verfolgungs_vollstreckungsverjaehrung_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verfolgungs- und Vollstreckungsverjaehrung ist abgelaufen"
    reference = "SR 366.1 Art. 14 Abs. 2"


class interpol_daten_zu_loeschen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten im Interpol-System sind zu loeschen"
    reference = "SR 366.1 Art. 14"

    def formula(person, period, parameters):
        nicht_benoetigt = person('interpol_daten_nicht_mehr_benoetigt', period)
        verjaehrt = person('verfolgungs_vollstreckungsverjaehrung_abgelaufen', period)
        return nicht_benoetigt + verjaehrt
