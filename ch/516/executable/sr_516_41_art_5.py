"""SR 516.41 Art. 5 - Communications a l'auditeur en chef

Generated from: ch/516/fr/516.41.md

Communications to the Chief Auditor: session dates, verdicts,
appeals, annual reports, and investigation notifications.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class president_dirigeant_seance(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La personne est le president dirigeant la seance du tribunal militaire"
    reference = "SR 516.41 Art. 5 al. 1"


class obligation_communiquer_date_et_prononce(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le president doit communiquer la date de seance et le prononce a l'auditeur en chef"
    reference = "SR 516.41 Art. 5 al. 1"

    def formula(self, period, parameters):
        return self('president_dirigeant_seance', period)


class est_juge_instruction(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La personne est juge d'instruction militaire"
    reference = "SR 516.41 Art. 5 al. 4"


class obligation_informer_ouverture_cloture_enquete(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le juge d'instruction informe l'auditeur en chef de l'ouverture et de la cloture d'une enquete"
    reference = "SR 516.41 Art. 5 al. 4"

    def formula(self, period, parameters):
        return self('est_juge_instruction', period)
