"""SR 512.271.1 Art. 19 – Einstufung und Dienstleistungen in der Kategorie A

Generated from: ch/512/de/512.271.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class pilot_unterkategorie(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Unterkategorie des Milizpiloten (A1, A2, A3, A4, B1, B2, B3)"
    reference = "SR 512.271.1 Art. 19-20"
    default_value = ""


class max_tage_individuelles_training(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Tage individuelles Training pro Jahr"
    reference = "SR 512.271.1 Art. 19-20"

    def formula(person, period, parameters):
        kat = person('pilot_unterkategorie', period)

        # Art. 19: Kategorie A
        # A/1: nach Bedarf (unbegrenzt) → encode as 365
        # A/2: max. 12 Tage
        # A/3: max. 12 Tage
        # A/4: max. 45 Tage
        # Art. 20: Kategorie B
        # B/1, B/2, B/3: max. 12 Tage
        return (
            where(kat == 'A1', 365,
            where(kat == 'A2', 12,
            where(kat == 'A3', 12,
            where(kat == 'A4', 45,
            where(kat == 'B1', 12,
            where(kat == 'B2', 12,
            where(kat == 'B3', 12, 0)))))))
        )


class minimale_flugstunden(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Minimale Anzahl Flugstunden pro Jahr"
    reference = "SR 512.271.1 Art. 19-20"

    def formula(person, period, parameters):
        kat = person('pilot_unterkategorie', period)

        # Art. 19: Kategorie A
        # A/1: 40 Stunden
        # A/2: 50 Stunden
        # A/3: 30 Stunden
        # A/4: 50 Stunden
        # Art. 20: Kategorie B
        # B/1, B/2, B/3: 20 Stunden
        return (
            where(kat == 'A1', 40,
            where(kat == 'A2', 50,
            where(kat == 'A3', 30,
            where(kat == 'A4', 50,
            where(kat == 'B1', 20,
            where(kat == 'B2', 20,
            where(kat == 'B3', 20, 0)))))))
        )
