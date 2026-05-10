"""SR 744.10 Art. 9

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strassentransportunternehmen_im_register(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen ist im Register der Strassentransportunternehmen eingetragen (Art. 9 Abs. 1)"
    reference = "SR 744.10 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        # BAV führt Register zur Beurteilung der Zuverlässigkeit
        # und zur Überprüfung der Einhaltung der Zulassungsvorschriften
        zulassung_vorhanden = person('zulassungsbewilligung_strassentransport', period)
        return zulassung_vorhanden


class zulassungsbewilligung_strassentransport(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen verfügt über eine Zulassungsbewilligung für den Strassentransport"
    reference = "SR 744.10 Art. 9 Abs. 1"


class register_oeffentlicher_teil_name_und_sitz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Name und Sitz des Unternehmens im öffentlichen Registerteil enthalten (Art. 9 Abs. 2 Bst. a)"
    reference = "SR 744.10 Art. 9 Abs. 2 Bst. a"

    def formula(person, period, parameters):
        return person('strassentransportunternehmen_im_register', period)


class register_oeffentlicher_teil_bewilligungsart(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Art der Zulassungsbewilligung im öffentlichen Registerteil enthalten (Art. 9 Abs. 2 Bst. b)"
    reference = "SR 744.10 Art. 9 Abs. 2 Bst. b"

    def formula(person, period, parameters):
        return person('strassentransportunternehmen_im_register', period)


class register_oeffentlicher_teil_verkehrsleiter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Name des Verkehrsleiters im öffentlichen Registerteil enthalten (Art. 9 Abs. 2 Bst. c)"
    reference = "SR 744.10 Art. 9 Abs. 2 Bst. c"

    def formula(person, period, parameters):
        return person('strassentransportunternehmen_im_register', period)


class register_oeffentlicher_teil_fahrzeugzahl(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zahl der Fahrzeuge im öffentlichen Registerteil enthalten (Art. 9 Abs. 2 Bst. d)"
    reference = "SR 744.10 Art. 9 Abs. 2 Bst. d"

    def formula(person, period, parameters):
        return person('strassentransportunternehmen_im_register', period)


class register_nicht_oeffentlicher_teil_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eintrag im nicht öffentlichen Registerteil zulässig (Art. 9 Abs. 3)"
    reference = "SR 744.10 Art. 9 Abs. 3"

    def formula(person, period, parameters):
        # Nicht öffentlicher Teil enthält Daten gemäss Abs. 3 Bst. a–e
        identifikationsdaten = person('register_identifikationsdaten_zuverlässigkeit', period)
        sanktionsdaten = person('register_verwaltungs_oder_strafrechtliche_sanktionen', period)
        zweifelsgründe = person('register_ernsthafte_zweifel_zuverlaessigkeit', period)
        zuverlaessigkeit_versagt = person('register_zuverlaessigkeit_nicht_mehr_erfuellt', period)
        bewilligung_entzogen = person('register_bewilligung_entzogen_oder_widerrufen', period)
        return (
            identifikationsdaten
            + sanktionsdaten
            + zweifelsgründe
            + zuverlaessigkeit_versagt
            + bewilligung_entzogen
        )


class register_identifikationsdaten_zuverlässigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Identifikationsdaten der Personen, die Zuverlässigkeit erfüllen müssen, im Register (Art. 9 Abs. 3 Bst. a)"
    reference = "SR 744.10 Art. 9 Abs. 3 Bst. a"


class register_verwaltungs_oder_strafrechtliche_sanktionen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten über verwaltungs- oder strafrechtliche Verfolgungen/Sanktionen nach Art. 5 Abs. 1 Bst. a oder b im Register (Art. 9 Abs. 3 Bst. b)"
    reference = "SR 744.10 Art. 9 Abs. 3 Bst. b"


class register_ernsthafte_zweifel_zuverlaessigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gründe für ernsthafte Zweifel an der Zuverlässigkeit im Register (Art. 9 Abs. 3 Bst. c)"
    reference = "SR 744.10 Art. 9 Abs. 3 Bst. c"


class register_zuverlaessigkeit_nicht_mehr_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Feststellung nach Prüfung (Art. 8 Abs. 1), dass Zuverlässigkeit nicht mehr erfüllt ist, im Register (Art. 9 Abs. 3 Bst. d)"
    reference = "SR 744.10 Art. 9 Abs. 3 Bst. d"


class register_bewilligung_entzogen_oder_widerrufen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entzug oder Widerruf der Zulassungsbewilligung im Register (Art. 9 Abs. 3 Bst. e)"
    reference = "SR 744.10 Art. 9 Abs. 3 Bst. e"


class register_daten_nach_zehn_jahren_vernichtet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Registerdaten sind nach zehn Jahren zu vernichten (Art. 9 Abs. 4)"
    reference = "SR 744.10 Art. 9 Abs. 4"

    def formula(person, period, parameters):
        # BAV vernichtet Daten nach zehn Jahren
        jahre_seit_eintragung = person('jahre_seit_registereintragung', period)
        return jahre_seit_eintragung >= 10


class jahre_seit_registereintragung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre seit der Eintragung ins Register der Strassentransportunternehmen"
    reference = "SR 744.10 Art. 9 Abs. 4"
