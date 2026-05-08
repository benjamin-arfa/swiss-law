"""SR 923.0 Art. 6

Generated from: ch/923/de/923.0.md

Art. 6: Fremde Arten, Rassen und Varietäten - Non-native species:
1. Federal permit required for:
   a. Importing and introducing non-native species/breeds/varieties of fish and crayfish
   b. Introducing non-local species/breeds/varieties
2. Permit granted if: a. native fauna not endangered; b. no undesired fauna change
3. Federal Council may provide for exceptions
4. Non-native species may not be used as live bait fish
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bgf_art_ist_landesfremd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Art/Rasse/Varietät ist landesfremd"
    reference = "SR 923.0 Art. 6 Abs. 1 Bst. a"


class bgf_art_ist_standortfremd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Art/Rasse/Varietät ist standortfremd"
    reference = "SR 923.0 Art. 6 Abs. 1 Bst. b"


class bgf_einheimische_fauna_nicht_gefaehrdet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einheimische Tier- und Pflanzenwelt wird nicht gefährdet"
    reference = "SR 923.0 Art. 6 Abs. 2 Bst. a"


class bgf_keine_unerwuenschte_faunaveraenderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Keine unerwünschte Veränderung der Fauna"
    reference = "SR 923.0 Art. 6 Abs. 2 Bst. b"


class bgf_bewilligung_fremde_art_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bundesbewilligung für fremde Art/Rasse/Varietät ist erforderlich"
    reference = "SR 923.0 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        landesfremd = person('bgf_art_ist_landesfremd', period)
        standortfremd = person('bgf_art_ist_standortfremd', period)
        return (landesfremd + standortfremd) > 0


class bgf_bewilligung_fremde_art_erteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bewilligung für fremde Art kann erteilt werden (Voraussetzungen erfüllt)"
    reference = "SR 923.0 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        erforderlich = person('bgf_bewilligung_fremde_art_erforderlich', period)
        fauna_ok = person('bgf_einheimische_fauna_nicht_gefaehrdet', period)
        keine_veraenderung = person('bgf_keine_unerwuenschte_faunaveraenderung', period)
        return erforderlich * fauna_ok * keine_veraenderung
