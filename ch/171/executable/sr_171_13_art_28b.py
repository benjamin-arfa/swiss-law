"""SR 171.13 Art. 28b

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class frist_kommission_parl_initiative_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist in Jahren für Kommission zur Beschlussfassung über eine parlamentarische Initiative"
    reference = "SR 171.13 Art. 28b Abs. 1"

    def formula(person, period, parameters):
        return 1


class frist_rat_parl_initiative_sessionen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist in ordentlichen Sessionen für Behandlung einer parlamentarischen Initiative mit Folgegeben-Antrag"
    reference = "SR 171.13 Art. 28b Abs. 2"

    def formula(person, period, parameters):
        return 2
