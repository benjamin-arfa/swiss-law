"""SR 514.54 Art. 8

Generated from: ch/514/de/514.54.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_person(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person in Jahren"


class steht_unter_umfassender_beistandschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person steht unter umfassender Beistandschaft"


class selbst_oder_drittgefaehrdung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person gibt Anlass zur Annahme, dass sie sich selbst oder Dritte gefaehrdet"


class vorstrafe_gewalt_oder_gemeingefaehrlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person erscheint im Privatauszug wegen gewalttaetiger Handlung oder wiederholter Verbrechen"


class waffenerwerbsschein_ausschlussgründe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat Ausschlussgruende fuer Waffenerwerbsschein (Art. 8 Abs. 2 SR 514.54)"
    reference = "SR 514.54 Art. 8"

    def formula(person, period, parameters):
        alter = person('alter_person', period)
        beistandschaft = person('steht_unter_umfassender_beistandschaft', period)
        gefaehrdung = person('selbst_oder_drittgefaehrdung', period)
        vorstrafe = person('vorstrafe_gewalt_oder_gemeingefaehrlich', period)

        # Keinen Waffenerwerbsschein erhalten Personen die:
        # a) unter 18 Jahre alt
        # b) unter umfassender Beistandschaft stehen
        # c) sich selbst oder Dritte gefaehrden
        # d) wegen Gewalt/Gemeingefaehrlichkeit/wiederholter Verbrechen vorbestraft
        zu_jung = alter < 18
        return zu_jung + beistandschaft + gefaehrdung + vorstrafe


class darf_waffenerwerbsschein_erhalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person darf Waffenerwerbsschein erhalten (Art. 8 SR 514.54)"
    reference = "SR 514.54 Art. 8"

    def formula(person, period, parameters):
        ausschluss = person('waffenerwerbsschein_ausschlussgründe', period)
        return ausschluss == False
