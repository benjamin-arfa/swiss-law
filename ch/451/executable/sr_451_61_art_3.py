"""SR 451.61 Art. 3

Generated from: ch/451/de/451.61.md
Nagoya-Verordnung - Sorgfaltspflicht und Aufbewahrungsdauer 10 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ende_nutzung_genetische_ressource_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr des Endes der Nutzung oder des unmittelbaren Erzielens von Vorteilen"
    reference = "SR 451.61 Art. 3 Abs. 5 Bst. a"


class ressource_noch_aufbewahrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Genetische Ressource oder Produkt wird noch aufbewahrt"
    reference = "SR 451.61 Art. 3 Abs. 5 Bst. b"


class aufbewahrungspflicht_nagoya(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aufbewahrungspflicht fuer Informationen besteht noch"
    reference = "SR 451.61 Art. 3 Abs. 5"

    def formula(person, period, parameters):
        ende = person('ende_nutzung_genetische_ressource_jahr', period)
        noch_aufbewahrt = person('ressource_noch_aufbewahrt', period)
        aktuelles_jahr = period.start.year

        # Bst. a: 10 Jahre nach Ende der Nutzung
        frist_a = (aktuelles_jahr - ende) <= 10

        # Bst. b: solange Ressource/Produkt aufbewahrt wird
        return frist_a + noch_aufbewahrt
