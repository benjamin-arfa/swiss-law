"""SR 952.02 Art. 1 — Gegenstand

Generated from: ch/952/de/952.02.md

Die Bankenverordnung (BankV) regelt namentlich:
- Fuer Banken und Personen nach Art. 1b BankG: Bewilligungsvoraussetzungen,
  Organisationsanforderungen, Rechnungslegungsvorgaben.
- Fuer Banken: Einlagensicherung, nachrichtenlose Vermoegenswerte.
- Fuer systemrelevante Banken: Notfallplanung, Sanier-/Liquidierbarkeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class bankv_gegenstand_bewilligung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "BankV regelt Bewilligungsvoraussetzungen fuer dieses Institut"
    reference = "SR 952.02 Art. 1 lit. a"


class bankv_gegenstand_einlagensicherung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "BankV regelt Einlagensicherung fuer dieses Institut (nur Banken)"
    reference = "SR 952.02 Art. 1 lit. b"


class bankv_gegenstand_notfallplanung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "BankV regelt Notfallplanung fuer dieses Institut (nur systemrelevante Banken)"
    reference = "SR 952.02 Art. 1 lit. c"
