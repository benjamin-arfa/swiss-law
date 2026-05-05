"""SR 142.209 Art. 10

Generated from: ch/142/de/142.209.md

Bundesgebuehren des SEM:
- Voruebergehende Aufhebung eines Einreiseverbotes: 150 CHF
- Vorzeitige Aufhebung eines Einreiseverbotes: 150 CHF
- ZEMIS-Datenbearbeitungsgebuehr: max. 10 CHF pro Person und Jahr
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gebuehr_voruebergehende_aufhebung_einreiseverbot(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebuehr fuer voruebergehende Aufhebung eines Einreiseverbotes (CHF)"
    reference = "SR 142.209 Art. 10 Abs. 1 Bst. a"
    default_value = 150.0


class gebuehr_vorzeitige_aufhebung_einreiseverbot(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebuehr fuer vorzeitige Aufhebung eines Einreiseverbotes (CHF)"
    reference = "SR 142.209 Art. 10 Abs. 1 Bst. b"
    default_value = 150.0


class gebuehr_zemis_datenbearbeitung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche ZEMIS-Datenbearbeitungsgebuehr pro Auslaender/in (CHF, max. 10)"
    reference = "SR 142.209 Art. 10 Abs. 2"
    default_value = 10.0
