"""SR 0.103.2 Art. 14

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fair_trial(Variable):
    value_type = bool
    label = "Fair trial"
    entity = Person


class presumed_innocent(Variable):
    value_type = bool
    label = "Presumed innocent"
    entity = Person


class informed_of_charges(Variable):
    value_type = bool
    label = "Informed of charges"
    entity = Person


class reasonable_time(Variable):
    value_type = bool
    label = "Reasonable time to prepare defense"
    entity = Person


class speedy_trial(Variable):
    value_type = bool
    label = "Speedy trial"
    entity = Person


class present_at_trial(Variable):
    value_type = bool
    label = "Present at trial"
    entity = Person


class question_witnesses(Variable):
    value_type = bool
    label = "Question witnesses"
    entity = Person


class interpreter_available(Variable):
    value_type = bool
    label = "Interpreter available"
    entity = Person


class minor_protection(Variable):
    value_type = bool
    label = "Minor protection"
    entity = Person


class right_to_appeal(Variable):
    value_type = bool
    label = "Right to appeal"
    entity = Person


class right_to_compensation(Variable):
    value_type = bool
    label = "Right to compensation"
    entity = Person


class has_presumed_innocent(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check presumed innocence
        # TO DO: Set variable according to condition
        return 0  # Placeholder


class has_informed_of_charges(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check informed of charges
        # TO DO: Set variable according to condition
        return 0  # Placeholder


class has_reasonable_time(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check reasonable time
        # TO DO: Set variable according to condition
        return 0  # Placeholder


class has_speedy_trial(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check speedy trial
        # TO DO: Set variable according to condition
        return 0  # Placeholder


class has_present_at_trial(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check present at trial
        # TO DO: Set variable according to condition
        return 0  # Placeholder


class has_question_witnesses(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check question witnesses
        # TO DO: Set variable according to condition
        return 0  # Placeholder


class has_interpreter_available(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check interpreter available
        # TO DO: Set variable according to condition
        return 0  # Placeholder


class has_minor_protection(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check minor protection
        # TO DO: Set variable according to condition
        return 0  # Placeholder


class has_right_to_appeal(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check right to appeal
        # TO DO: Set variable according to condition
        return 0  # Placeholder


class has_right_to_compensation(Condition):
    value_type = bool
    def formula(person, period):
        other_cases = ['CriminalCase']
        # TO DO: Define function to check right to compensation
        # TO DO: Set variable according to condition
        return 0  # Placeholder
