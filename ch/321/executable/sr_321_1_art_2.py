"""SR 321.1 Art. 2

Generated from: ch/321/de/321.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class teilnahme_spanischer_buergerkrieg_republikanisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person nahm an Kampfhandlungen auf republikanischer Seite im Spanischen Buergerkrieg teil oder versuchte es oder leistete Hilfe"
    reference = "SR 321.1 Art. 2"


class rechtlich_zur_verantwortung_gezogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person wurde wegen Handlungen im Spanischen Buergerkrieg rechtlich zur Verantwortung gezogen"
    reference = "SR 321.1 Art. 2"


class faellt_unter_rehabilitierungsgesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person faellt unter den Geltungsbereich des Rehabilitierungsgesetzes"
    reference = "SR 321.1 Art. 2"

    def formula(person, period, parameters):
        teilnahme = person('teilnahme_spanischer_buergerkrieg_republikanisch', period)
        verantwortung = person('rechtlich_zur_verantwortung_gezogen', period)
        return teilnahme * verantwortung
