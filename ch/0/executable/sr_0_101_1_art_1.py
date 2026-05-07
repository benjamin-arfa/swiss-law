"""SR 0.101.1 Art. 1

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY

class is_subject_to_convention(Variable):
    value_type = bool
    label = "Is the person subject to the Convention?"
    definition period = ETERNITY
    definition formula = """
    # Agents and their supporting advisors and lawyers of the contracting parties
    agent_of_contracting_party = person('agent_of_contracting_party', period)
    agent_advisor_lawyer = person('agent_advisor_lawyer', period)
    # Persons participating in procedures initiated before the Commission under Article 25
    person_participating_in_procedure = person('person_participating_in_procedure', period)
    # Lawyers or professors of law participating in proceedings to assist one of the persons mentioned above
    lawyer_professor = person('lawyer_professor', period)
    # Persons designated by the Commission to support its representatives in proceedings before the Court
    commission_support_person = person('commission_support_person', period)
    # Witnesses, experts, and other persons participating in proceedings at the request of the Commission or the Court
    witness_expert_other = person('witness_expert_other', period)
    
    is_subject_to_convention = (
        (agent_of_contracting_party != 0) | (agent_advisor_lawyer != 0) |
        (person_participating_in_procedure != 0) | (lawyer_professor != 0) |
        (commission_support_person != 0) | (witness_expert_other != 0)
    )
    return is_subject_to_convention
"""
Note that the variable name `is_subject_to_convention` should be replaced with the actual variable name used in the OpenFisca model.

To define the rates and thresholds used in the variable, we need to create a YAML parameter snippet.
