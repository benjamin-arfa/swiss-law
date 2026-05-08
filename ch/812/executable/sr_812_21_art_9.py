"""SR 812.21 Art. 9

Generated from: ch/812/de/812.21.md

Art. 9: Zulassung - Marketing authorization for medicines.
Ready-to-use medicines and veterinary premixes need Swissmedic authorization
to be placed on the market, with exceptions for:
- Formula magistralis (pharmacy compounding on prescription)
- Formula officinalis (pharmacopoeia-based compounding)
- Non-prescription pharmacy preparations
- Clinical trial medicines
- Non-standardizable medicines
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hmg_ist_verwendungsfertiges_arzneimittel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Arzneimittel ist verwendungsfertig"
    reference = "SR 812.21 Art. 9 Abs. 1"


class hmg_ist_formula_magistralis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Arzneimittel ist Formula magistralis (Herstellung auf ärztliche Verschreibung)"
    reference = "SR 812.21 Art. 9 Abs. 2 Bst. a"
    default_value = False


class hmg_ist_formula_officinalis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Arzneimittel ist Formula officinalis (nach Pharmakopöe-Monografie)"
    reference = "SR 812.21 Art. 9 Abs. 2 Bst. b"
    default_value = False


class hmg_ist_klinischer_versuch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Arzneimittel für klinische Versuche"
    reference = "SR 812.21 Art. 9 Abs. 2 Bst. d"
    default_value = False


class hmg_ist_nicht_standardisierbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Arzneimittel ist nicht standardisierbar"
    reference = "SR 812.21 Art. 9 Abs. 2 Bst. e"
    default_value = False


class hmg_zulassung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Swissmedic-Zulassung für Inverkehrbringen erforderlich"
    reference = "SR 812.21 Art. 9"

    def formula(person, period, parameters):
        verwendungsfertig = person('hmg_ist_verwendungsfertiges_arzneimittel', period)
        magistralis = person('hmg_ist_formula_magistralis', period)
        officinalis = person('hmg_ist_formula_officinalis', period)
        klinisch = person('hmg_ist_klinischer_versuch', period)
        nicht_standard = person('hmg_ist_nicht_standardisierbar', period)

        # Exceptions from authorization requirement
        ausnahme = magistralis + officinalis + klinisch + nicht_standard > 0

        return verwendungsfertig * not_(ausnahme)
