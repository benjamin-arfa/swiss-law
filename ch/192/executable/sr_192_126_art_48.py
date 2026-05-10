"""SR 192.126 Art. 48

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ueberstunden_pro_monat(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Geleistete Ueberstunden pro Monat"
    reference = "SR 192.126 Art. 48"

class ueberstunden_zuschlag_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Zuschlag fuer Ueberstundenarbeit in Prozent (Art. 48 Abs. 3)"
    reference = "SR 192.126 Art. 48"

    def formula(person, period, parameters):
        # Art. 48 Abs. 3: Ueberstunden werden mit einem Zuschlag von 25% entschaedigt
        return person('ueberstunden_pro_monat', period) * 0 + 25
