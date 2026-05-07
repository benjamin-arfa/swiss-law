"""SR 0.101.06 Art. 5

Generated from: ch/0/de/0.101.06.md
"""

import pandas as pd
from openfisca_core import variables
from openfisca_core.periods import EDF
from openfisca_core.parameters import Parameter
from openfisca_core.datasets import Dataset
from openfisca_core import periods

class ProtocolAreas(variables.FunctionVariable):
    value_type = 'string'

class ExtensionAreas(variables.FunctionVariable):
    value_type = 'string'

class WithdrawnAreas(variables.FunctionVariable):
    value_type = 'string'

def protocol_areas(data_input):
    return data_input["protocol_starting_areas"]

def extension_areas(data_input):
    if data_input["new_area_submitted"]:
        return extension_areas.data_input["new_area_submitted"]
    else:
        return ""

def withdrawn_areas(data_input):
    if data_input["new_area_withdrawn"]:
        return withdrawn_areas.data_input["new_area_withdrawn"]

protocol_areas_formula = protocol_areas
extension_areas_formula = extension_areas
withdrawn_areas_formula = withdrawn_areas
