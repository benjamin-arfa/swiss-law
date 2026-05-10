"""SR 711 Art. 13

Generated from: ch/fr/711.md

Extension de l'expropriation a la demande de l'expropriant:
When partial expropriation indemnity for depreciation of remaining part exceeds
1/3 of that part's value, the expropriator can request total expropriation.
Renunciation deadline: 20 days from final indemnity determination.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

SEUIL_DEPRECIATION_FRACTION = 1 / 3
DELAI_RENONCIATION_JOURS = 20


class valeur_venale_partie_restante_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Valeur venale de la partie restante de l'immeuble (CHF)"
    reference = "SR 711 Art. 13 al. 1"


class indemnite_depreciation_partie_restante_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Indemnite pour depreciation de la partie restante (CHF)"
    reference = "SR 711 Art. 13 al. 1"


class expropriant_peut_demander_expropriation_totale(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'expropriant peut demander l'expropriation totale"
    reference = "SR 711 Art. 13 al. 1"

    def formula(person, period):
        valeur = person('valeur_venale_partie_restante_chf', period)
        indemnite = person('indemnite_depreciation_partie_restante_chf', period)
        # L'indemnite depasse le tiers de la valeur de la partie restante
        import numpy as np
        return np.where(valeur > 0, indemnite > valeur * SEUIL_DEPRECIATION_FRACTION, False)
