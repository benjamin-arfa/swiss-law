"""SR 611.010 Art. 4

Generated from: ch/611/de/611.010.md

Art. 4: Sparaufträge im Rahmen des Konsolidierungs- und
Aufgabenüberprüfungspakets 2014. Einsparungen gegenüber dem Finanzplan
vom 22. August 2012.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einsparung_eigenbereich_bundesverwaltung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Einsparungen im Eigenbereich der Bundesverwaltung in Mio. CHF (Art. 4 Abs. 1)"
    reference = "SR 611.010 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        # Art. 4 Abs. 1 Ziff. 1: Massnahmen im Eigenbereich der Bundesverwaltung: 60.3 Mio.
        return 60.3


class einsparung_entwicklungszusammenarbeit(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kürzungen in der Entwicklungszusammenarbeit in Mio. CHF (Art. 4 Abs. 1)"
    reference = "SR 611.010 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        # Art. 4 Abs. 1 Ziff. 2: Kürzungen in der Entwicklungszusammenarbeit: 38.5 Mio.
        return 38.5


class einsparung_aussennetz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Optimierungen Aussennetz in Mio. CHF (Art. 4 Abs. 1)"
    reference = "SR 611.010 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        # Art. 4 Abs. 1 Ziff. 3: Optimierungen Aussennetz: 6.3 Mio.
        return 6.3
