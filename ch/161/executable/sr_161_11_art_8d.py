"""SR 161.11 Art. 8d

Generated from: ch/161/fr/161.11.md

Finalizing candidate lists: cantonal services send lists to Federal Chancellery
by day after deposit deadline. Chancellery communicates deletions within 72 hours.
Canton transmits final copy within 24 hours after list finalization deadline.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class odp_delai_envoi_listes_chancellerie_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour envoyer les listes a la Chancellerie (1 jour apres date limite depot)"
    reference = "SR 161.11 Art. 8d al. 1"

    def formula(person, period, parameters):
        return 1


class odp_delai_communication_biffages_heures(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour communiquer les biffages par la Chancellerie (72 heures)"
    reference = "SR 161.11 Art. 8d al. 3"

    def formula(person, period, parameters):
        return 72


class odp_delai_transmission_copie_definitive_heures(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour transmettre la copie definitive a la Chancellerie (24 heures)"
    reference = "SR 161.11 Art. 8d al. 4"

    def formula(person, period, parameters):
        return 24
