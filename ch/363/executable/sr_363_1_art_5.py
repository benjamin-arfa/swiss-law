"""SR 363.1 Art. 5

Generated from: ch/363/de/363.1.md

Meldepflicht: Labors melden dem EJPD innert 30 Tagen Aenderungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class labor_aenderung_angaben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Labor hat Aenderungen bei den Anerkennungsangaben"
    reference = "SR 363.1 Art. 5"


class labor_meldefrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer die Meldung von Aenderungen an das EJPD (Tage)"
    reference = "SR 363.1 Art. 5"

    def formula(person, period, parameters):
        return person('labor_aenderung_angaben', period) * 0 + 30
