"""SR 744.211 Art. 4

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_trolleybus_unternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person betreibt ein Trolleybusunternehmen"
    reference = "SR 744.211 Art. 4"

    def formula(person, period, parameters):
        return person('ist_trolleybus_unternehmen', period)


class hat_feste_anlagen_trolleybus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybusunternehmen erstellt oder unterhält feste Anlagen"
    reference = "SR 744.211 Art. 4"

    def formula(person, period, parameters):
        ist_trolleybus = person('ist_trolleybus_unternehmen', period)
        return ist_trolleybus


class eisenbahngesetzgebung_sinngemäss_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eisenbahngesetzgebung gilt sinngemäss für feste Anlagen des Trolleybusunternehmens"
    reference = "SR 744.211 Art. 4"

    def formula(person, period, parameters):
        return person('hat_feste_anlagen_trolleybus', period)


class elektrische_anlagen_gesetzgebung_sinngemäss_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesetzgebung über elektrische Anlagen gilt sinngemäss für feste Anlagen des Trolleybusunternehmens"
    reference = "SR 744.211 Art. 4"

    def formula(person, period, parameters):
        return person('hat_feste_anlagen_trolleybus', period)


class eisenbahnverordnung_742_141_1_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eisenbahnverordnung vom 23. November 1983 (SR 742.141.1) gilt sinngemäss für feste Anlagen des Trolleybusunternehmens"
    reference = "SR 744.211 Art. 4"

    def formula(person, period, parameters):
        return person('hat_feste_anlagen_trolleybus', period)
