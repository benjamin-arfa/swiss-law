"""SR 642.11 Art. 37a

Generated from: ch/642/fr/642.11.md

Art. 37a Procédure simplifiée (Simplified procedure for small wages):
1. For small employment income, tax is levied at a flat rate of 0.5%
   without considering other income, professional expenses, or social
   deductions, provided the employer pays via the simplified procedure
   under the Black Labour Act (LTN Art. 2-3).
2. Art. 88(1)(a) applies by analogy.
3. The employer must periodically remit tax to the competent AVS office.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ifd_procedure_simplifiee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the simplified tax procedure applies (employer uses LTN Art. 2-3)"
    reference = "SR 642.11 Art. 37a Abs. 1"


class ifd_salaire_procedure_simplifiee(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Salary subject to the simplified procedure (CHF)"
    reference = "SR 642.11 Art. 37a Abs. 1"


class ifd_impot_procedure_simplifiee(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Federal income tax under the simplified procedure (CHF)"
    reference = "SR 642.11 Art. 37a Abs. 1"

    def formula(person, period, parameters):
        applicable = person('ifd_procedure_simplifiee', period)
        salaire = person('ifd_salaire_procedure_simplifiee', period)
        taux = parameters(period).sr_642_11.simplified_procedure_rate
        return applicable * salaire * taux
