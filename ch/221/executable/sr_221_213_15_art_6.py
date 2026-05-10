"""SR 221.213.15 Art. 6

Generated from: ch/221/de/221.213.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rahmenmietvertrag_erfuellt_art3(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rahmenmietvertrag genügt den Erfordernissen nach Artikel 3"
    reference = "SR 221.213.15 Art. 6 lit. a"


class repraesentative_organisationen_nicht_abgelehnt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Repräsentative Organisationen haben Allgemeinverbindlicherklärung nicht ausdrücklich abgelehnt"
    reference = "SR 221.213.15 Art. 6 lit. b"


class allgemeinverbindlichkeit_im_oeffentlichen_interesse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Allgemeinverbindlicherklärung liegt im öffentlichen Interesse und dient dem Wohnfrieden"
    reference = "SR 221.213.15 Art. 6 lit. c"


class allgemeinverbindlicherklaerung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Allgemeinverbindlicherklärung darf angeordnet werden"
    reference = "SR 221.213.15 Art. 6"

    def formula(person, period, parameters):
        art3 = person('rahmenmietvertrag_erfuellt_art3', period)
        nicht_abgelehnt = person('repraesentative_organisationen_nicht_abgelehnt', period)
        oeffentliches_interesse = person('allgemeinverbindlichkeit_im_oeffentlichen_interesse', period)
        return art3 * nicht_abgelehnt * oeffentliches_interesse
