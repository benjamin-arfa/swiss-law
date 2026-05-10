"""SR 711 Art. 6

Generated from: ch/fr/711.md

Expropriation temporaire (Temporary expropriation):
- Limited to max 10 years unless law/decree/agreement provides otherwise
- Period runs from taking possession, ends 3 months after completion at latest
- If temporary expropriation destroys essential value, owner can demand permanent expropriation
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

DUREE_MAX_EXPROPRIATION_TEMPORAIRE_ANS = 10
DELAI_APRES_ACHEVEMENT_MOIS = 3


class duree_expropriation_temporaire_ans(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Duree de l'expropriation temporaire (annees)"
    reference = "SR 711 Art. 6 al. 1"


class expropriation_temporaire_valide(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'expropriation temporaire respecte la duree maximale de 10 ans"
    reference = "SR 711 Art. 6 al. 1"

    def formula(person, period):
        duree = person('duree_expropriation_temporaire_ans', period)
        return duree <= DUREE_MAX_EXPROPRIATION_TEMPORAIRE_ANS


class valeur_essentielle_perdue(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'expropriation temporaire fait perdre sa valeur essentielle au droit"
    reference = "SR 711 Art. 6 al. 2"


class peut_exiger_expropriation_permanente(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'exproprie peut exiger l'expropriation permanente"
    reference = "SR 711 Art. 6 al. 2"

    def formula(person, period):
        return person('valeur_essentielle_perdue', period)
