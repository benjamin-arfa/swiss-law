"""SR 744.21 Art. 11b

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class operational_safety_responsible(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Unternehmen ist für die Sicherheit des Betriebs verantwortlich (SR 744.21 Art. 11b)"
    reference = "SR 744.21 Art. 11b"

    def formula(person, period, parameters):
        return True


class installations_maintained_for_safety(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Anlagen werden so instand gehalten, dass die Sicherheit jederzeit gewährleistet ist (SR 744.21 Art. 11b)"
    reference = "SR 744.21 Art. 11b"

    def formula(person, period, parameters):
        return True


class vehicles_maintained_for_safety(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Fahrzeuge werden so instand gehalten, dass die Sicherheit jederzeit gewährleistet ist (SR 744.21 Art. 11b)"
    reference = "SR 744.21 Art. 11b"

    def formula(person, period, parameters):
        return True


class safety_guaranteed_at_all_times(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Sicherheit ist jederzeit gewährleistet (SR 744.21 Art. 11b)"
    reference = "SR 744.21 Art. 11b"

    def formula(person, period, parameters):
        installations_safe = person('installations_maintained_for_safety', period)
        vehicles_safe = person('vehicles_maintained_for_safety', period)
        return installations_safe * vehicles_safe
