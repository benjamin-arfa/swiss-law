"""SR 783.018 Art. 2

Generated from: ch/783/de/783.018.md

Grundsaetze: PostCom legt Gebuehr im Einzelfall nach Gebuehrenansaetzen fest.
Anpassung an Landesindex der Konsumentenpreise moeglich ab 5% Anstieg.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class landesindex_konsumentenpreise_anstieg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anstieg des Landesindex der Konsumentenpreise seit Inkrafttreten oder letzter Anpassung (in Prozent)"
    reference = "SR 783.018 Art. 2 Abs. 2"


SCHWELLENWERT_INDEX_ANPASSUNG = 5.0


class postcom_gebuehrenanpassung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Anpassung der Gebuehrenansaetze an den Konsumentenpreisindex zulaessig ist"
    reference = "SR 783.018 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        anstieg = person('landesindex_konsumentenpreise_anstieg', period)
        return anstieg >= SCHWELLENWERT_INDEX_ANPASSUNG
