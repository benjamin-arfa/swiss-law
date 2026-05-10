"""SR 121.3 Art. 11

Generated from: ch/121/de/121.3.md

Bezeichnung und Gesuche: Cantons designate oversight bodies and report them.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class entscheid_einsichtsverweigerung_frist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist in Tagen fuer Entscheid ueber Verweigerung der Einsicht"
    reference = "SR 121.3 Art. 11 Abs. 4"

    def formula(person, period, parameters):
        return 30  # 30 Tage
