"""SR 741.01 Art. 9 - Ausmasse und Gewicht

Generated from: ch/de/741/741.01.md

Maximum vehicle dimensions and weights:
- Max weight: 40t (44t combined transport)
- Max height: 4m
- Max width: 2.55m (2.6m refrigerated)
- Max combination length: 18.75m
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class fahrzeug_gesamtgewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtgewicht des Fahrzeugs oder der Fahrzeugkombination in kg"
    reference = "SR 741.01 Art. 9 Abs. 1"


class fahrzeug_hoehe_m(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoehe des Fahrzeugs in Metern"
    reference = "SR 741.01 Art. 9 Abs. 1"


class fahrzeug_breite_m(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Breite des Fahrzeugs in Metern"
    reference = "SR 741.01 Art. 9 Abs. 1"


class fahrzeug_laenge_kombination_m(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Laenge der Fahrzeugkombination in Metern"
    reference = "SR 741.01 Art. 9 Abs. 1"


class ist_kombinierter_verkehr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Fahrzeug im kombinierten Verkehr eingesetzt wird"
    reference = "SR 741.01 Art. 9 Abs. 1"


class ist_klimatisiertes_fahrzeug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein klimatisiertes Fahrzeug handelt"
    reference = "SR 741.01 Art. 9 Abs. 1"


class fahrzeug_gewicht_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Fahrzeuggewicht innerhalb der zulaessigen Grenzen liegt"
    reference = "SR 741.01 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        gewicht = person('fahrzeug_gesamtgewicht_kg', period)
        kombiniert = person('ist_kombinierter_verkehr', period)
        max_gewicht = where(kombiniert, 44000.0, 40000.0)
        return gewicht <= max_gewicht


class fahrzeug_hoehe_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Fahrzeughoehe innerhalb der zulaessigen 4m liegt"
    reference = "SR 741.01 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return person('fahrzeug_hoehe_m', period) <= 4.0


class fahrzeug_breite_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Fahrzeugbreite innerhalb der zulaessigen Grenzen liegt"
    reference = "SR 741.01 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        breite = person('fahrzeug_breite_m', period)
        klimatisiert = person('ist_klimatisiertes_fahrzeug', period)
        max_breite = where(klimatisiert, 2.6, 2.55)
        return breite <= max_breite


class fahrzeug_laenge_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Laenge der Fahrzeugkombination innerhalb 18.75m liegt"
    reference = "SR 741.01 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return person('fahrzeug_laenge_kombination_m', period) <= 18.75


class fahrzeug_masse_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Ausmasse und Gewichte den Vorschriften entsprechen"
    reference = "SR 741.01 Art. 9"

    def formula(person, period, parameters):
        return (
            person('fahrzeug_gewicht_zulaessig', period)
            * person('fahrzeug_hoehe_zulaessig', period)
            * person('fahrzeug_breite_zulaessig', period)
            * person('fahrzeug_laenge_zulaessig', period)
        )
