"""SR 455.102.4 Art. 4

Generated from: ch/455/de/455.102.4.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class staerkstes_belastendes_merkmal_kategorie(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Belastungskategorie des am staerksten belastenden Merkmals oder Symptoms (Art. 4 Abs. 2 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 4 Abs. 2"


class zugeordnete_belastungskategorie(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Zugeordnete Belastungskategorie des Tieres nach Art. 4 SR 455.102.4"
    reference = "SR 455.102.4 Art. 4"

    def formula(person, period, parameters):
        # Art. 4 Abs. 2: Das am staerksten belastende Merkmal bestimmt die Kategorie
        return person('staerkstes_belastendes_merkmal_kategorie', period)
