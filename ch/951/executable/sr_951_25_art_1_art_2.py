"""SR 951.25 Art. 1–2

Generated from: ch/951/de/951.25.md

Zweck und Foerderungsgrundsaetze des KMU-Buergschaftsgesetzes:
- Art. 1: Erleichterung der Bankkreditaufnahme fuer leistungs- und
  entwicklungsfaehige KMU; Foerderung von Neugruendungen.
- Art. 2: Beruecksichtigung der Landesregionen; landesweites Angebot;
  besondere Beruecksichtigung gewerbetreibender Frauen und Personen
  mit Ziel selbststaendiger Erwerbstaetigkeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class kmu_buergschaft_ist_kmu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unternehmen ist ein leistungs- und entwicklungsfaehiges KMU"
    reference = "SR 951.25 Art. 1 Abs. 1"


class kmu_buergschaft_ist_neugruendung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unternehmen ist eine Neugruendung"
    reference = "SR 951.25 Art. 1 Abs. 1"


class kmu_buergschaft_ist_gewerbetreibende_frau(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesuchstellerin ist gewerbetreibende Frau (Art. 2 lit. c)"
    reference = "SR 951.25 Art. 2 lit. c"


class kmu_buergschaft_strebt_selbstaendigkeit_an(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person strebt selbststaendige Erwerbstaetigkeit an"
    reference = "SR 951.25 Art. 2 lit. c"


class kmu_buergschaft_foerderungsberechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "KMU erfuellt Foerderungsvoraussetzungen nach Art. 1-2"
    reference = "SR 951.25 Art. 1–2"

    def formula_2007(person, period, parameters):
        ist_kmu = person('kmu_buergschaft_ist_kmu', period)
        return ist_kmu
