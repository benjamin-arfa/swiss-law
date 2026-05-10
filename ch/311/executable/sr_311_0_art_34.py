"""SR 311.0 Art. 34

Generated from: ch/fr/311/311.0.md

Art. 34: Peine pecuniaire (Geldstrafe) - Fixation
- Abs. 1: Min 3 jours-amende, max 180 jours-amende.
- Abs. 2: Jour-amende: min 30 CHF, max 3000 CHF (exception: min 10 CHF).
  Amount based on personal and economic situation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stgb_anzahl_tagessaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Tagessaetze (Geldstrafe), zwischen 3 und 180"
    reference = "SR 311.0 Art. 34 Abs. 1"


class stgb_tagessatz_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag eines Tagessatzes in CHF (30 bis 3000, Ausnahme min 10)"
    reference = "SR 311.0 Art. 34 Abs. 2"


class stgb_geldstrafe_gesamt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamtbetrag der Geldstrafe (Anzahl Tagessaetze * Betrag)"
    reference = "SR 311.0 Art. 34"

    def formula(person, period, parameters):
        anzahl = person('stgb_anzahl_tagessaetze', period)
        betrag = person('stgb_tagessatz_betrag', period)
        # Enforce limits: 3-180 days, 30-3000 CHF per day (10 CHF exception handled externally)
        anzahl_begrenzt = max_(min_(anzahl, 180), 3)
        betrag_begrenzt = max_(min_(betrag, 3000), 10)
        return anzahl_begrenzt * betrag_begrenzt


class stgb_tagessatz_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Tagessatz-Betrag im gesetzlichen Rahmen liegt"
    reference = "SR 311.0 Art. 34 Abs. 2"

    def formula(person, period, parameters):
        betrag = person('stgb_tagessatz_betrag', period)
        return (betrag >= 10) * (betrag <= 3000)
