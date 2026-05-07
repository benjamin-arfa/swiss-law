"""SR 0.101.093 Art. 8

Generated from: ch/0/de/0.101.093.md
"""

import numpy as np

from openfisca_core.variables import Variable

class HasNotification(Variable):
    value_type = bool
    definition_period = "1 month"
    label = "Has received notification"
    
    def formula(person, period, variables):
        # Since the protocol provides notification for:a) Signatory states;b) Depositing of ratification documents;c) Entry into force dates;d) Other communication,
        # We'll capture these events through other boolean variables or events in openfisca and then return True if any of them are True.
        return np.any([person('has_signed_state', period), 
                       person('has_deposited_ratification', period), 
                       person('has_entry_into_force_date', period), 
                       person('has_other_communication', period)])
