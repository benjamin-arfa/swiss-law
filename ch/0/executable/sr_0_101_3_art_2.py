"""SR 0.101.3 Art. 2

Generated from: ch/0/de/0.101.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_country_datasets import switzerland


class Article2Immunity(switzerland.core_models.person_employment.Earnings):
    label = "Immunität nach Art. 2"
    entity_class = switzerland.core_models.entities.Person

    def formula(action, period, parameters):
        made_statement_to_court = (action == "statement_to_court")
        disclosed_sensitive_info = (action == "disclosed_sensitive_info")
        return ~(disclosed_sensitive_info) if (made_statement_to_court) else False
