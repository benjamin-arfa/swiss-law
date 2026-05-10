"""SR 952.02 Art. 5 — Publikumseinlagen

Generated from: ch/952/de/952.02.md

Abs. 1: Publikumseinlagen = Verbindlichkeiten gegenueber Kunden,
  ausgenommen die in Abs. 2 und 3 genannten.
Abs. 2: Nicht als Publikumseinlagen gelten Einlagen von:
  a) Banken/staatlich beaufsichtigte Unternehmen
  b) Aktionaere mit qualifizierter Beteiligung
  c) mit b) verbundene Personen
  d) institutionelle Anleger mit professioneller Tresorerie
  e) Arbeitnehmer beim Arbeitgeber
  f) Vereine/Stiftungen/Genossenschaften (nicht im Finanzbereich,
     ideeller Zweck, Laufzeit >= 6 Monate)
Abs. 3: Nicht als Einlagen gelten u.a. Gegenleistungen aus Vertraegen,
  Anleihensobligationen, Habensaldi zur Abwicklung (innert 60 Tagen),
  Gelder im Zusammenhang mit Vorsorge, Kleinbetraege fuer Zahlungsmittel,
  bankgarantierte Gelder.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bankv_verbindlichkeiten_gegenueber_kunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamte Verbindlichkeiten gegenueber Kundinnen und Kunden (CHF)"
    reference = "SR 952.02 Art. 5 Abs. 1"


class bankv_einlage_von_beaufsichtigtem_unternehmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einlage stammt von Bank oder staatlich beaufsichtigtem Unternehmen"
    reference = "SR 952.02 Art. 5 Abs. 2 lit. a"


class bankv_einlage_von_qualifiziert_beteiligtem(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einlage stammt von qualifiziert beteiligtem Aktionaer/Gesellschafter"
    reference = "SR 952.02 Art. 5 Abs. 2 lit. b"


class bankv_einlage_von_verbundener_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einlage stammt von mit qualifiziert Beteiligtem verbundener Person"
    reference = "SR 952.02 Art. 5 Abs. 2 lit. c"


class bankv_einlage_von_institutionellem_anleger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einlage stammt von institutionellem Anleger mit professioneller Tresorerie"
    reference = "SR 952.02 Art. 5 Abs. 2 lit. d"


class bankv_einlage_von_arbeitnehmer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einlage stammt von Arbeitnehmer beim eigenen Arbeitgeber"
    reference = "SR 952.02 Art. 5 Abs. 2 lit. e"


class bankv_einlage_bei_verein_stiftung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einlage bei Verein/Stiftung/Genossenschaft (ideeller Zweck, nicht Finanzbereich)"
    reference = "SR 952.02 Art. 5 Abs. 2 lit. f"


class bankv_einlage_laufzeit_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Laufzeit der Einlage bei Verein/Stiftung/Genossenschaft (Monate)"
    reference = "SR 952.02 Art. 5 Abs. 2 lit. f Ziff. 3"


class bankv_ist_publikumseinlage_ausgenommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einlage ist von der Definition Publikumseinlage ausgenommen (Abs. 2)"
    reference = "SR 952.02 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        beaufsichtigt = person('bankv_einlage_von_beaufsichtigtem_unternehmen', period)
        qualifiziert = person('bankv_einlage_von_qualifiziert_beteiligtem', period)
        verbunden = person('bankv_einlage_von_verbundener_person', period)
        institutionell = person('bankv_einlage_von_institutionellem_anleger', period)
        arbeitnehmer = person('bankv_einlage_von_arbeitnehmer', period)
        verein = person('bankv_einlage_bei_verein_stiftung', period)
        laufzeit = person('bankv_einlage_laufzeit_monate', period)

        p = parameters(period).sr952_02
        min_laufzeit = p.verein_einlage_min_laufzeit_monate  # 6

        verein_qualifiziert = verein * (laufzeit >= min_laufzeit)

        return (
            beaufsichtigt
            + qualifiziert
            + verbunden
            + institutionell
            + arbeitnehmer
            + verein_qualifiziert
        ) >= 1
