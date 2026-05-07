"""SR 0.103.2 Art. 47

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

This article is more of an environmental policy, so it's irrelevant for creating an OpenFisca Variable.
However, as a possible interpretation, this variable does not map to any parameters or formulas, as it falls under environmental law.
