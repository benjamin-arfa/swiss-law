"""SR 921.552.1 Art. 10

Generated from: ch/921/de/921.552.1.md

Trennung von Vermehrungsgut: Bei Ernte, Aufbereitung, Lagerung, Befoerderung
und Anzucht nach Art/Kategorie/Erntebestand etc. in Partien getrennt halten.

Abs. 2: Saatgutmischungen nur innerhalb gleicher Kategorie, gleichem
Herkunftsgebiet und bestimmtem Hoehenband:
  - unter 1200 m ue. M.: Hoehenband 400 m
  - ab 1200 m ue. M.: Hoehenband 200 m
Komponenten muessen zu gleichen Teilen enthalten sein.

Abs. 3: Mischung verschiedener Kategorien -> Kennzeichnung als quellengesichert.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class saatgutmischung_hoehe_ueber_meer(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoehe ueber Meer des Erntestandorts (m)"
    reference = "SR 921.552.1 Art. 10 Abs. 2"


class saatgutmischung_zulaessiges_hoehenband(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zulaessiges Hoehenband fuer Saatgutmischungen (m)"
    reference = "SR 921.552.1 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        hoehe = person('saatgutmischung_hoehe_ueber_meer', period)
        return where(hoehe < 1200, 400, 200)
