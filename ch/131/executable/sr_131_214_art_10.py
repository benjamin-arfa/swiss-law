"""SR 131.214 Art. 10

Generated from: ch/131/de/131.214.md

Menschenwürde: Die Würde des Menschen ist unantastbar.
Establishes human dignity as an inviolable fundamental right.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class menschenwuerde_garantiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Menschenwürde verfassungsrechtlich garantiert ist"
    reference = "SR 131.214 Art. 10"
    default_value = True

    def formula(person, period, parameters):
        # Human dignity is guaranteed unconditionally for all persons in Canton Uri
        # This is a fundamental constitutional principle
        return parameters(period).grundrechte_uri.menschenwuerde_schutz


class verletzung_menschenwuerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Verletzung der Menschenwürde vorliegt"
    reference = "SR 131.214 Art. 10"
    default_value = False


class anspruch_schutz_menschenwuerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Schutz der Menschenwürde"
    reference = "SR 131.214 Art. 10"

    def formula(person, period, parameters):
        # Everyone has a right to protection of their human dignity
        menschenwuerde_garantiert = person('menschenwuerde_garantiert', period)
        verletzung = person('verletzung_menschenwuerde', period)

        # Right to protection exists when dignity is guaranteed and there is a violation
        return menschenwuerde_garantiert * verletzung