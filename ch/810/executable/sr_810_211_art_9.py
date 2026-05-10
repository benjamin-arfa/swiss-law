"""SR 810.211 Art. 9

Generated from: ch/810/de/810.211.md

Art. 9: Information der Lebendspenderin oder des Lebendspenders.

Abs. 1: Aerztinnen/Aerzte muessen die Person vor der Entnahme
muendlich und schriftlich umfassend und verstaendlich informieren.

Abs. 2: Informationspflichten umfassen namentlich:
  a. Zweck und Ablauf der Vorabklaerungen und des Eingriffs
  b. Freiwilligkeit und Unentgeltlichkeit; Strafbarkeit bei Entgelt
  c. Kurz- und Langzeitrisiken fuer die Gesundheit
  d. Dauer Spitalaufenthalt und Arbeitsunfaehigkeit
  e. Regelmässige Gesundheitspruefung als Spender/in
  f. Nachverfolgung des Gesundheitszustands
  g. Versicherungsschutz (Art. 11) und Aufwandersatz (Art. 12)
  h. Grundzuege der Datenbearbeitung
  i. Recht auf Ablehnung oder Widerruf ohne Begruendung
  j. Moegliche psychische Folgen und psychologische Betreuung
  k. Erwartete Vorteile/Nachteile und Therapieoptionen fuer Empfaenger

Abs. 3: Angemessene Bedenkzeit muss eingeraeumt werden.

Abs. 4: Ablauf ist zu dokumentieren; Aufbewahrung 10 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class muendliche_information_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Muendliche Information der Lebendspenderin/des Lebendspenders ist erfolgt"
    reference = "SR 810.211 Art. 9 Abs. 1"


class schriftliche_information_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Schriftliche Information der Lebendspenderin/des Lebendspenders ist erfolgt"
    reference = "SR 810.211 Art. 9 Abs. 1"


class bedenkzeit_eingeraeumt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Angemessene Bedenkzeit fuer den Entscheid wurde eingeraeumt"
    reference = "SR 810.211 Art. 9 Abs. 3"


class dokumentation_information_aufbewahrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Dokumentation der Information wird aufbewahrt (Pflicht: 10 Jahre)"
    reference = "SR 810.211 Art. 9 Abs. 4"


class aufbewahrungsfrist_dokumentation_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsfrist fuer die Dokumentation in Jahren"
    reference = "SR 810.211 Art. 9 Abs. 4"

    def formula(person, period, parameters):
        return parameters(period).sr_810_211.art_9.aufbewahrungsfrist_jahre


class informationspflicht_lebendspende_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Alle Informationspflichten gegenueber Lebendspender/in sind erfuellt (Art. 9)"
    reference = "SR 810.211 Art. 9"

    def formula(person, period, parameters):
        muendlich = person('muendliche_information_erfolgt', period)
        schriftlich = person('schriftliche_information_erfolgt', period)
        bedenkzeit = person('bedenkzeit_eingeraeumt', period)
        return muendlich * schriftlich * bedenkzeit
