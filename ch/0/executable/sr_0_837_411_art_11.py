"""SR 0.837.411 Art. 11 - Maximum benefit duration

Art. 11: Benefits may be limited to a period that must be:
- Normally not less than 156 working days per year
- In no case less than 78 working days per year

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class duree_max_indemnite_jours(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximum duration of unemployment benefit in working days per year (Art. 11)"
    default_value = 156


class duree_min_indemnite_jours_normal(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Normal minimum benefit duration: 156 working days/year (Art. 11)"
    default_value = 156


class duree_min_indemnite_jours_absolu(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Absolute minimum benefit duration: 78 working days/year (Art. 11)"
    default_value = 78


class jours_indemnite_utilises(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Working days of unemployment benefit already used this year"
    default_value = 0


class droit_indemnite_chomage_duree(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person still has remaining benefit days (Art. 11)"

    def formula(person, period, parameters):
        jours_utilises = person("jours_indemnite_utilises", period.this_year)
        jours_max = person("duree_max_indemnite_jours", period.this_year)
        return jours_utilises < jours_max
