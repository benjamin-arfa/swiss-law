"""SR 523.51 Art. 22a

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class versichert_nach_mvg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Versichert nach dem Bundesgesetz ueber die Militaerversicherung (MVG)"
    reference = "SR 523.51 Art. 22a Abs. 1"

    def formula(person, period, parameters):
        return person('ist_lehrpersonal_zivilschutz', period)


class versicherung_sache_arbeitgeber(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Versicherung ist Sache des Arbeitgebers oder der Organisation"
    reference = "SR 523.51 Art. 22a Abs. 2"

    def formula(person, period, parameters):
        return not_(person('ist_lehrpersonal_zivilschutz', period))
