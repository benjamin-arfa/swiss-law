"""SR 661.1 Art. 2

Generated from: ch/661/de/661.1.md

Art. 2 Ersatzbefreiung wegen Gesundheitsschädigung durch Militär- oder Zivildienst:
1. A health impairment from military/civil service exists if the person lost
   fitness due to a condition wholly or partly caused/worsened by service.
2. Persons dispensed from service due to health impairment are exempt from
   the levy only for the duration of the dispensation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wpev_gesundheitsschaedigung_durch_dienst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the person has a health impairment caused/worsened by military or civil service"
    reference = "SR 661.1 Art. 2 Abs. 1"


class wpev_dispensation_aktiv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the person is currently dispensed from service"
    reference = "SR 661.1 Art. 2 Abs. 2"


class wpev_ersatzbefreiung_gesundheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the person is exempt from levy due to service-related health impairment"
    reference = "SR 661.1 Art. 2"

    def formula(person, period, parameters):
        schaedigung = person('wpev_gesundheitsschaedigung_durch_dienst', period)
        dispensation = person('wpev_dispensation_aktiv', period)
        return schaedigung * dispensation
