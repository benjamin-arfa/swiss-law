"""SR 0.142.111.762 Art. 4

Generated from: ch/0/de/0.142.111.762.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class article_4_refusal_rate(Variable):
    value_type = float
    label = "Refusal rate for entry under Article 4"

    def formula(person, period, parameters):
        # This is a very simplified and hypothetical formula, not a direct calculation from the article
        return 0.05 # 5% refusal rate, subject to change in parameters
