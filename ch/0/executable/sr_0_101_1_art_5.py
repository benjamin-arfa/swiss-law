"""SR 0.101.1 Art. 5

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

from openfisca_country_especifique import countries

class ImmunitatsaufhebungBenefit(Variable):
    value_type = float
    entity = Person
    calculation = Aggregatetransformer()

    def formula_2022P(assets,.period, parameters):
        # We calculate the benefit amount
        # The first requirement is that the immunity is lifted according to article 5.1
        lifted_immunity_article_5_1 = ...  # We assume that the parameter is in available_variables
        # The second requirement is that the certificate has been submitted
        certificate_submitted = ...  # We assume that the parameter is in available_variables
        # The third case involves evaluating the situations where immunity has to be lifted

        # The formula calculates the benefit based on the calculated values
        benefit_amount = lifted_immunity_article_5_1 + certificate_submitted
        return benefit_amount

class LIFTED_IMMUNITY_ARTICLE_5_1(Variable):
    value_type = int
    entity = Person
    calculation = FormulaCol('immunitatsaufhebung_benefit', 'article_5_1')
    definition_period = YEAR

class CERTIFICATE_SUBMITTED(Variable):
    value_type = int
    entity = Person
    calculation = FormulaCol('immunitatsaufhebung_benefit', 'certificate_submit')
    definition_period = YEAR
