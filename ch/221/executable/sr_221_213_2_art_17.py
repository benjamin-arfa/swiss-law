"""SR 221.213.2 Art. 17

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wichtige_gruende_fuer_vorzeitige_kuendigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wichtige Gründe machen Vertragserfüllung unzumutbar"
    reference = "SR 221.213.2 Art. 17 Abs. 1"


class vorzeitige_kuendigung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorzeitige Kündigung ist zulässig"
    reference = "SR 221.213.2 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        return person('wichtige_gruende_fuer_vorzeitige_kuendigung', period)


class vorzeitige_kuendigungsfrist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kündigungsfrist bei vorzeitiger Kündigung in Monaten"
    reference = "SR 221.213.2 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        # Die Kündigungsfrist beträgt sechs Monate
        return person.filled_array(6)
