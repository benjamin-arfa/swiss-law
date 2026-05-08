"""SR 950.1 Art. 15–16

Generated from: ch/950/de/950.1.md

Dokumentation und Rechenschaft:
- Art. 15: Finanzdienstleister dokumentieren: vereinbarte
  Dienstleistungen, erhobene Informationen, erteilte Informationen,
  Angemessenheits-/Eignungspruefung, erbrachte Dienstleistungen.
  Aufbewahrung: 10 Jahre nach Beendigung der Geschaeftsbeziehung.
- Art. 16: Rechenschaftspflicht: Kopie der Dokumentation auf Anfrage,
  Depotauszuege, Zusammensetzung und Bewertung des Portfolios,
  Verwendung von Finanzinstrumenten der Kunden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class fidleg_dokumentation_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Dokumentation nach Art. 15 ist vollstaendig"
    reference = "SR 950.1 Art. 15"


class fidleg_dokumentation_aufbewahrungsfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Aufbewahrungsfrist fuer Dokumentation (Jahre)"
    reference = "SR 950.1 Art. 15"

    def formula_2020(person, period, parameters):
        import numpy as np

        p = parameters(period).sr950_1
        return np.full(person.count, p.dokumentation_aufbewahrung_jahre)


class fidleg_rechenschaft_erteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Rechenschaft nach Art. 16 auf Anfrage erteilt"
    reference = "SR 950.1 Art. 16"
