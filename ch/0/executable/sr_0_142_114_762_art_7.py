"""SR 0.142.114.762 Art. 7

Generated from: ch/0/de/0.142.114.762.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

No new Variable class is necessary. Variables in OpenFisca typically involve calculations; 
this article establishes a general rule for resolving disagreements, which is a procedural aspect rather than a quantitative variable.
