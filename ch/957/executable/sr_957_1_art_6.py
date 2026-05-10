"""SR 957.1 Art. 6-8

Generated from: ch/957/de/957.1.md

Entstehung, Umwandlung und Untergang von Bucheffekten:
- Entstehung durch: Hinterlegung von Wertpapieren zur Sammelverwahrung,
  Hinterlegung von Globalurkunden, Eintragung von Wertrechten,
  Übertragung von Registerwertrechten
- Umwandlung zwischen Formen möglich (Emittent trägt Kosten)
- Auslieferung von Wertpapieren auf Verlangen möglich
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class entstehungsart_bucheffekte(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Entstehungsart: sammelverwahrung, globalurkunde, wertrechte, registerwertrechte"
    reference = "SR 957.1 Art. 6 Abs. 1"


class bucheffekte_gueltig_entstanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Bucheffekte gültig entstanden ist (Hinterlegung/Eintragung + Gutschrift)"
    reference = "SR 957.1 Art. 6 Abs. 1"


class umwandlung_durch_emittent(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Emittent eine Umwandlung der Form vornimmt"
    reference = "SR 957.1 Art. 7 Abs. 1"


class gesamtzahl_unveraendert_nach_umwandlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gesamtzahl der ausgegebenen Rechte durch Umwandlung unverändert bleibt"
    reference = "SR 957.1 Art. 7 Abs. 3"


class hat_anspruch_auf_wertpapier_auslieferung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kontoinhaberin Anspruch auf Auslieferung von Wertpapieren hat"
    reference = "SR 957.1 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_effektenkonto_gutgeschrieben', period)
