"""SR 235.1 Art. 38

Generated from: ch/235/de/235.1.md

Uebergangsbestimmungen: Fristen fuer Anmeldung und Auskunftsfaehigkeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_uebergangsfrist_anmeldung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Uebergangsfrist fuer Anmeldung bestehender Datensammlungen in Jahren"
    reference = "SR 235.1 Art. 38 Abs. 1"

    def formula(person, period, parameters):
        return person('dsg_uebergangsfrist_anmeldung_jahre', period) * 0 + 1


class dsg_uebergangsfrist_auskunft_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Uebergangsfrist fuer Auskunftsfaehigkeit in Jahren"
    reference = "SR 235.1 Art. 38 Abs. 2"

    def formula(person, period, parameters):
        return person('dsg_uebergangsfrist_auskunft_jahre', period) * 0 + 1
