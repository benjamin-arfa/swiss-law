"""SR 0.101.07 Art. 2

Generated from: ch/0/de/0.101.07.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

classification_of_crime = {'Straftaten geringfügiger Art': False,  # example minor crimes: will be added in the parameter_yaml section
                           'Taxes': False,
                           }

class convicted(Variable):
    value_type = bool
    label = "Convicted"
    definition_period = "P1Y"  # yearly
    references = "SR 0.101.07 Art. 2"

    def formula(person, period, parameters):
        convicted_status = person("convicted", period)
        minor_crime = parameters(period).minor_crime  # to be replaced with the parameter_yaml definition
        exceptions = person('first_instance_supreme_court', period) == 1 or (person('convicted_status_after Appeal', period) == 1) # additional conditions

        # replace the default with the new list of minor crimes as defined in parameter_yaml
        classification_of_crime.pop('Taxes', None)

        return (convicted_status == 1) & (~(minor_crime in classification_of_crime) | exceptions)
