"""SR 614.0 Art. 8

Generated from: ch/614/de/614.0.md

Art. 8: Bereich der Aufsicht - Definiert, welche Stellen der Finanzaufsicht
durch die EFK unterstellt sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_zentrale_bundesverwaltung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verwaltungseinheit der zentralen oder dezentralen Bundesverwaltung (Art. 8 Abs. 1 lit. a)"
    reference = "SR 614.0 Art. 8 Abs. 1 lit. a"


class ist_parlamentsdienste(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Parlamentsdienste (Art. 8 Abs. 1 lit. b)"
    reference = "SR 614.0 Art. 8 Abs. 1 lit. b"


class ist_empfaenger_abgeltungen_finanzhilfen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Empfänger von Abgeltungen und Finanzhilfen (Art. 8 Abs. 1 lit. c)"
    reference = "SR 614.0 Art. 8 Abs. 1 lit. c"


class ist_organisation_mit_oeffentlicher_aufgabe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Körperschaft, Anstalt oder Organisation, der vom Bund die Erfüllung "
        "öffentlicher Aufgaben übertragen wurde (Art. 8 Abs. 1 lit. d)"
    )
    reference = "SR 614.0 Art. 8 Abs. 1 lit. d"


class bund_beteiligung_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bundesbeteiligung am Stamm-, Grund- oder Aktienkapital in Prozent"
    reference = "SR 614.0 Art. 8 Abs. 1 lit. e"


class ist_unternehmung_mit_bundesbeteiligung_ueber_50(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Unternehmung, an deren Kapital der Bund mit mehr als 50 Prozent "
        "beteiligt ist (Art. 8 Abs. 1 lit. e)"
    )
    reference = "SR 614.0 Art. 8 Abs. 1 lit. e"

    def formula(person, period, parameters):
        beteiligung = person('bund_beteiligung_prozent', period)
        return beteiligung > 50


class untersteht_efk_finanzaufsicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Untersteht der Finanzaufsicht durch die EFK (Art. 8 Abs. 1)"
    reference = "SR 614.0 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        # Art. 8 Abs. 1: Unter Vorbehalt der Sonderregelungen nach Art. 19
        zentrale_bv = person('ist_zentrale_bundesverwaltung', period)
        parlamentsdienste = person('ist_parlamentsdienste', period)
        empfaenger = person('ist_empfaenger_abgeltungen_finanzhilfen', period)
        oeffentliche_aufgabe = person('ist_organisation_mit_oeffentlicher_aufgabe', period)
        bundesbeteiligung = person('ist_unternehmung_mit_bundesbeteiligung_ueber_50', period)
        sonderregelung = person('hat_sonderregelung_art_19', period)
        return (
            (zentrale_bv + parlamentsdienste + empfaenger +
             oeffentliche_aufgabe + bundesbeteiligung)
            * (1 - sonderregelung)
        )


class hat_sonderregelung_art_19(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat eine Sonderregelung nach Art. 19 FKG (nicht der EFK unterstellt)"
    reference = "SR 614.0 Art. 19"
