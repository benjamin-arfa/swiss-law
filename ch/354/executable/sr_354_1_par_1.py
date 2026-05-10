"""SR 354.1 § 1

Generated from: ch/354/de/354.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_polizeitransport(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Handelt es sich um einen Polizeitransport im Sinne der Uebereinkunft"
    reference = "SR 354.1 § 1"

    def formula(person, period):
        von_polizei_angeordnet = person('transport_von_polizei_angeordnet', period)
        betrifft_abschiebung_oder_heimschaffung = person('betrifft_abschiebung_oder_heimschaffung', period)
        return von_polizei_angeordnet * betrifft_abschiebung_oder_heimschaffung


class transport_von_polizei_angeordnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Transport wurde von der Polizei angeordnet"
    reference = "SR 354.1 § 1 Abs. 1"


class betrifft_abschiebung_oder_heimschaffung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Betrifft die Abschiebung oder Heimschaffung von Personen zwischen Kantonen oder ins/vom Ausland"
    reference = "SR 354.1 § 1 Abs. 1"
