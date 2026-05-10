"""SR 411.3 Art. 3

Generated from: ch/411/de/411.3.md

Bedingungen - Vorrangige Platzvergabe an Kinder von Bundesangestellten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_kind_von_bundesangestelltem(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist das Kind eines Angestellten der Bundesverwaltung"
    reference = "SR 411.3 Art. 3"


class ist_kind_von_angestelltem_nach_art_1(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist das Kind eines Angestellten nach Art. 1 Abs. 2 Bst. a (Bundesverwaltung oder Organisation im Interesse des Bundes)"
    reference = "SR 411.3 Art. 3"


class anmeldungen_ueberschreiten_kapazitaet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ueberschreiten die Anmeldungen die Aufnahmekapazitaeten der ECLF"
    reference = "SR 411.3 Art. 3"


class hat_vorrang_bei_platzvergabe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat das Kind Vorrang bei der Platzvergabe an der ECLF"
    reference = "SR 411.3 Art. 3"

    def formula(person, period):
        ueberschreitung = person('anmeldungen_ueberschreiten_kapazitaet', period)
        ist_art1 = person('ist_kind_von_angestelltem_nach_art_1', period)
        # Vorrang nur relevant wenn Kapazitaet ueberschritten
        return ueberschreitung * ist_art1


class hat_prioritaet_bei_platzvergabe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat das Kind hoechste Prioritaet (Bundesverwaltung vor anderen Art.1-Angestellten)"
    reference = "SR 411.3 Art. 3"

    def formula(person, period):
        vorrang = person('hat_vorrang_bei_platzvergabe', period)
        ist_bund = person('ist_kind_von_bundesangestelltem', period)
        return vorrang * ist_bund
