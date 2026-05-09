"""SR 654.1 Art. 20 - Obligation de garder le secret

Generated from: ch/654/de/654.1.md

Persons entrusted with enforcement must maintain confidentiality,
with defined exceptions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class personne_chargee_execution(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La personne est chargee de l'execution de l'accord applicable et de la loi"
    reference = "SR 654.1 Art. 20 al. 1"


class exception_secret_transmission_legale(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exception au secret: transmission d'informations prevue par l'accord ou la loi"
    reference = "SR 654.1 Art. 20 al. 2 let. a"


class exception_secret_organes_judiciaires(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exception au secret: renseignements officiels aupres d'organes judiciaires ou administratifs"
    reference = "SR 654.1 Art. 20 al. 2 let. b"


class exception_secret_accord_applicable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exception au secret: levee autorisee par l'accord applicable avec base legale suisse"
    reference = "SR 654.1 Art. 20 al. 2 let. c"


class obligation_secret_applicable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'obligation de garder le secret s'applique a la personne"
    reference = "SR 654.1 Art. 20 al. 1"

    def formula(self, period, parameters):
        chargee = self('personne_chargee_execution', period)
        exception_a = self('exception_secret_transmission_legale', period)
        exception_b = self('exception_secret_organes_judiciaires', period)
        exception_c = self('exception_secret_accord_applicable', period)
        aucune_exception = not_(exception_a + exception_b + exception_c)
        return chargee * aucune_exception
