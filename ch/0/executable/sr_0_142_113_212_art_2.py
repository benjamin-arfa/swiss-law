"""SR 0.142.113.212 Art. 2

Generated from: ch/0/de/0.142.113.212.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class swiss_migration_rule(Variable):
  value_type = bool
  entity = Person
  definition_period = MONTH
  label = "Migration rule (SR 0.142.113.212 Art. 2)"

  def formula(person, period, parameters):
    # conditions:
    has_diplomatic_passport = person("has_diplomatic_passport", period)
    does_not_work_in_switzerland = person("does_not_work_in_switzerland", period)
    is_staying_for_permitted_time = person("is_staying_for_permitted_time", period)
    
    if (not parameters(period).is_schengen_state):
      return has_diplomatic_passport 
    return has_diplomatic_passport & does_not_work_in_switzerland & is_staying_for_permitted_time
