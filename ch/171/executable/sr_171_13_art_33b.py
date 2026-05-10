"""SR 171.13 Art. 33b

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class frist_antraege_legislaturplanung_stunden(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist in Stunden für Einreichung von Anträgen zur Legislaturplanung vor Detailberatungsbeginn"
    reference = "SR 171.13 Art. 33b Abs. 2"

    def formula(person, period, parameters):
        return 24


class frist_mitteilung_antragseinreichung_wochen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist in Wochen für die Mitteilung der Antragseinreichungsfrist an Fraktionen"
    reference = "SR 171.13 Art. 33b Abs. 3"

    def formula(person, period, parameters):
        return 3
