"""SR 122.1 Art. 2

Generated from: ch/122/de/122.1.md

Verfolgung und Beurteilung: Prosecution and adjudication of participation in
or support of a banned organisation fall under federal jurisdiction.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beteiligung_an_verbotener_organisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person an einer verbotenen Organisation oder Gruppierung beteiligt ist"
    reference = "SR 122.1 Art. 2"


class unterstuetzung_verbotener_organisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine verbotene Organisation oder Gruppierung unterstuetzt"
    reference = "SR 122.1 Art. 2"


class bundesgerichtsbarkeit_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Bundesgerichtsbarkeit fuer Verfolgung und Beurteilung zustaendig ist"
    reference = "SR 122.1 Art. 2"

    def formula(person, period, parameters):
        beteiligung = person('beteiligung_an_verbotener_organisation', period)
        unterstuetzung = person('unterstuetzung_verbotener_organisation', period)
        return beteiligung + unterstuetzung > 0
