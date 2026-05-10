"""SR 151.3 Art. 22

Generated from: ch/151/de/151.3.md

Anpassungsfristen fuer den oeffentlichen Verkehr:
20 Jahre fuer Bauten/Anlagen/Fahrzeuge, 10 Jahre fuer Kommunikationssysteme.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_inkrafttreten_behig(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit Inkrafttreten des BehiG (1. Jan. 2004)"
    reference = "SR 151.3 Art. 22"


class anpassungsfrist_bauten_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die 20-jaehrige Anpassungsfrist fuer Bauten/Anlagen/Fahrzeuge abgelaufen ist"
    reference = "SR 151.3 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_inkrafttreten_behig', period)
        return jahre >= 20


class anpassungsfrist_kommunikation_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die 10-jaehrige Anpassungsfrist fuer Kommunikationssysteme/Billettausgabe abgelaufen ist"
    reference = "SR 151.3 Art. 22 Abs. 2"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_inkrafttreten_behig', period)
        return jahre >= 10
