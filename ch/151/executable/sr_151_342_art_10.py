"""SR 151.342 Art. 10

Generated from: ch/151/de/151.342.md

Erreichbarkeit der Haltepunkte im Bus- und Trolleybusverkehr:
Maximale Neigungen und Durchfahrbreiten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class neigung_zugang_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Neigung des Zugangs zum Haltepunkt in Prozent"
    reference = "SR 151.342 Art. 10"


class zugang_beheizt_oder_gedeckt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Zugang beheizt oder gedeckt ist"
    reference = "SR 151.342 Art. 10 Abs. 2"


class neigung_zugang_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Neigung des Zugangs den Anforderungen entspricht"
    reference = "SR 151.342 Art. 10"

    def formula(person, period, parameters):
        neigung = person('neigung_zugang_prozent', period)
        beheizt = person('zugang_beheizt_oder_gedeckt', period)
        # Einstufig: max 6% normal, mehrstufig: max 10% (12% beheizt/gedeckt)
        max_neigung = beheizt * 12 + (1 - beheizt) * 10
        return neigung <= max_neigung


class durchfahrbreite_perron_cm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Durchfahrbreite auf dem Perron in cm"
    reference = "SR 151.342 Art. 10 Abs. 4"


class sturzgefahr_fahrbahn(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob fuer Rollstuehle Sturzgefahr auf die Fahrbahn besteht"
    reference = "SR 151.342 Art. 10 Abs. 4"


class durchfahrbreite_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Durchfahrbreite den Anforderungen entspricht"
    reference = "SR 151.342 Art. 10 Abs. 4"

    def formula(person, period, parameters):
        breite = person('durchfahrbreite_perron_cm', period)
        sturzgefahr = person('sturzgefahr_fahrbahn', period)
        min_breite = sturzgefahr * 120 + (1 - sturzgefahr) * 90
        return breite >= min_breite
