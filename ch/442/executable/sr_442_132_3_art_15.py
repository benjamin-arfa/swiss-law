"""SR 442.132.3 Art. 15

Generated from: ch/442/de/442.132.3.md

Praktikantenlohn:
- Kategorie I (Berufsmaturitaet): 1'800 CHF/Monat bzw. 23'400 CHF/Jahr
- Kategorie II (Fachhochschule/Uni): 2'500 CHF/Monat bzw. 32'500 CHF/Jahr
- Kategorie III (nach Abschluss FH/Uni): 3'200 CHF/Monat bzw. 41'600 CHF/Jahr
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class praktikanten_kategorie(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Praktikanten-Kategorie (1=Berufsmatur, 2=FH/Uni, 3=nach Abschluss)"
    reference = "SR 442.132.3 Art. 15 Abs. 2"


class praktikantenlohn_monatlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Monatlicher Praktikantenlohn inkl. 13. Monatslohn (CHF)"
    reference = "SR 442.132.3 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        kat = person('praktikanten_kategorie', period.this_year)
        return (kat == 1) * 1800 + (kat == 2) * 2500 + (kat == 3) * 3200


class praktikantenlohn_jaehrlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Praktikantenlohn inkl. 13. Monatslohn (CHF)"
    reference = "SR 442.132.3 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        kat = person('praktikanten_kategorie', period)
        return (kat == 1) * 23400 + (kat == 2) * 32500 + (kat == 3) * 41600
