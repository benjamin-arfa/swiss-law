"""SR 836.1 Art. 18

Generated from: ch/836/de/836.1.md

Art. 18: Familienzulagen für landwirtschaftliche Arbeitnehmer - Financing.
Abs. 1: Employer contribution of 2% of cash and in-kind wages subject to AHV.
Abs. 4: Uncovered expenses: 2/3 federal, 1/3 cantonal.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class bar_und_naturallohn_ahv_pflichtig(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Im landwirtschaftlichen Betrieb ausgerichtete Bar- und Naturallöhne (AHV-pflichtig)"
    reference = "SR 836.1 Art. 18 Abs. 1"


class arbeitgeberbeitrag_familienzulagen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Arbeitgeberbeitrag für Familienzulagen: 2% der AHV-pflichtigen Löhne (Art. 18 Abs. 1 FLG)"
    reference = "SR 836.1 Art. 18 Abs. 1"

    def formula(person, period, parameters):
        loehne = person('bar_und_naturallohn_ahv_pflichtig', period)
        return loehne * 0.02


class ungedeckte_aufwendungen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Nicht durch Arbeitgeberbeiträge gedeckte Aufwendungen"
    reference = "SR 836.1 Art. 18 Abs. 4"


class bundesanteil_ungedeckte_aufwendungen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bundesanteil an ungedeckten Aufwendungen: 2/3 (Art. 18 Abs. 4 FLG)"
    reference = "SR 836.1 Art. 18 Abs. 4"

    def formula(person, period, parameters):
        return person('ungedeckte_aufwendungen', period) * (2.0 / 3.0)


class kantonsanteil_ungedeckte_aufwendungen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kantonsanteil an ungedeckten Aufwendungen: 1/3 (Art. 18 Abs. 4 FLG)"
    reference = "SR 836.1 Art. 18 Abs. 4"

    def formula(person, period, parameters):
        return person('ungedeckte_aufwendungen', period) * (1.0 / 3.0)
