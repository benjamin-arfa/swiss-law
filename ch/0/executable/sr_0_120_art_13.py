"""SR 0.120 Art. 13

Generated from: ch/0/de/0.120.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class global_cooperation_goals(Variable):
    value_type = str
    label = "Global cooperation goals (Art. 13 SR 0.120)"

    def formula(variables, period, parameters):
        return "Politische Zusammenarbeit und Förderung des Völkerrechts (Art. 13.1 SR 0.120)" + "," + \
               "Internationale Zusammenarbeit in Wirtschaft, Sozialwesen, Kultur, Erziehung und Gesundheit (Art. 13.1 SR 0.120)"
