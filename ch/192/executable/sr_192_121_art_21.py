"""SR 192.121 Art. 21

Generated from: ch/192/de/192.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wohnt_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person wohnt in der Schweiz"
    reference = "SR 192.121 Art. 21"

class nebenerwerbstaetig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person uebt eine Nebenerwerbstaetigkeit aus"
    reference = "SR 192.121 Art. 21"

class nebenerwerb_wochenstunden(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Wochenstunden der Nebenerwerbstaetigkeit"
    reference = "SR 192.121 Art. 21"

class nebenerwerb_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Nebenerwerbstaetigkeit ist zulaessig (max. 10 Wochenstunden, Art. 21 Abs. 2)"
    reference = "SR 192.121 Art. 21"

    def formula(person, period, parameters):
        wohnt_ch = person('wohnt_in_schweiz', period.this_year)
        stunden = person('nebenerwerb_wochenstunden', period)
        return wohnt_ch * (stunden <= 10)

class nebenerwerb_keine_immunitaet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Keine Vorrechte oder Immunitaeten fuer Nebenerwerbstaetigkeit (Art. 21 Abs. 4)"
    reference = "SR 192.121 Art. 21"

    def formula(person, period, parameters):
        return person('nebenerwerbstaetig', period)

class nebenerwerb_einkommen_steuerpflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einkommen aus Nebenerwerbstaetigkeit ist in der Schweiz steuerpflichtig (Art. 21 Abs. 6)"
    reference = "SR 192.121 Art. 21"

    def formula(person, period, parameters):
        return person('nebenerwerbstaetig', period)
