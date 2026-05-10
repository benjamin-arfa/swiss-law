"""SR 0.103.3 Art. 39

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_treaty_entry_person(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Has the country joined the AHV treaty (Art. 39 SR 0.103.3)"

    def formula(person, period, parameters):
        country = personountry()
        ahv_treaty_entry = country("ahv_treaty_entry", period)
        ahv_insurance_obligation = person("resides_in_switzerland", period)

        return ahv_insurance_obligation & ahv_treaty_entry


class ahv_insurance_obligation_treaty_entry(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "AHV insurance obligation and the country has joined the AHV treaty (Art. 3 AHVG and Art. 39 SR 0.103.3)"

    def formula(person, period, parameters):
        ahv_insurance_obligation = person("ahv_insurance_obligation", period)
        ahv_treaty_entry_person = person("ahv_treaty_entry_person", period)
        return ahv_insurance_obligation & ahv_treaty_entry_person
