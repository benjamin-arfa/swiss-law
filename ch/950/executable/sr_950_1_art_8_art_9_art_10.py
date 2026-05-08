"""SR 950.1 Art. 8–10

Generated from: ch/950/de/950.1.md

Informationspflichten und Pruefpflicht:
- Art. 8: Finanzdienstleister informieren ueber: Name, Adresse,
  Taetigkeit, Aufsichtsstatus, Kundensegment, Risiken,
  Kosten, wirtschaftliche Bindungen, Marktangebote.
  Basisinformationsblatt bei zusammengesetzten Instrumenten.
- Art. 9: Information vor Vertragsschluss oder Dienstleistung.
  Prospekt und Basisinformationsblatt kostenlos.
- Art. 10: Pruefpflicht fuer Angemessenheit bei Portfolioverwaltung
  und Anlageberatung; Eignungspruefung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class fidleg_information_erteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Finanzdienstleister hat Informationspflichten erfuellt (Art. 8)"
    reference = "SR 950.1 Art. 8"


class fidleg_basisinformationsblatt_bereitgestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Basisinformationsblatt wurde bereitgestellt"
    reference = "SR 950.1 Art. 8 Abs. 3"


class fidleg_information_vor_vertragsschluss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Information wurde vor Vertragsschluss erteilt (Art. 9)"
    reference = "SR 950.1 Art. 9 Abs. 1"


class fidleg_eignungspruefung_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Eignungs- oder Angemessenheitspruefung durchgefuehrt (Art. 10-12)"
    reference = "SR 950.1 Art. 10–12"


class fidleg_ist_portfolioverwaltung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Dienstleistung ist Portfolioverwaltung oder Anlageberatung"
    reference = "SR 950.1 Art. 10"


class fidleg_pruefpflicht_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Pruefpflicht bei Portfolioverwaltung/Beratung erfuellt"
    reference = "SR 950.1 Art. 10"

    def formula_2020(person, period, parameters):
        import numpy as np

        ist_portfolio = person('fidleg_ist_portfolioverwaltung', period)
        eignungspruefung = person('fidleg_eignungspruefung_durchgefuehrt', period)

        # Pruefpflicht nur bei Portfolio/Beratung
        return np.where(ist_portfolio, eignungspruefung, True)
