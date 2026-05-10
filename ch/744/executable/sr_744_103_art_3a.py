"""SR 744.103 Art. 3a

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_jahresrechnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Unternehmen verfügt über eine Jahresrechnung (Erfolgsrechnung, Bilanz, OR-Angaben)"
    reference = "SR 744.103 Art. 3a Abs. 1"

    def formula(person, period, parameters):
        return person('jahresrechnung_vorhanden', period)


class jahresrechnung_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Jahresrechnung ist vorhanden"
    reference = "SR 744.103 Art. 3a Abs. 1"


class ist_einzelunternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Unternehmen ist ein Einzelunternehmen"
    reference = "SR 744.103 Art. 3a Abs. 2"


class kein_vermoegen_in_steuerveranlagung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "In der Steuerveranlagung ist aufgrund von Freibeträgen kein Vermögen ausgewiesen"
    reference = "SR 744.103 Art. 3a Abs. 2"


class revision_nach_or_vorgeschrieben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Obligationenrecht schreibt die Revision der Jahresrechnung vor"
    reference = "SR 744.103 Art. 3a Abs. 4"


class unternehmensdauer_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Monate seit Unternehmensgründung"
    reference = "SR 744.103 Art. 3a Abs. 3"


class nachweis_durch_steuerveranlagung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einzelunternehmen ohne Jahresrechnung darf finanzielle Leistungsfähigkeit anhand Steuerveranlagung nachweisen"
    reference = "SR 744.103 Art. 3a Abs. 2"

    def formula(person, period, parameters):
        return person('ist_einzelunternehmen', period) * ~person('hat_jahresrechnung', period)


class muss_steuererklarung_zusaetzlich_einreichen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Neben der Steuerveranlagung ist zusätzlich die vollständige Steuererklärung einzureichen"
    reference = "SR 744.103 Art. 3a Abs. 2"

    def formula(person, period, parameters):
        nachweis_via_steuer = person('nachweis_durch_steuerveranlagung_zulaessig', period)
        kein_vermoegen = person('kein_vermoegen_in_steuerveranlagung', period)
        return nachweis_via_steuer * kein_vermoegen


class muss_eroeffnungsbilanz_oder_aktuelle_jahresrechnung_einreichen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen unter 15 Monaten muss Eröffnungsbilanz oder aktuelle Jahresrechnung (Bilanz + Erfolgsrechnung) einreichen"
    reference = "SR 744.103 Art. 3a Abs. 3"

    def formula(person, period, parameters):
        dauer = person('unternehmensdauer_monate', period)
        return dauer < 15


class muss_revisorenbericht_einreichen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mit der Jahresrechnung oder Eröffnungsbilanz ist ein Revisorenbericht einzureichen"
    reference = "SR 744.103 Art. 3a Abs. 4"

    def formula(person, period, parameters):
        return person('revision_nach_or_vorgeschrieben', period)


class nachweis_finanzielle_leistungsfaehigkeit_sr_744_103(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nachweis der finanziellen Leistungsfähigkeit gemäss SR 744.103 Art. 3a ist erbracht"
    reference = "SR 744.103 Art. 3a"

    def formula(person, period, parameters):
        hat_jr = person('hat_jahresrechnung', period)
        junges_unternehmen = person('unternehmensdauer_monate', period) < 15
        einzelunternehmen_via_steuer = person('nachweis_durch_steuerveranlagung_zulaessig', period)

        nachweis_standard = hat_jr * ~junges_unternehmen
        nachweis_jung = junges_unternehmen
        nachweis_einzelunternehmen = einzelunternehmen_via_steuer

        return nachweis_standard + nachweis_jung + nachweis_einzelunternehmen
