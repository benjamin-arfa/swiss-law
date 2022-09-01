"""SR 120.4 Art. 22

Generated from: ch/120/de/120.4.md

Verfuegung: Four possible outcomes of the security check.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class PSP_VERFUEGUNG(Enum):
    keine = "Keine Verfuegung"
    sicherheitserklaerung = "Sicherheitserklaerung (unbedenklich)"
    sicherheitserklaerung_mit_auflagen = "Sicherheitserklaerung mit Auflagen (Risiko mit Vorbehalt)"
    risikoerklaerung = "Risikoerklaerung (Sicherheitsrisiko)"
    feststellungserklaerung = "Feststellungserklaerung (zu wenig Daten)"


class psp_verfuegung(Variable):
    value_type = Enum
    possible_values = PSP_VERFUEGUNG
    default_value = PSP_VERFUEGUNG.keine
    entity_key = 'person'
    definition_period = YEAR
    label = "Verfuegung der Pruefbehoerde"
    reference = "SR 120.4 Art. 22 Abs. 1"
