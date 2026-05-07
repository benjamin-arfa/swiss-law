"""SR 518.52 Art. 2

Generated from: ch/518/fr/518.52.md

Competence of the Federal Council to recognise the International
Fact-Finding Commission (Art. 90 para. 2 Protocol I).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class autre_partie_accepte_meme_obligation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'autre Haute Partie contractante accepte la meme obligation"
    reference = "SR 518.52 Art. 2"


class competence_commission_etablissement_faits(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La competence de la Commission internationale d'etablissement des faits est reconnue de plein droit"
    reference = "SR 518.52 Art. 2"

    def formula(self, period, parameters):
        autre_partie = self('autre_partie_accepte_meme_obligation', period)
        return autre_partie
