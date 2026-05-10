"""SR 128.51 Art. 5

Generated from: ch/128/de/128.51.md

Priorisierung der Beratung und Unterstuetzung bei Cyberangriffen: When demand
exceeds BACS capacity, it may prioritize consulting/support considering public
safety, population welfare, and economic functioning.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nachfrage_uebersteigt_bacs_kapazitaet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Nachfrage nach Beratung und Unterstuetzung die Kapazitaeten des BACS uebersteigt"
    reference = "SR 128.51 Art. 5 Abs. 1"


class bacs_darf_priorisieren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BACS die Beratung und Unterstuetzung priorisieren darf"
    reference = "SR 128.51 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('nachfrage_uebersteigt_bacs_kapazitaet', period)
