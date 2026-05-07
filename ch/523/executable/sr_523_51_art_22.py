"""SR 523.51 Art. 22

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class bund_traegt_ausbildungskosten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund traegt die Modulkosten und Reise/Unterkunft/Verpflegungskosten"
    reference = "SR 523.51 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        zivilschutz = person('ist_lehrpersonal_zivilschutz', period)
        fuehrung = person('ist_lehrpersonal_fuehrungsorgane', period)
        return zivilschutz + fuehrung


class arbeitgeber_traegt_kosten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Reise/Unterkunft/Verpflegungskosten werden durch Arbeitgeber oder Partnerorganisation getragen"
    reference = "SR 523.51 Art. 22 Abs. 2"

    def formula(person, period, parameters):
        return not_(person('bund_traegt_ausbildungskosten', period))
