"""SR 744.211 Art. 3

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_trolleybus_company(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the entity is a trolleybus company subject to federal supervision"
    reference = "SR 744.211 Art. 3"

    def formula(person, period, parameters):
        return person('operates_trolleybus_service', period)


class operates_trolleybus_service(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the entity operates a trolleybus service"
    reference = "SR 744.211 Art. 3"

    def formula(person, period, parameters):
        return person('operates_trolleybus_service', period)


class subject_to_bav_supervision(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the entity is subject to supervision by the Federal Office of Transport (BAV/OFT)"
    reference = "SR 744.211 Art. 3"

    def formula(person, period, parameters):
        return is_trolleybus_company(person, period)


class bav_jurisdiction_trolleybus_act(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether BAV jurisdiction applies under the Federal Trolleybus Act (SR 744.21) of 29 March 1950"
    reference = "SR 744.211 Art. 3"

    def formula(person, period, parameters):
        return person('subject_to_bav_supervision', period)


class bav_jurisdiction_railway_legislation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether BAV jurisdiction applies under railway and electrical installations legislation"
    reference = "SR 744.211 Art. 3"

    def formula(person, period, parameters):
        return person('subject_to_bav_supervision', period)
