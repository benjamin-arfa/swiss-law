"""SR 443.11 Art. 8

Generated from: ch/443/de/443.11.md

Erhebung der Abgabe: Monatliche Meldung bis 15. des Folgemonats.
Zahlungsfrist 30 Tage. Verzugszins 5%.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class monatliche_eintritte_kinoregion(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Entgeltliche Eintritte eines Monats in der Kinoregion"
    reference = "SR 443.11 Art. 8 Abs. 1"


class zahlungsfrist_filmabgabe_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Zahlungsfrist fuer Filmabgabe in Tagen"
    reference = "SR 443.11 Art. 8 Abs. 2"
    default_value = 30


class verzugszins_filmabgabe_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verzugszins bei verspaeteter Zahlung der Filmabgabe"
    reference = "SR 443.11 Art. 8 Abs. 3"
    default_value = 5.0
