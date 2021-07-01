"""SR 444.1 Art. 16

Generated from: ch/444/de/444.1.md

Sorgfaltspflichten im Kunsthandel: Identitaetsfeststellung, Unterrichtung
Kundschaft, Buchfuehrung (30 Jahre Aufbewahrung).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class aufbewahrungsfrist_buchfuehrung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsfrist fuer Aufzeichnungen und Belege in Jahren"
    reference = "SR 444.1 Art. 16 Abs. 3"
    default_value = 30


class sorgfaltspflichten_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sorgfaltspflichten im Kunsthandel eingehalten werden"
    reference = "SR 444.1 Art. 16"
