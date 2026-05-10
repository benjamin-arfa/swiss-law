"""SR 744.10 Art. 5

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nicht_wegen_verbrechens_verurteilt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person wurde in den letzten zehn Jahren nicht wegen eines Verbrechens verurteilt"
    reference = "SR 744.10 Art. 5 Abs. 1 lit. a"

    def formula(person, period, parameters):
        return person('keine_verbrechensverurteilung_letzte_10_jahre', period)


class keine_verbrechensverurteilung_letzte_10_jahre(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Keine Verurteilung wegen eines Verbrechens in den letzten zehn Jahren"
    reference = "SR 744.10 Art. 5 Abs. 1 lit. a"

    def formula(person, period, parameters):
        return person('verurteilung_wegen_verbrechens_letzte_10_jahre', period) == False


class verurteilung_wegen_verbrechens_letzte_10_jahre(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verurteilung wegen eines Verbrechens in den letzten zehn Jahren"
    reference = "SR 744.10 Art. 5 Abs. 1 lit. a"


class schwere_wiederholte_widerhandlungen_entlohnung_arbeitsbedingungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schwere und wiederholte Widerhandlungen gegen Entlöhnungs- und Arbeitsbedingungen (inkl. Lenk- und Ruhezeiten)"
    reference = "SR 744.10 Art. 5 Abs. 1 lit. b Ziff. 1"


class schwere_wiederholte_widerhandlungen_strassenverkehrssicherheit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schwere und wiederholte Widerhandlungen gegen Vorschriften über die Sicherheit im Strassenverkehr"
    reference = "SR 744.10 Art. 5 Abs. 1 lit. b Ziff. 2"


class schwere_wiederholte_widerhandlungen_fahrzeugbau_ausruestung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schwere und wiederholte Widerhandlungen gegen Vorschriften über Bau und Ausrüstung der Strassenfahrzeuge (Masse und Gewichte)"
    reference = "SR 744.10 Art. 5 Abs. 1 lit. b Ziff. 3"


class keine_schweren_wiederholten_widerhandlungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Keine schweren und wiederholten Widerhandlungen in den letzten zehn Jahren (alle Kategorien)"
    reference = "SR 744.10 Art. 5 Abs. 1 lit. b"

    def formula(person, period, parameters):
        keine_widerhandlung_entlohnung = (
            person('schwere_wiederholte_widerhandlungen_entlohnung_arbeitsbedingungen', period) == False
        )
        keine_widerhandlung_verkehr = (
            person('schwere_wiederholte_widerhandlungen_strassenverkehrssicherheit', period) == False
        )
        keine_widerhandlung_fahrzeug = (
            person('schwere_wiederholte_widerhandlungen_fahrzeugbau_ausruestung', period) == False
        )
        return keine_widerhandlung_entlohnung * keine_widerhandlung_verkehr * keine_widerhandlung_fahrzeug


class keine_sonstigen_zuverlaessigkeitszweifel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Keine anderen Gründe, die ernsthafte Zweifel an der Zuverlässigkeit wecken"
    reference = "SR 744.10 Art. 5 Abs. 2"


class zuverlaessigkeit_berufskraftfahrer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person gilt als zuverlässig im Sinne von SR 744.10 Art. 5 (Strassentransportgesetz)"
    reference = "SR 744.10 Art. 5"

    def formula(person, period, parameters):
        keine_verbrechensverurteilung = person('keine_verbrechensverurteilung_letzte_10_jahre', period)
        keine_widerhandlungen = person('keine_schweren_wiederholten_widerhandlungen', period)
        keine_zweifel = person('keine_sonstigen_zuverlaessigkeitszweifel', period)
        return keine_verbrechensverurteilung * keine_widerhandlungen * keine_zweifel
