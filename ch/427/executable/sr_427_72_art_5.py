"""SR 427.72 Art. 5

Generated from: ch/427/de/427.72.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class thematik_wissenschaftlich_geeignet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Thematik ist fuer eine wissenschaftliche Erforschung geeignet"
    reference = "SR 427.72 Art. 5 Abs. 2 lit. a"


class thematik_nicht_bereits_bearbeitet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Thematik wird nicht bereits bearbeitet"
    reference = "SR 427.72 Art. 5 Abs. 2 lit. b"


class thematik_im_einklang_mit_forschungsprogramm(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Thematik steht im Einklang mit den Prioritaeten des Forschungsprogramms des ASTRA"
    reference = "SR 427.72 Art. 5 Abs. 2 lit. c"


class beitrag_zur_loesung_oeffentliches_interesse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Von der Erforschung kann ein Beitrag zur Loesung von Aufgaben im oeffentlichen Interesse erwartet werden"
    reference = "SR 427.72 Art. 5 Abs. 2 lit. d"


class kommission_empfiehlt_gutheissung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Kommission empfiehlt dem ASTRA die Gutheissung des Gesuchs"
    reference = "SR 427.72 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        geeignet = person('thematik_wissenschaftlich_geeignet', period)
        nicht_bearbeitet = person('thematik_nicht_bereits_bearbeitet', period)
        einklang = person('thematik_im_einklang_mit_forschungsprogramm', period)
        oeffentlich = person('beitrag_zur_loesung_oeffentliches_interesse', period)
        return geeignet * nicht_bearbeitet * einklang * oeffentlich
