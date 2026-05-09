"""SR 836.2 Art. 2

Generated from: ch/836/de/836.2.md

Art. 2: Begriff und Zweck der Familienzulagen.
Familienzulagen sind einmalige oder periodische Geldleistungen, die
ausgerichtet werden, um die finanzielle Belastung durch ein oder
mehrere Kinder teilweise auszugleichen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class anzahl_kinder(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Kinder, fuer die Familienzulagen beansprucht werden"
    reference = "SR 836.2 Art. 2"


class ist_familienzulage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ob eine Leistung als Familienzulage im Sinne von Art. 2 FamZG gilt"
    reference = "SR 836.2 Art. 2"

    def formula(person, period, parameters):
        # Familienzulagen setzen mindestens ein Kind voraus
        return person('anzahl_kinder', period) > 0
