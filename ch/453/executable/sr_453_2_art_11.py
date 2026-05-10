"""SR 453.2 Art. 11

Generated from: ch/453/de/453.2.md
Bestandeskontrolle und Aufbewahrungspflicht - 3 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einfuhr_sendung_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr der Einfuhr der Sendung"
    reference = "SR 453.2 Art. 11 Abs. 2"


class aufbewahrungspflicht_fischerei_besteht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aufbewahrungspflicht fuer Begleitdokumente besteht noch (3 Jahre)"
    reference = "SR 453.2 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        einfuhr = person('einfuhr_sendung_jahr', period)
        aktuelles_jahr = period.start.year
        return (aktuelles_jahr - einfuhr) <= 3
