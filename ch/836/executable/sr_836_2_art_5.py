"""SR 836.2 Art. 5

Generated from: ch/836/de/836.2.md

Art. 5: Höhe der Familienzulagen; Anpassung der Ansätze.
Abs. 1: Kinderzulage mindestens 215 CHF/Monat (Stand 2025).
Abs. 2: Ausbildungszulage mindestens 268 CHF/Monat (Stand 2025).
Abs. 3: Bundesrat passt Ansätze der Teuerung an (wenn LIK >= 5 Punkte).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mindestansatz_kinderzulage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Mindestansatz der Kinderzulage pro Monat (Art. 5 Abs. 1 FamZG)"
    reference = "SR 836.2 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        # Mindestens 215 CHF pro Monat (Stand 2025, angepasst gemäss
        # V vom 28. Aug. 2024 über Anpassung an Preisentwicklung)
        return 215.0


class mindestansatz_ausbildungszulage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Mindestansatz der Ausbildungszulage pro Monat (Art. 5 Abs. 2 FamZG)"
    reference = "SR 836.2 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        # Mindestens 268 CHF pro Monat (Stand 2025, angepasst gemäss
        # V vom 28. Aug. 2024 über Anpassung an Preisentwicklung)
        return 268.0


class betrag_kinderzulage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Monatlicher Betrag der Kinderzulage (Art. 5 Abs. 1 FamZG)"
    reference = "SR 836.2 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        anspruch = person('anspruch_kinderzulage', period)
        mindestansatz = person('mindestansatz_kinderzulage', period)
        return anspruch * mindestansatz


class betrag_ausbildungszulage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Monatlicher Betrag der Ausbildungszulage (Art. 5 Abs. 2 FamZG)"
    reference = "SR 836.2 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        anspruch = person('anspruch_ausbildungszulage', period)
        mindestansatz = person('mindestansatz_ausbildungszulage', period)
        return anspruch * mindestansatz
