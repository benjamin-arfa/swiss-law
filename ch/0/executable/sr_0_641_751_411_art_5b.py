"""SR 0.641.751.411 Art. 5b - Scope of CO2 vehicle emission rules

Art. 5b: For the application of Swiss CO2 vehicle emission rules:
- Import to Liechtenstein = import to Switzerland
- Registration in Liechtenstein = registration in Switzerland

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class importation_vehicule_li_comme_ch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle import to LI treated as import to CH for CO2 rules (Art. 5b)"
    default_value = True


class immatriculation_li_comme_ch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle registration in LI treated as registration in CH for CO2 rules (Art. 5b)"
    default_value = True
