"""SR 0.105 Art. 9

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mutual_legal_cooperation(boolean_var):
    value_type = bool
    definition_period = YEAR
    label = "Participation in mutual legal cooperation (SR 0.105 Art. 9)"

    def formula(person, period, parameters):
        involved_crimes = [crime for crime in parameters(period).miscellaneous.offenses if person("acquainted_with", period, parameters).formula(person, period, parameters).evaluator.apply(crime)]
        evidence = person("evidence_available", period, parameters).formula(person, period, parameters).evaluator.apply()
        return (len(involved_crimes) > 0 and evidence) | any(treaty in parameters(period).treaties for treaty in parameters(period).treaties)

# Assuming the existence of some external variables:
from external import crimes, treaties

class acquaintance(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Was an individual aware of the fact, which can lead to an acquaitance"

    def formula(household, period, parameters):
        crimes = [params(crime) for params in parameters(period).miscellaneous.offenses if params(crime)]
        evidence = [params(evidence) for params in parameters(period).miscellaneous.evidence if params(evidence)]
        return household.associated_members.sum(acquainted_with(crime) for crime in crimes) > 0 and household.associated_members.sum(having_ev(evidence) for evidence in evidence) > 0

class evidence_available(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Do we have access to certain documents?"

    def formula(household, period, parameters):
        return (all(treaty.get('treaty') for treaty in parameters(period).treaties)) and any(params(accessibility) for params in parameters(period).miscellaneous.document_accessibility if params(accessibility))
