"""SR 311.0 Art. 42

Generated from: ch/fr/311/311.0.md

Art. 42: Sursis a l'execution de la peine (Bedingter Strafvollzug)
- Abs. 1: Suspended sentence for monetary penalty or imprisonment <= 2 years
  when a firm sentence is not necessary for deterrence.
- Abs. 2: If prior conviction of >6 months firm imprisonment within 5 years,
  suspension only in particularly favorable circumstances.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class stgb_strafe_ist_geldstrafe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um eine Geldstrafe handelt"
    reference = "SR 311.0 Art. 42 Abs. 1"


class stgb_freiheitsstrafe_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Dauer der Freiheitsstrafe in Monaten"
    reference = "SR 311.0 Art. 42 Abs. 1"


class stgb_vorstrafe_ueber_6_monate_letzte_5_jahre(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob eine unbedingte Vorstrafe von mehr als 6 Monaten in den letzten 5 Jahren vorliegt"
    reference = "SR 311.0 Art. 42 Abs. 2"


class stgb_besonders_guenstige_umstaende(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob besonders guenstige Umstaende vorliegen (fuer bedingten Vollzug trotz Vorstrafe)"
    reference = "SR 311.0 Art. 42 Abs. 2"


class stgb_bedingter_strafvollzug_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein bedingter Strafvollzug (Bewaehrung) moeglich ist"
    reference = "SR 311.0 Art. 42"

    def formula(person, period, parameters):
        geldstrafe = person('stgb_strafe_ist_geldstrafe', period)
        monate = person('stgb_freiheitsstrafe_monate', period)
        vorstrafe = person('stgb_vorstrafe_ueber_6_monate_letzte_5_jahre', period)
        guenstig = person('stgb_besonders_guenstige_umstaende', period)

        # Eligible: monetary penalty or imprisonment <= 24 months
        strafart_ok = geldstrafe + (monate <= 24) * (monate > 0)

        # No prior conviction issue, or particularly favorable circumstances
        vorstrafe_ok = not_(vorstrafe) + (vorstrafe * guenstig)

        return strafart_ok * vorstrafe_ok
