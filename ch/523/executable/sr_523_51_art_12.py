"""SR 523.51 Art. 12

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class anzahl_modulwiederholungen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Wiederholungen eines Moduls"
    reference = "SR 523.51 Art. 12 Abs. 1"


class modul_wiederholung_erlaubt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wiederholung des Moduls ist erlaubt"
    reference = "SR 523.51 Art. 12 Abs. 1-2"

    def formula(person, period, parameters):
        wiederholungen = person('anzahl_modulwiederholungen', period)
        begruendetes_versaeumnis = person('versaeumnis_begruendet', period.first_month)
        # Max 1 Wiederholung, ausser bei begruendetem Versaeumnis
        return (wiederholungen < 1) + begruendetes_versaeumnis
