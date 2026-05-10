"""SR 210 Art. 33

Generated from: ch/de/210.md

Beweis fuer Geburt und Tod - Beweismittel: Der Beweis fuer die Geburt oder
den Tod einer Person wird mit den Zivilstandsurkunden gefuehrt. Fehlen
solche oder sind die vorhandenen als unrichtig erwiesen, so kann der Beweis
auf andere Weise erbracht werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_zivilstandsurkunde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Zivilstandsurkunden fuer Geburt/Tod vorliegen"
    reference = "SR 210 Art. 33 Abs. 1"
    default_value = True


class ist_zivilstandsurkunde_unrichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die vorhandenen Zivilstandsurkunden als unrichtig erwiesen sind"
    reference = "SR 210 Art. 33 Abs. 2"


class kann_beweis_anderweitig_erbringen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Beweis fuer Geburt/Tod auf andere Weise erbracht werden kann"
    reference = "SR 210 Art. 33 Abs. 2"

    def formula(person, period, parameters):
        # Abs. 2: Wenn keine Urkunden vorhanden oder als unrichtig erwiesen
        hat_urkunde = person('hat_zivilstandsurkunde', period)
        ist_unrichtig = person('ist_zivilstandsurkunde_unrichtig', period)
        return not_(hat_urkunde) + ist_unrichtig > 0
