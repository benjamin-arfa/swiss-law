"""SR 351.6 Art. 53

Generated from: ch/351/de/351.6.md
Conditions for Switzerland to accept execution of ICC sentences.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verurteilte_person_ist_schweizer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verurteilte Person ist Schweizer Buergerin oder Buerger"
    reference = "SR 351.6 Art. 53 Abs. 1 lit. a"


class verurteilte_person_hat_aufenthalt_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verurteilte Person hat ihren gewoehnlichen Aufenthalt in der Schweiz"
    reference = "SR 351.6 Art. 53 Abs. 1 lit. b"


class ist_geldstrafe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sanktion ist eine Geldstrafe"
    reference = "SR 351.6 Art. 53 Abs. 2"


class verurteilte_hat_vermoegenswerte_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verurteilte Person verfuegt in der Schweiz ueber Vermoegenswerte"
    reference = "SR 351.6 Art. 53 Abs. 2"


class vollstreckung_freiheitsstrafe_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schweiz kann die Vollstreckung der Freiheitsstrafe uebernehmen"
    reference = "SR 351.6 Art. 53 Abs. 1"

    def formula(person, period):
        schweizer = person('verurteilte_person_ist_schweizer', period)
        aufenthalt = person('verurteilte_person_hat_aufenthalt_schweiz', period)
        return schweizer + aufenthalt


class vollstreckung_geldstrafe_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geldstrafe kann in der Schweiz vollstreckt werden"
    reference = "SR 351.6 Art. 53 Abs. 2"

    def formula(person, period):
        freiheitsstrafe_ok = person('vollstreckung_freiheitsstrafe_zulaessig', period)
        geldstrafe = person('ist_geldstrafe', period)
        vermoegen_ch = person('verurteilte_hat_vermoegenswerte_schweiz', period)
        # Geldstrafen auch wenn Person im Ausland, aber Vermoegen in CH
        return geldstrafe * (freiheitsstrafe_ok + vermoegen_ch)
