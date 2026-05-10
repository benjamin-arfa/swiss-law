"""SR 128.51 Art. 8

Generated from: ch/128/de/128.51.md

Kommunikationssystem fuer den sicheren Informationsaustausch: Access to BACS
communication system for mandatory critical infrastructure operators,
Swiss-based organisations, and authorities.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_meldepflichtige_betreiberin_kritischer_infrastruktur(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation eine meldepflichtige Betreiberin kritischer Infrastrukturen ist"
    reference = "SR 128.51 Art. 8 Abs. 1"


class ist_organisation_mit_sitz_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation ihren Sitz in der Schweiz hat"
    reference = "SR 128.51 Art. 8 Abs. 1"


class ist_behoerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Behoerde handelt"
    reference = "SR 128.51 Art. 8 Abs. 1"


class zugang_bacs_kommunikationssystem(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation Zugang zum BACS-Kommunikationssystem hat"
    reference = "SR 128.51 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        krit_infra = person('ist_meldepflichtige_betreiberin_kritischer_infrastruktur', period)
        schweiz = person('ist_organisation_mit_sitz_in_schweiz', period)
        behoerde = person('ist_behoerde', period)
        return krit_infra + schweiz + behoerde > 0
