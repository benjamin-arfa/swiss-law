"""SR 516.41 Art. 4 - Auditeur en chef

Generated from: ch/516/fr/516.41.md

Chief Auditor: exercises same functions towards military justice
members as the Chief of the Army does towards military personnel.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class est_auditeur_en_chef(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La personne est l'auditeur en chef"
    reference = "SR 516.41 Art. 4"


class competence_organisation_justice_militaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'auditeur en chef definit l'organisation et le nombre de membres de la justice militaire"
    reference = "SR 516.41 Art. 4 al. 2"

    def formula(self, period, parameters):
        return self('est_auditeur_en_chef', period)


class competence_attribution_membres(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'auditeur en chef attribue les membres aux regions, tribunaux ou fonctions"
    reference = "SR 516.41 Art. 4 al. 3"

    def formula(self, period, parameters):
        return self('est_auditeur_en_chef', period)


class competence_nomination_promotion(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'auditeur en chef procede aux nominations et promotions des officiers de justice"
    reference = "SR 516.41 Art. 4 al. 4"

    def formula(self, period, parameters):
        return self('est_auditeur_en_chef', period)
