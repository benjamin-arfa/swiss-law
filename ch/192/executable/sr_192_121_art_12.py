"""SR 192.121 Art. 12

Generated from: ch/192/de/192.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_quasizwischenstaatlich_taetig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist in offizieller Eigenschaft fuer quasizwischenstaatliche Organisation taetig"
    reference = "SR 192.121 Art. 12"

class hat_schweizer_buergerrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person besitzt das Schweizer Buergerrecht"
    reference = "SR 192.121 Art. 12"

class gehalt_quasizwischenstaatlich(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gehalt von quasizwischenstaatlicher Organisation (CHF)"
    reference = "SR 192.121 Art. 12"

class befreiung_direkte_steuern_gehalt_quasi(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befreiung von direkten Steuern auf Gehaeltern der quasizwischenstaatlichen Organisation (Art. 12 Abs. 1 lit. a)"
    reference = "SR 192.121 Art. 12"

    def formula(person, period, parameters):
        taetig = person('ist_quasizwischenstaatlich_taetig', period)
        schweizer = person('hat_schweizer_buergerrecht', period)
        return taetig * (1 - schweizer)

class befreiung_einreise_aufenthalt_quasi(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befreiung von Einreise- und Aufenthaltsbestimmungen fuer Personal quasizwischenstaatlicher Organisationen (Art. 12 Abs. 1 lit. c)"
    reference = "SR 192.121 Art. 12"

    def formula(person, period, parameters):
        taetig = person('ist_quasizwischenstaatlich_taetig', period)
        schweizer = person('hat_schweizer_buergerrecht', period)
        return taetig * (1 - schweizer)
