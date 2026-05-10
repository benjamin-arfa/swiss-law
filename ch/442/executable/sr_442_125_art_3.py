"""SR 442.125 Art. 3

Generated from: ch/442/de/442.125.md

Foerdervoraussetzungen spartenspezifische Finanzhilfen: Min 3 Sprachregionen,
min 2500 Aktive, min 3 Jahre taetig, Geschaeftsstelle erforderlich.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_sprachregionen_mitglieder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Sprachregionen mit Mitgliedern"
    reference = "SR 442.125 Art. 3 Abs. 1 Bst. a"


class anzahl_aktive_vertreten(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl vertretener Aktiver"
    reference = "SR 442.125 Art. 3 Abs. 1 Bst. f"


class jahre_kontinuierlich_taetig(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre kontinuierlicher Taetigkeit der Organisation"
    reference = "SR 442.125 Art. 3 Abs. 1 Bst. d"


class hat_geschaeftsstelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation eine erreichbare Geschaeftsstelle hat"
    reference = "SR 442.125 Art. 3 Abs. 3"


class erfuellt_foerdervoraussetzungen_spartenspezifisch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation die Foerdervoraussetzungen fuer spartenspezifische Finanzhilfen erfuellt"
    reference = "SR 442.125 Art. 3"

    def formula(person, period, parameters):
        sprachregionen = person('anzahl_sprachregionen_mitglieder', period)
        aktive = person('anzahl_aktive_vertreten', period)
        jahre = person('jahre_kontinuierlich_taetig', period)
        geschaeftsstelle = person('hat_geschaeftsstelle', period)
        return (sprachregionen >= 3) * (aktive >= 2500) * (jahre >= 3) * geschaeftsstelle
