"""SR 442.133 Art. 8

Generated from: ch/442/de/442.133.md

Bemessung der Finanzhilfen: Verteilschluessel aus 3 gleichgewichteten Indikatoren:
1. Staendige Wohnbevoelkerung pro Kanton
2. Staendige Wohnbevoelkerung 0-19 Jahre pro Kanton
3. Anzahl Fachbelegungen an Musikschulen pro Kanton
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wohnbevoelkerung_kanton(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Staendige Wohnbevoelkerung des Kantons"
    reference = "SR 442.133 Art. 8 Abs. 2 Bst. a"


class wohnbevoelkerung_0_19_kanton(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Staendige Wohnbevoelkerung 0-19 Jahre des Kantons"
    reference = "SR 442.133 Art. 8 Abs. 2 Bst. b"


class fachbelegungen_musikschulen_kanton(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Fachbelegungen an Musikschulen im Kanton"
    reference = "SR 442.133 Art. 8 Abs. 2 Bst. c"
