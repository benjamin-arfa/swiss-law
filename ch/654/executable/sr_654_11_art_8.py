"""SR 654.11 Art. 8 - Vernichtung der Daten

Generated from: ch/654/de/654.11.md

The ESTV must destroy the data no later than 20 years after the end
of the calendar year in which it received them.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class aufbewahrungsfrist_daten_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Aufbewahrungsfrist der Daten durch die ESTV (Jahre nach Empfang)"
    reference = "SR 654.11 Art. 8"
    default_value = 20


class jahr_datenempfang(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kalenderjahr, in dem die ESTV die Daten erhalten hat"
    reference = "SR 654.11 Art. 8"


class daten_muessen_vernichtet_werden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Daten muessen spaetestens in diesem Jahr vernichtet werden"
    reference = "SR 654.11 Art. 8"

    def formula(self, period, parameters):
        jahr_empfang = self('jahr_datenempfang', period)
        frist = self('aufbewahrungsfrist_daten_jahre', period)
        return period.start.year >= (jahr_empfang + frist)
