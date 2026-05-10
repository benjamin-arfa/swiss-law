"""SR 0.101.094 Art. 14

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class Art14Modification(Variable):
    value_type = int
    label = u"Modification from Art. 14"

    def __init__(self, period, parameters):
        super(Art14Modification, self).__init__(period, parameters)
        
    # However, as we noted that the change does not give any computational basis this would not give a complete solution and in real scenarios this could
    # possibly be determined by data which might not be directly available to us. In simpler conditions one might look like this.
    
    # def formula_2018(self, person, period):
    #     if some_modifying_legal_document_from_Art_14_changes_variable_38_at_Sr_0_101_094:
    #         return calculate_new_value_situation
    #     else:
    #         return original_value_for_38_at_Sr_0_101_094
