"""SR 520.20 Art. 8

Generated from: ch/520/de/520.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class bund_oder_kanton_traegt_betriebskosten(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Der Bund oder der Kanton traegt die Kosten fuer Betrieb und Unterhalt der Schutzanlage waehrend der Requisition"
    reference = "SR 520.20 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return person('requisition_voraussetzungen_erfuellt', period)


class fachkundiges_personal_betrieb(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Infrastruktur wird von fachkundigem Personal betrieben und unterhalten"
    reference = "SR 520.20 Art. 8 Abs. 2"
