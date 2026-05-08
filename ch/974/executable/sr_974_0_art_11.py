"""SR 974.0 Art. 11

Generated from: ch/974/de/974.0.md

Private Bestrebungen:
- Bundesrat kann private Institutionen unterstützen, die den Grundsätzen
  und Zielen des Gesetzes entsprechen
- Angemessene Eigenleistung erforderlich
- Kann juristische Personen gründen oder sich an solchen beteiligen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_private_institution_entwicklungszusammenarbeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine private Institution der Entwicklungszusammenarbeit handelt"
    reference = "SR 974.0 Art. 11 Abs. 1"


class entspricht_grundsaetzen_und_zielen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Bestrebungen den Grundsätzen und Zielen des Gesetzes entsprechen"
    reference = "SR 974.0 Art. 11 Abs. 1"


class erbringt_angemessene_eigenleistung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Institution eine angemessene Eigenleistung erbringt"
    reference = "SR 974.0 Art. 11 Abs. 1"


class berechtigt_fuer_bundesunterstuetzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die private Institution für Bundesunterstützung berechtigt ist"
    reference = "SR 974.0 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        privat = person('ist_private_institution_entwicklungszusammenarbeit', period)
        grundsaetze = person('entspricht_grundsaetzen_und_zielen', period)
        eigenleistung = person('erbringt_angemessene_eigenleistung', period)
        return privat * grundsaetze * eigenleistung
