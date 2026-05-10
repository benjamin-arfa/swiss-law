"""SR 0.101.094 Art. 13

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class participation_commissioner_in_chamber_hearings(Variable):
    value_type = bool
    label = French('Partipation du commissaire des droits de l\'homme dans les audiences de la chambre')
    definition_period = YEAR
    reference = 'SR 0.101.094 Art. 13'
    
    def formula_2010_01_01(engagements, period, variables):
        return ~engagements('case_before_chamber_or_gross_chamber', period)
    
    def formula(engagements, period, variables):
        return 1  # This formula is only for the beginning of 2010, and needs to be updated for the actual implementation
