"""SR 195.1 Art. 26

Generated from: ch/195/de/195.1.md

Ausschlussgruende: Sozialhilfe kann verweigert oder entzogen werden bei
bestimmten Gruenden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_oeffentliche_interessen_geschaedigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person schweizerische oeffentliche Interessen schwer geschaedigt hat"
    reference = "SR 195.1 Art. 26 lit. a"


class hat_unwahre_angaben_gemacht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person wissentlich durch unwahre oder unvollstaendige Angaben Leistungen erwirkt oder zu erwirken versucht"
    reference = "SR 195.1 Art. 26 lit. b"


class verweigert_auskunft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person sich weigert, Auskunft zu erteilen oder zur Einholung von Auskuenften zu ermaechtigen"
    reference = "SR 195.1 Art. 26 lit. c"


class erfuellt_auflagen_nicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Bedingungen/Auflagen nicht erfuellt oder wesentliche Aenderungen nicht meldet"
    reference = "SR 195.1 Art. 26 lit. d"


class unterlaesst_zumutbares(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person das ihr Zumutbare offensichtlich unterlaesst um ihre Lage zu verbessern"
    reference = "SR 195.1 Art. 26 lit. e"


class verwendet_leistungen_missbraeuchlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Sozialhilfeleistungen missbraeuchlich verwendet"
    reference = "SR 195.1 Art. 26 lit. f"


class sozialhilfe_ausschlussgrund_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Ausschlussgrund fuer Sozialhilfe vorliegt"
    reference = "SR 195.1 Art. 26"

    def formula(person, period, parameters):
        a = person('hat_oeffentliche_interessen_geschaedigt', period)
        b = person('hat_unwahre_angaben_gemacht', period)
        c = person('verweigert_auskunft', period)
        d = person('erfuellt_auflagen_nicht', period)
        e = person('unterlaesst_zumutbares', period)
        f = person('verwendet_leistungen_missbraeuchlich', period)
        return a + b + c + d + e + f > 0
