"""SR 0.142.117.121 Art. 16

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

To model this data protection regulation in OpenFisca requires defining several new entities and variables to capture information about personal data processing. Below are a few possible variables that could capture these requirements. Note that more variables might be necessary depending on the specific requirements defined by Art. 16.
