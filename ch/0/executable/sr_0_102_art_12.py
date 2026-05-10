"""SR 0.102 Art. 12

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class article_commitment_status(Variable):
    value_type = set
    entity = Person
    definition_period = MONTH
    label = "Status of commitment to the European Charter of Local Self-Government (SR 0.102 Art. 12)"

    def formula(person, period, parameters):
        articles = {"Article 2", "Article 3", "Article 4", "Article 5", "Article 7", "Article 8", "Article 9", "Article 10"}
        initial_selection = {f"Article {article}" for article in [2, 3, 4, 5, 7, 8, 9, 10, 11]}
        selected_articles = set()
        last_notification_month = person("last_commitment_notification", period)
        if last_notification_month <= 0:
            selected_articles = initial_selection
        else:
            additional_articles = set([5, 2, 7, 8, 9, 10, 11])  # articles to be later selected
            selected_articles = initial_selection.union(additional_articles)

        return selected_articles
