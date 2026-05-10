"""SR 672.201 Art. 4 — Aufwandbesteuerung

Art. 4: Natürliche Personen können nur für Steuern Anrechnung verlangen,
für die sie nicht nach dem Aufwand besteuert werden (Art. 14 DBG, Art. 6 StHG).
Ausnahme: Wer auf allen Einkünften aus einem Vertragsstaat volle Steuern
zum Satz des Gesamteinkommens entrichtet.

Generated from: ch/672/de/672.201.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_nach_aufwand_besteuert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person wird nach dem Aufwand besteuert (Art. 14 DBG / Art. 6 StHG)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_4"
    default_value = False


class entrichtet_volle_steuer_auf_vertragsstaat_einkuenfte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person entrichtet volle Steuern auf allen Einkünften aus einem Vertragsstaat (Art. 14 Abs. 5 DBG)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_4"
    default_value = False


class anrechnung_ausgeschlossen_aufwandbesteuerung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anrechnung ausgeschlossen wegen Aufwandbesteuerung (SR 672.201 Art. 4)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_4"

    def formula(person, period, parameters):
        # Art. 4 Abs. 1: Keine Anrechnung für Steuern, bei denen nach Aufwand besteuert wird.
        # Art. 4 Abs. 2: Ausnahme wenn volle Steuern auf Vertragsstaat-Einkünften entrichtet werden.
        nach_aufwand = person('ist_nach_aufwand_besteuert', period)
        volle_steuer = person('entrichtet_volle_steuer_auf_vertragsstaat_einkuenfte', period)
        return nach_aufwand * (1 - volle_steuer)
