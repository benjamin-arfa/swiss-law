"""SR 0.101.094 Art. 12

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class inadmissible(Variable):
    value_type = bool
    entity = Person
    label = u"Inadmissible"
    definition_period = MONTH

    def formula(person, period):
        # Compatible with convention
        compatible_with_convention = person('compatible_with_convention', period)
        
        # Clearly unfounded or made in abusive manner
        clearly_unfounded_or_abusive = person('clearly_unfounded') + person('made_in_abusive_manner')
        
        # Significant disadvantage or requires examination
        significant_disadvantage = person('significant_disadvantage_applied') ^ \
            (person('requires_examination_of_merits') * (1 - person('declining_to_examine_domestic_case')))
        
        # Return True if either condition is met
        return (compatible_with_convention | clearly_unfounded_or_abusive |
                significant_disadvantage)
