"""SR 0.142.117.121 Art. 2

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *

class SwissCitizen(EnumSubSet):
    value_type = Enum
    possible_values = ["yes", "no"]
    default_value = "yes"

class SriLankanCitizen(EnumSubSet):
    value_type = Enum
    possible_values = ["yes", "no"]
    default_value = "no"

class ThirdCountryNational(EnumSubSet):
    value_type = Enum
    possible_values = ["yes", "no"]
    default_value = "no"

class StatelessPerson(EnumSubSet):
    value_type = Enum
    possible_values = ["yes", "no"]
    default_value = "no"

class HasPermittedResidence(Variable):
    value_type = bool
    default_value = True
