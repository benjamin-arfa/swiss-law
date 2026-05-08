"""SR 951.25 Art. 5–8

Generated from: ch/951/de/951.25.md

Finanzhilfen, Buergschaftslimite und Finanzierung:
- Art. 5: Finanzhilfen fuer Verlustdeckung und Verwaltungskosten;
  nachrangige Darlehen in Ausnahmefaellen.
- Art. 6: Buergschaftslimite max. CHF 1'000'000; Bund uebernimmt 65%
  des Buergschaftsverlustes.
- Art. 7: Bund beteiligt sich an Verwaltungskosten; Kuerzung bei
  Reinertrag-Verteilung an Eigentuemer.
- Art. 8: Verpflichtungskredite fuer Darlehen; Netto-Buergschaftsvolumen
  max. CHF 600 Mio.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class kmu_buergschaft_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag der gewaehrten Buergschaft (CHF)"
    reference = "SR 951.25 Art. 6 Abs. 1"


class kmu_buergschaft_verlust(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Eingetretener Buergschaftsverlust (CHF)"
    reference = "SR 951.25 Art. 6 Abs. 2"


class kmu_buergschaft_betrag_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Buergschaftsbetrag liegt innerhalb der Limite (max. CHF 1 Mio.)"
    reference = "SR 951.25 Art. 6 Abs. 1"

    def formula_2019(person, period, parameters):
        betrag = person('kmu_buergschaft_betrag', period)
        p = parameters(period).sr951_25
        limite = p.buergschaftslimite
        return betrag <= limite


class kmu_buergschaft_bund_verlustanteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anteil des Bundes am Buergschaftsverlust (CHF)"
    reference = "SR 951.25 Art. 6 Abs. 2"

    def formula_2019(person, period, parameters):
        verlust = person('kmu_buergschaft_verlust', period)
        p = parameters(period).sr951_25
        anteil = p.bund_verlustanteil  # 0.65
        return verlust * anteil


class kmu_buergschaft_org_verteilt_reinertrag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Organisation verteilt Reinertrag an Eigentuemer"
    reference = "SR 951.25 Art. 7 Abs. 2"


class kmu_buergschaft_verwaltungskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Verwaltungskosten der Buergschaftsorganisation (CHF)"
    reference = "SR 951.25 Art. 7 Abs. 1"


class kmu_buergschaft_reinertrag_verteilung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag des an Eigentuemer verteilten Reinertrags (CHF)"
    reference = "SR 951.25 Art. 7 Abs. 2"


class kmu_buergschaft_bund_verwaltungskosten_beitrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Beitrag des Bundes an Verwaltungskosten (CHF)"
    reference = "SR 951.25 Art. 7"

    def formula_2019(person, period, parameters):
        import numpy as np

        kosten = person('kmu_buergschaft_verwaltungskosten', period)
        verteilt_reinertrag = person('kmu_buergschaft_org_verteilt_reinertrag', period)
        reinertrag = person('kmu_buergschaft_reinertrag_verteilung', period)

        # Abs. 2: Kuerzung in Hoehe des verteilten Reinertrags
        kuerzung = np.where(verteilt_reinertrag, reinertrag, 0.0)
        beitrag = np.maximum(kosten - kuerzung, 0.0)
        return beitrag


class kmu_buergschaft_netto_volumen_max(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximales Netto-Buergschaftsvolumen (CHF 600 Mio.)"
    reference = "SR 951.25 Art. 8 Abs. 2"

    def formula_2019(person, period, parameters):
        import numpy as np

        p = parameters(period).sr951_25
        return np.full(person.count, p.netto_volumen_max)
