"""SR 232.16 Art. 6

Generated from: ch/232/de/232.16.md

Art. 6 defines exceptions where the consent of the variety protection
holder is NOT required.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class handlung_im_privaten_bereich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Handlung erfolgt im privaten Bereich zu nicht gewerblichen Zwecken"
    reference = "SR 232.16 Art. 6 lit. a"


class handlung_zu_versuchszwecken(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Handlung erfolgt zu Versuchszwecken"
    reference = "SR 232.16 Art. 6 lit. b"


class handlung_zur_schaffung_neuer_sorten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Handlung erfolgt zum Zweck der Schaffung neuer Sorten"
    reference = "SR 232.16 Art. 6 lit. c"


class sortenschutz_ausnahme_art_6(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ausnahme vom Sortenschutz nach Art. 6 (keine Zustimmung erforderlich)"
    reference = "SR 232.16 Art. 6"

    def formula(person, period, parameters):
        privat = person('handlung_im_privaten_bereich', period)
        versuch = person('handlung_zu_versuchszwecken', period)
        neue_sorten = person('handlung_zur_schaffung_neuer_sorten', period)
        return privat + versuch + neue_sorten > 0
