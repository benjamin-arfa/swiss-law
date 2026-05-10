"""SR 0.103.3 Art. 25

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class child_abduction_prevention_measures(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Measures implemented to prevent child abduction (Art. 25 SR 0.103.3)"

    def formula(person, period, parameters):
        implementation_status = parameters(period).justice.child_abduction_prevention_measures.implemented
        return implementation_status

class child_reunification_assistance(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Assistance provided for child reunification (Art. 25 SR 0.103.3)"

    def formula(person, period, parameters):
        assistance_status = parameters(period).justice.child_abduction_recovery.child_reunification_assistance
        return assistance_status

class child_welfare_priority(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Priority given to child welfare in proceedings (Art. 25 SR 0.103.3)"

    def formula(person, period, parameters):
        welfare_priority_status = parameters(period).justice.child_abduction_prevention_measures.child_welfare_priority
        return welfare_priority_status

class adoption_review_procedure(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Adoption review procedures implemented (Art. 25 SR 0.103.3)"

    def formula(person, period, parameters):
        procedure_status = parameters(period).justice.child_abduction_prevention_measures.adoption_review_procedure
        return procedure_status
