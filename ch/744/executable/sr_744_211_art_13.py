"""SR 744.211 Art. 13

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class has_spare_vehicles_or_parts(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmung verfügt über notwendige Ersatzfahrzeuge oder Ersatzbestandteile für störungsfreien Betrieb"
    reference = "SR 744.211 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        return person('spare_vehicles_available', period) + person('spare_parts_available', period) > 0


class spare_vehicles_available(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ersatzfahrzeuge vorhanden"
    reference = "SR 744.211 Art. 13 Abs. 1"


class spare_parts_available(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ersatzbestandteile vorhanden"
    reference = "SR 744.211 Art. 13 Abs. 1"


class spare_vehicles_periodically_inspected_and_maintained(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ersatzfahrzeuge und Ersatzbestandteile werden periodisch gründlich untersucht und instand gestellt"
    reference = "SR 744.211 Art. 13 Abs. 2"


class electrical_insulation_continuously_monitored(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Elektrische Isolation wird laufend auf ihren Zustand geprüft"
    reference = "SR 744.211 Art. 13 Abs. 3"


class sr_744_211_art_13_compliant(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Einhaltung von Art. 13 SR 744.211: Ersatzfahrzeuge, Wartung und elektrische Isolation"
    reference = "SR 744.211 Art. 13"

    def formula(person, period, parameters):
        year = period.this_year

        has_spares = person('has_spare_vehicles_or_parts', year)
        inspected = person('spare_vehicles_periodically_inspected_and_maintained', year)
        insulation_ok = person('electrical_insulation_continuously_monitored', period)

        return has_spares * inspected * insulation_ok
