"""SR 120.4 Art. 13

Generated from: ch/120/de/120.4.md

Ausnahme fuer versetzungspflichtiges und im Ausland eingesetztes Personal:
EDA may deviate from check level in urgent cases.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_versetzungspflichtiges_eda_personal(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person versetzungspflichtiges oder im Ausland eingesetztes EDA-Personal ist"
    reference = "SR 120.4 Art. 13 Abs. 1"


class zeitliche_dringlichkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob zeitliche Dringlichkeit vorliegt"
    reference = "SR 120.4 Art. 13 Abs. 1"


class abweichung_pruefstufe_eda_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob EDA von der Pruefstufe abweichen kann"
    reference = "SR 120.4 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('ist_versetzungspflichtiges_eda_personal', period) *
            person('zeitliche_dringlichkeit', period)
        )
