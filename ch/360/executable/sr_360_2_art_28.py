"""SR 360.2 Art. 28

Generated from: ch/360/de/360.2.md

Finanzierung: Bund finanziert Datenleitungen, Kantone Endgeraete.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_kosten_bund(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten fuer Datenleitungen zum Hauptverteiler traegt der Bund"
    reference = "SR 360.2 Art. 28 Abs. 1"

    def formula(person, period, parameters):
        return person('nes_kosten_bund', period) * 0 + 1


class nes_kosten_kanton(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten fuer Geraete und Feinverteilung tragen die Kantone"
    reference = "SR 360.2 Art. 28 Abs. 2"

    def formula(person, period, parameters):
        return person('nes_kosten_kanton', period) * 0 + 1
