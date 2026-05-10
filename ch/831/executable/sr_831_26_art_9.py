"""SR 831.26 Art. 9

Generated from: ch/831/de/831.26.md

Complaint right of organizations: nationwide disability organizations
that have existed for at least 10 years can file complaints against
institution recognition decisions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_behindertenorganisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Behindertenorganisation handelt"
    reference = "SR 831.26 Art. 9 Abs. 1"


class organisation_gesamtschweizerisch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation von gesamtschweizerischer Bedeutung ist"
    reference = "SR 831.26 Art. 9 Abs. 1"


class organisation_bestehensdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Bestehensdauer der Organisation in Jahren"
    reference = "SR 831.26 Art. 9 Abs. 1"


class organisation_beschwerderecht_anerkennung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Beschwerderecht gegen Anerkennung einer Institution"
    reference = "SR 831.26 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        ist_org = person('ist_behindertenorganisation', period)
        gesamt_ch = person('organisation_gesamtschweizerisch', period)
        dauer = person('organisation_bestehensdauer_jahre', period)
        return ist_org * gesamt_ch * (dauer >= 10)
