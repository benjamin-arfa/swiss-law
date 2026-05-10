"""SR 121.3 Art. 6

Generated from: ch/121/de/121.3.md

Erteilung von Auskuenften: Employees must provide complete and truthful
information to AB-ND. No disadvantages may result from truthful disclosures.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class befragt_durch_ab_nd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person von der AB-ND befragt wird"
    reference = "SR 121.3 Art. 6 Abs. 1"


class auskunftspflicht_ab_nd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person zur vollstaendigen und wahrheitsgetreuen Auskunft verpflichtet ist"
    reference = "SR 121.3 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return person('befragt_durch_ab_nd', period)


class nachteilsverbot_bei_auskunft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Person keinerlei Nachteile aus wahrheitsgemaeessen Auskuenften erwachsen duerfen"
    reference = "SR 121.3 Art. 6 Abs. 4"

    def formula(person, period, parameters):
        return person('befragt_durch_ab_nd', period)
