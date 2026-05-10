"""SR 412.10 Art. 60

Generated from: ch/412/de/412.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Note: This article is modeled at the organizational level but expressed
# per-entity for OpenFisca compatibility.


class anteil_betriebe_am_fonds(Variable):
    """Anteil der Betriebe die sich am Bildungsfonds beteiligen (0-1)"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der Betriebe am Bildungsfonds (Dezimalzahl)"
    reference = "SR 412.10 Art. 60 Abs. 4 Bst. a"


class anteil_arbeitnehmende_am_fonds(Variable):
    """Anteil der Arbeitnehmenden und Lernenden deren Betriebe sich beteiligen (0-1)"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der Arbeitnehmenden/Lernenden am Bildungsfonds (Dezimalzahl)"
    reference = "SR 412.10 Art. 60 Abs. 4 Bst. a"


class hat_eigene_bildungsinstitution(Variable):
    """Ob die Organisation ueber eine eigene Bildungsinstitution verfuegt"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation verfuegt ueber eigene Bildungsinstitution"
    reference = "SR 412.10 Art. 60 Abs. 4 Bst. b"
    default_value = False


class voraussetzungen_allgemeinverbindlichkeit(Variable):
    """Ob die Voraussetzungen fuer Allgemeinverbindlicherklaerung erfuellt sind"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen fuer Allgemeinverbindlicherklaerung des Bildungsfonds erfuellt"
    reference = "SR 412.10 Art. 60 Abs. 4"

    def formula(person, period, parameters):
        anteil_betriebe = person('anteil_betriebe_am_fonds', period)
        anteil_arbeitnehmende = person('anteil_arbeitnehmende_am_fonds', period)
        hat_institution = person('hat_eigene_bildungsinstitution', period)
        # Mindestens 30% der Betriebe mit mind. 30% der Arbeitnehmenden
        min_betriebe = anteil_betriebe >= 0.30
        min_arbeitnehmende = anteil_arbeitnehmende >= 0.30
        return min_betriebe * min_arbeitnehmende * hat_institution
