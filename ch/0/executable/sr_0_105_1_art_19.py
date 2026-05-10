"""SR 0.105.1 Art. 19

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class NationalMechanismPreventsFolter(Variable):
    value_type = bool
    entity = Person # We'll return True for persons under certain conditions, not for the institution
    definition_period = MONTH
    label = "Mechanism prevents torture according to the national mechanism (Art. 19 SR 0.105.1)"

    def formula(institution, period, parameters):

        return institution("has_national_mechanism", period)

class HasNationalMechanism(Variable):
    value_type = bool
    entity = Facility
    definition_period = MONTH
    label = "Entity has a national mechanisms (Art. 19 SR 0.105.1)"

    def formula(facility, period, parameters):

        return facility("has_torture_prevention_mechanism", period)

class HasTorturePreventionMechanism(Variable):
    value_type = bool
    entity = Institution
    definition_period = MONTH
    label = "Entity has measures according to national mechanics (part of Art. 19 SR 0.105.1)"

    def formula(institution, period, parameters):
        return (institution("mechanism_proposes_recommendations", period)  
               & institution("mechanism_submits_recommendations", period) 
               & institution("mechanism_vouches_for_existing_legislation_proposals", period))
