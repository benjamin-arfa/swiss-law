"""SR 0.142.117.432 Art. 8

Generated from: ch/0/de/0.142.117.432.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

OpenFisca does not handle international diplomacy or law. It's used for social welfare and tax policies. Therefore, no OpenFisca variable can be defined to represent this regulation.
