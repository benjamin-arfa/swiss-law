"""SR 952.02 Art. 2 — Banken (Kategorisierung)

Generated from: ch/952/de/952.02.md

FINMA teilt Banken in Kategorien nach Anhang 3 ein anhand:
a) Bilanzsumme, b) verwaltete Vermoegen, c) privilegierte Einlagen,
d) Mindesteigenmittel.
Bank wird ab Kat. 5 in hoechste Kat. eingeteilt, in der sie mindestens
3 Schwellenwerte erreicht.
FINMA kann in begruendeten Einzelfaellen abweichen.
EFD prueft Schwellenwerte mind. alle 5 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bankv_bilanzsumme(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bilanzsumme der Bank (CHF)"
    reference = "SR 952.02 Art. 2 Abs. 2 lit. a"


class bankv_verwaltete_vermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verwaltete Vermoegen der Bank (CHF)"
    reference = "SR 952.02 Art. 2 Abs. 2 lit. b"


class bankv_privilegierte_einlagen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Privilegierte Einlagen der Bank (CHF)"
    reference = "SR 952.02 Art. 2 Abs. 2 lit. c"


class bankv_mindesteigenmittel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindesteigenmittel der Bank (CHF)"
    reference = "SR 952.02 Art. 2 Abs. 2 lit. d"


class bankv_schwellenwerte_erreicht(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl der erreichten Kategorie-Schwellenwerte (max. 4)"
    reference = "SR 952.02 Art. 2 Abs. 3"

    def formula_2019(person, period, parameters):
        import numpy as np

        p = parameters(period).sr952_02
        bilanzsumme = person('bankv_bilanzsumme', period)
        vermoegen = person('bankv_verwaltete_vermoegen', period)
        einlagen = person('bankv_privilegierte_einlagen', period)
        eigenmittel = person('bankv_mindesteigenmittel', period)

        count = (
            (bilanzsumme >= p.schwelle_bilanzsumme).astype(int)
            + (vermoegen >= p.schwelle_verwaltete_vermoegen).astype(int)
            + (einlagen >= p.schwelle_privilegierte_einlagen).astype(int)
            + (eigenmittel >= p.schwelle_mindesteigenmittel).astype(int)
        )
        return count


class bankv_kategorie_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bank erreicht naechsthoehere Kategorie (mind. 3 Schwellenwerte)"
    reference = "SR 952.02 Art. 2 Abs. 3"

    def formula_2019(person, period, parameters):
        schwellenwerte = person('bankv_schwellenwerte_erreicht', period)
        return schwellenwerte >= 3
