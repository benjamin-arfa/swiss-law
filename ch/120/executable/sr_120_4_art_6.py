"""SR 120.4 Art. 6

Generated from: ch/120/de/120.4.md

Dritte: Third parties must undergo PSP when working on classified projects.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_dritter_an_klassifiziertem_projekt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Dritte/r an einem klassifizierten Projekt mitwirkt"
    reference = "SR 120.4 Art. 6 lit. a"


class psp_pflicht_aufgrund_abkommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person aufgrund internationaler Informationsschutzabkommen geprueft werden muss"
    reference = "SR 120.4 Art. 6 lit. b"


class psp_pflicht_dritte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Dritte einer PSP unterzogen werden"
    reference = "SR 120.4 Art. 6"

    def formula(person, period, parameters):
        klassifiziert = person('ist_dritter_an_klassifiziertem_projekt', period) * (
            person('zugang_vertraulich_klassifizierte_informationen', period) +
            person('zugang_geheim_klassifizierte_informationen', period) +
            person('zugang_schutzzone_2', period) +
            person('zugang_schutzzone_3', period)
        )
        abkommen = person('psp_pflicht_aufgrund_abkommen', period)
        return (klassifiziert + abkommen) > 0
