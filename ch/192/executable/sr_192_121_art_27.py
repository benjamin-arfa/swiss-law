"""SR 192.121 Art. 27

Generated from: ch/192/de/192.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finanzbeitrag_einmalig_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Einmaliger Finanzbeitrag in CHF"
    reference = "SR 192.121 Art. 27"

class finanzbeitrag_wiederkehrend_jahr_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Wiederkehrender Finanzbeitrag pro Jahr in CHF"
    reference = "SR 192.121 Art. 27"

class finanzbeitrag_entscheid_bundesrat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat entscheidet ueber Finanzbeitrag (>3M einmalig oder >2M/Jahr, Art. 27 Abs. 1)"
    reference = "SR 192.121 Art. 27"

    def formula(person, period, parameters):
        einmalig = person('finanzbeitrag_einmalig_chf', period)
        wiederkehrend = person('finanzbeitrag_wiederkehrend_jahr_chf', period)
        return (einmalig > 3_000_000) + (wiederkehrend > 2_000_000) > 0

class finanzbeitrag_entscheid_eda(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EDA entscheidet ueber Finanzbeitrag (<=3M einmalig oder <=2M/Jahr, Art. 27 Abs. 2)"
    reference = "SR 192.121 Art. 27"

    def formula(person, period, parameters):
        einmalig = person('finanzbeitrag_einmalig_chf', period)
        wiederkehrend = person('finanzbeitrag_wiederkehrend_jahr_chf', period)
        return (einmalig <= 3_000_000) * (wiederkehrend <= 2_000_000)
