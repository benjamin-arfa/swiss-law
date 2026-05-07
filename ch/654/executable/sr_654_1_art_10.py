"""SR 654.1 Art. 10 - Obligation de s'annoncer

Generated from: ch/654/fr/654.1.md

Obligation to register with the FTA within 90 days of the end
of the reportable fiscal period.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class delai_annonce_jours(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Delai pour s'annoncer aupres de l'AFC (en jours apres fin de la periode fiscale)"
    reference = "SR 654.1 Art. 10 al. 4"
    default_value = 90


class annonce_afc_effectuee(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite declarante s'est annoncee spontanement aupres de l'AFC"
    reference = "SR 654.1 Art. 10 al. 1"


class obligation_annonce_afc(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite declarante est tenue de s'annoncer aupres de l'AFC"
    reference = "SR 654.1 Art. 10 al. 1"

    def formula(self, period, parameters):
        return self('entite_declarante', period)
