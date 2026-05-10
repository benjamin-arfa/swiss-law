"""SR 311.0 Art. 22

Generated from: ch/fr/311/311.0.md

Art. 22: Punissabilite de la tentative (Strafbarkeit des Versuchs)
- Abs. 1: Sentence may be mitigated if execution not completed or
  required result did not or could not occur.
- Abs. 2: Not punishable if offender did not realize completion was
  absolutely impossible due to nature of object or means used (untauglicher Versuch).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stgb_tat_vollendet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Tat vollendet wurde (Vollendung eingetreten)"
    reference = "SR 311.0 Art. 22 Abs. 1"


class stgb_versuch_untauglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob ein untauglicher Versuch vorliegt (Vollendung objektiv unmoeglich)"
    reference = "SR 311.0 Art. 22 Abs. 2"


class stgb_grober_unverstand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob grober Unverstand vorliegt (Taeter erkannte Unmöglichkeit nicht)"
    reference = "SR 311.0 Art. 22 Abs. 2"


class stgb_versuch_strafbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Versuch strafbar ist"
    reference = "SR 311.0 Art. 22"

    def formula(person, period, parameters):
        vollendet = person('stgb_tat_vollendet', period)
        untauglich = person('stgb_versuch_untauglich', period)
        unverstand = person('stgb_grober_unverstand', period)

        # Completed acts: always punishable (not attempt)
        # Attempted: punishable unless untauglich + grober Unverstand
        return vollendet + not_(vollendet) * not_(untauglich * unverstand)


class stgb_versuch_strafmilderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Strafmilderung wegen Versuch moeglich ist"
    reference = "SR 311.0 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        vollendet = person('stgb_tat_vollendet', period)
        return not_(vollendet)
