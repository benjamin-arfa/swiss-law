"""SR 512.271.1 Art. 26 – Dienstleistungen der Milizbordoperateure

Generated from: ch/512/de/512.271.1.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class ist_milizbordoperateur(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Milizbordoperateur/in"
    reference = "SR 512.271.1 Art. 26"
    default_value = False


class max_tage_training_bordoperateur(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Tage individuelles Training für Milizbordoperateure"
    reference = "SR 512.271.1 Art. 26 lit. a"

    def formula(person, period, parameters):
        ist_bord = person('ist_milizbordoperateur', period)
        # Art. 26 lit. a: nach Bedarf, max 8 Tage
        return where(ist_bord, 8, 0)


class pflicht_flugstunden_bordoperateur(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Pflichtflugstunden pro Jahr für Milizbordoperateure"
    reference = "SR 512.271.1 Art. 26 lit. b"

    def formula(person, period, parameters):
        ist_bord = person('ist_milizbordoperateur', period)
        # Art. 26 lit. b: 20 Flugstunden
        return where(ist_bord, 20, 0)
