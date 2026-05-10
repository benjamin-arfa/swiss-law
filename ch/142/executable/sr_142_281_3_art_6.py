"""SR 142.281.3 Art. 6

Generated from: ch/142/de/142.281.3.md

Zuschlag fuer Umgebungsarbeiten und bewegliche Ausstattung bei Umbauten:
Zuschlag in Hoehe der anerkannten Kosten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_umbau(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen Umbau handelt (nicht Neubau)"
    reference = "SR 142.281.3 Art. 6"


class anerkannte_kosten_umgebung_ausstattung_umbau(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anerkannte Kosten fuer Umgebungsarbeiten und Ausstattung bei Umbauten (CHF)"
    reference = "SR 142.281.3 Art. 6"


class zuschlag_umbau_umgebung_ausstattung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zuschlag fuer Umgebungsarbeiten und Ausstattung bei Umbauten (CHF)"
    reference = "SR 142.281.3 Art. 6"

    def formula(person, period, parameters):
        ist_um = person('ist_umbau', period)
        kosten = person('anerkannte_kosten_umgebung_ausstattung_umbau', period)
        return where(ist_um, kosten, 0.0)
