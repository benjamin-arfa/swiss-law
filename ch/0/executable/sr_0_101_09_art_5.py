"""SR 0.101.09 Art. 5

Generated from: ch/0/de/0.101.09.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from recopy import pdf_to_string
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse




# Parameters
class protocol_effect_date(ParameterQuantity):
    description = "Day when the protocol comes into effect"
    definition_period = ETD("year")
    
class judge_term_length(ParameterQuantity):
    description = "Length of a judge's term"
    definition_period = ETD("year")
    
class case_completion_date(ParameterQuantity):
    description = "Date when a court case is completed"
    definition_period = ETD("year")

# Variables
class has_judge_term_expired(Variable):
    value_type = bool
    label = "Has a judge's term expired?"
    unit = ""
    definition_period = ETD("year")
  
    def formula(person, period, parameters):
        protocol_effect_date_val = parameters(protocol_effect_date).period(period.start.offset(-judge_term_length)),
        judge_term_length_val = judge_term_length
        return (protocol_effect_date_val - judge_term_length_val).magnitude <= 0

class has_commission_member_term_expired(Variable):
    value_type = bool
    label = "Has a commission member's term expired?"
    unit = ""
    definition_period = ETD("year")
  
    def formula(person, period, parameters):
        protocol_effect_date_val = parameters(protocol_effect_date).period(period.start.offset(-judge_term_length)),
        judge_term_length_val = judge_term_length
        return (protocol_effect_date_val - judge_term_length_val).magnitude <= 0

class has_court_judgment(Variable):
    value_type = bool
    label = "Has a court made a judgment?"
    unit = ""
    definition_period = ETD("year")
  
    def formula(person, period, parameters):
        protocol_effect_date_val = parameters(protocol_effect_date).period(period.start.offset(-case_completion_date)),
        case_completion_date_val = case_completion_date
        return (protocol_effect_date_val - case_completion_date_val).magnitude <= 0

class number_of_complaints(Variable):
    value_type = int
    label = "Number of complaints"
    unit = ""
    definition_period = ETD("year")
  
    def formula(person, period, parameters):
        return ...

class has_commission_decision(Variable):
    value_type = bool
    label = "Has a commission made a decision?"
    unit = ""
    definition_period = ETD("year")
  
    def formula(person, period, parameters):
        return ...

class has_minister_committee_decision(Variable):
    value_type = bool
    label = "Has a minister committee made a decision?"
    unit = ""
    definition_period = ETD("year")
  
    def formula(person, period, parameters):
        return ...

class has_chamber_decision(Variable):
    value_type = bool
    label = "Has a chamber made a decision?"
    unit = ""
    definition_period = ETD("year")
  
    def formula(person, period, parameters):
        return ...

class date_of_protocol_effect(Variable):
    value_type = date
    label = "Date of the protocol's effect"
    unit = ""
    definition_period = ETD("year")
  
    def formula(person, period, parameters):
        return parameters(protocol_effect_date).period(period.start).start.date()
