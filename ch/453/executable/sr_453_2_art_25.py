"""SR 453.2 Art. 25

Generated from: ch/453/de/453.2.md
Archivierung und Loeschung - Daten nach spaetestens 10 Jahren geloescht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class daten_erfassung_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr der Erfassung der Daten im Informationssystem"
    reference = "SR 453.2 Art. 25 Abs. 2"


class daten_fischerei_zu_loeschen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten sind zu loeschen (spaetestens 10 Jahre nach Erfassung)"
    reference = "SR 453.2 Art. 25 Abs. 2"

    def formula(person, period, parameters):
        erfassung = person('daten_erfassung_jahr', period)
        aktuelles_jahr = period.start.year
        return (aktuelles_jahr - erfassung) >= 10
