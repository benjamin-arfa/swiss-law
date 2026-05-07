"""SR 455.110.2 Art. 16

Generated from: ch/455/de/455.110.2.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class betaeubungsverfahren_mechanisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mechanisches Betaeubungsverfahren wird verwendet"
    reference = "SR 455.110.2 Art. 16 lit. a"


class betaeubungsverfahren_elektrisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Elektrisches Betaeubungsverfahren wird verwendet"
    reference = "SR 455.110.2 Art. 16 lit. b"


class empfindungslosigkeit_sofort_eingetreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wahrnehmungs- und Empfindungslosigkeit ist sofort eingetreten"
    reference = "SR 455.110.2 Art. 16 lit. a"


class empfindungslosigkeit_innerhalb_1_sekunde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wahrnehmungs- und Empfindungslosigkeit innerhalb 1 Sekunde eingetreten"
    reference = "SR 455.110.2 Art. 16 lit. b"


class betaeubungserfolg_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Betaeubungserfolg ist konform nach Art. 16 SR 455.110.2"
    reference = "SR 455.110.2 Art. 16"

    def formula(person, period, parameters):
        mechanisch = person('betaeubungsverfahren_mechanisch', period)
        elektrisch = person('betaeubungsverfahren_elektrisch', period)
        sofort = person('empfindungslosigkeit_sofort_eingetreten', period)
        in_1s = person('empfindungslosigkeit_innerhalb_1_sekunde', period)
        return (mechanisch * sofort) + (elektrisch * in_1s)
