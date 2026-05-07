"""SR 0.142.116.912 Art. 12

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

However due to the lack of information in [[ ## available_variables ## ]] as to how this information would be represented in the legal text;  
therefore it seems unnecessary to write a Variable in this case as we need variable declaration that explains how the legal article would correlate to the variable definition.
