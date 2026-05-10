"""SR 235.1 Art. 8

Generated from: ch/235/de/235.1.md

Auskunftsrecht: Jede Person kann Auskunft verlangen, ob Daten ueber sie
bearbeitet werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_auskunft_verlangt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat Auskunft ueber Bearbeitung ihrer Daten verlangt"
    reference = "SR 235.1 Art. 8 Abs. 1"


class dsg_daten_werden_bearbeitet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten ueber die Person werden bearbeitet"
    reference = "SR 235.1 Art. 8 Abs. 1"


class dsg_auskunftsrecht_besteht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat ein Auskunftsrecht gemaess Art. 8 DSG"
    reference = "SR 235.1 Art. 8"

    def formula(person, period, parameters):
        # Jede Person kann Auskunft verlangen - Recht besteht immer
        return person('dsg_auskunft_verlangt', period) * 0 + 1


class dsg_auskunft_kostenlos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auskunft ist kostenlos zu erteilen (Abs. 5, Grundsatz)"
    reference = "SR 235.1 Art. 8 Abs. 5"

    def formula(person, period, parameters):
        return person('dsg_auskunft_verlangt', period) * 0 + 1


class dsg_auskunftsrecht_unverzichtbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auf das Auskunftsrecht kann nicht im Voraus verzichtet werden"
    reference = "SR 235.1 Art. 8 Abs. 6"

    def formula(person, period, parameters):
        return person('dsg_auskunft_verlangt', period) * 0 + 1
