"""SR 196.1 Art. 15

Generated from: ch/196/de/196.1.md

Vermutung der Unrechtmaessigkeit: Unter bestimmten Bedingungen wird vermutet,
dass Vermoegenswerte unrechtmaessig erworben wurden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermoegen_ausserordentlich_stark_gestiegen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Vermoegen beguenstigt durch die Ausuebung des oeffentlichen Amts ausserordentlich stark gestiegen ist"
    reference = "SR 196.1 Art. 15 Abs. 1 lit. a"


class korruptionsgrad_pep_oder_staat_notorisch_hoch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Korruptionsgrad des Herkunftsstaats oder der PEP waehrend deren Amtszeit notorisch hoch war"
    reference = "SR 196.1 Art. 15 Abs. 1 lit. b"


class rechtmaessiger_erwerb_ueberwiegend_nachgewiesen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob mit ueberwiegender Wahrscheinlichkeit nachgewiesen wurde, dass die Vermoegenswerte rechtmaessig erworben wurden"
    reference = "SR 196.1 Art. 15 Abs. 3"


class vermutung_unrechtmaessigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vermutung gilt, dass Vermoegenswerte unrechtmaessig erworben wurden"
    reference = "SR 196.1 Art. 15"

    def formula(person, period, parameters):
        anstieg = person('vermoegen_ausserordentlich_stark_gestiegen', period)
        korruption = person('korruptionsgrad_pep_oder_staat_notorisch_hoch', period)
        umgestossen = person('rechtmaessiger_erwerb_ueberwiegend_nachgewiesen', period)
        # Vermutung greift wenn beide Bedingungen erfuellt und nicht umgestossen
        return anstieg * korruption * (1 - umgestossen)
