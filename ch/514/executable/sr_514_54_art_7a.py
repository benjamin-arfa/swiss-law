"""SR 514.54 Art. 7a

Generated from: ch/514/de/514.54.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class betroffen_von_verbot_art_7(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist von einem Verbot nach Art. 7 Abs. 1 betroffen"


class meldefrist_monate_nach_verbot(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Meldefrist nach Inkrafttreten des Verbots in Monaten (Art. 7a Abs. 1 SR 514.54)"
    reference = "SR 514.54 Art. 7a"

    def formula(person, period, parameters):
        # Innerhalb von zwei Monaten melden
        return 2


class frist_ausnahmebewilligung_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Gesuch Ausnahmebewilligung in Monaten (Art. 7a Abs. 2 SR 514.54)"
    reference = "SR 514.54 Art. 7a"

    def formula(person, period, parameters):
        # Innerhalb von sechs Monaten
        return 6


class frist_uebertragung_nach_abweisung_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist zur Uebertragung nach Abweisung des Gesuchs in Monaten (Art. 7a Abs. 3 SR 514.54)"
    reference = "SR 514.54 Art. 7a"

    def formula(person, period, parameters):
        # Innerhalb von vier Monaten nach Abweisung
        return 4
