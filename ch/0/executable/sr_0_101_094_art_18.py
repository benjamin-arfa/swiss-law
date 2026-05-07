"""SR 0.101.094 Art. 18

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core import variables
from openfisca_core.periods import ANY
from openfisca_core Hood_Import import formula_

class Ratification_process_variable(variables.IntTaxBenefit, period_=ANY):
    @classmethod
    def new.definition(cls):
        return {
        'label': cls _('Ratification process'),
        'definition_period': ANY,
        'value_type': 'int',
        'default_value': 1,
        'definition': [
            variables.InitTerminal(),
            ('==', (formula_(" personne a signé le protocole"), 1), 'signedUnconditionally', 1),
            ('==', (formula_(" personne a signé le protocole"), 0), 'signedConditionally', 1),
       ],
    }

    def meaning(period, transition, parameters_):

        # If the person has NOT signed the protocol at the reference period, 
        # the value of 'Ratification process' remains undefined.
        if not transition.value("personne a signé le protocole"):

            # Define the initial Ratification process status.
            if period == transition.first_period():
                return {'Ratification process': None}
            # If no value has been assigned at a period before,
            # the value is undefined and remains so.
            else:
                return {'Ratification process': None}
        elif transition.value("personne a signé le protocole") == 1:

            # When a person signs the protocol at the reference period 
            # (Unconditionally signed), and no value has been assigned at a period before, 
            # the value of 'Ratification process' is set to 'signedUnconditionally'.
            if period == transition.first_period():
                return {'Ratification process': 'signedUnconditionally'}
        elif transition.value("personne a signé le protocole") == 0:

            # When a person signs the protocol at the reference period 
            # (Conditionally signed), and no value has been assigned at a period before, 
            # the value of 'Ratification process' is set to 'signedConditionally'.
            if period == transition.first_period():
                return {'Ratification process': 'signedConditionally'}
