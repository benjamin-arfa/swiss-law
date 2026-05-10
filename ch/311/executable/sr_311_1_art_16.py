"""SR 311.1 Art. 16

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class maximale_einzeltrennung_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer der ununterbrochenen Trennung bei Disziplinarmassnahme (7 Tage)"
    reference = "SR 311.1 Art. 16 Abs. 2"
    default_value = 7


class alter_fuer_einrichtung_junge_erwachsene(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestalter fuer Vollzug in Einrichtung fuer junge Erwachsene (17 Jahre)"
    reference = "SR 311.1 Art. 16 Abs. 3"
    default_value = 17


class vollzug_in_einrichtung_junge_erwachsene_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kann die Massnahme in einer Einrichtung fuer junge Erwachsene vollzogen werden"
    reference = "SR 311.1 Art. 16 Abs. 3"

    def formula(person, period, parameters):
        alter = person('alter_bei_tat', period)
        return alter >= 17
