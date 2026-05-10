"""SR 0.101.06 Art. 9

Generated from: ch/0/de/0.101.06.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class notify_article_9(Variable):
    value_type = bool
    entity = Person
    label = u'Notice: Article 9 invoked'
    definition_period = ETD

    def formula_country(definition, country, parameters):
        # For the sake of this placeholder example, assume any of the conditions specified in the article invoke this variable
        return 1
