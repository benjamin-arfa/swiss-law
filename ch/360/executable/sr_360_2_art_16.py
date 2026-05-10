"""SR 360.2 Art. 16

Generated from: ch/360/de/360.2.md

Periodische Gesamtueberpruefung der Daten in der Unterkategorie
Informationsfall: Alle 5 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_informationsfall_pruefintervall_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Intervall fuer Gesamtueberpruefung der Informationsfall-Daten in Jahren"
    reference = "SR 360.2 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        return person('nes_informationsfall_pruefintervall_jahre', period) * 0 + 5


class nes_jahre_seit_erstem_eintrag(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit Erfassung des ersten Eintrags im Datenblock"
    reference = "SR 360.2 Art. 16 Abs. 1"


class nes_gesamtpruefung_faellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtueberpruefung des Informationsfall-Datenblocks ist faellig"
    reference = "SR 360.2 Art. 16"

    def formula(person, period, parameters):
        jahre = person('nes_jahre_seit_erstem_eintrag', period)
        return (jahre > 0) * ((jahre % 5) == 0)
