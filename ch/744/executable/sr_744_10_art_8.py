"""SR 744.10 Art. 8

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zulassungsvoraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strassentransportunternehmen erfüllt die Zulassungsvoraussetzungen"
    reference = "SR 744.10 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return person('zulassungsbewilligung_inhaber', period)


class pruefung_faellig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Regelmässige Prüfung der Zulassungsvoraussetzungen fällig (mindestens alle 5 Jahre)"
    reference = "SR 744.10 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        jahre_seit_letzter_pruefung = person('jahre_seit_letzter_pruefung', period)
        return jahre_seit_letzter_pruefung >= 5


class jahre_seit_letzter_pruefung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahre seit der letzten Prüfung der Zulassungsvoraussetzungen durch das BAV"
    reference = "SR 744.10 Art. 8 Abs. 1"


class konkrete_anhaltspunkte_nichterfuellung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konkrete Anhaltspunkte dafür, dass Zulassungsvoraussetzungen nicht mehr erfüllt sind"
    reference = "SR 744.10 Art. 8 Abs. 1bis"


class nachweis_frist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist in Monaten für den Nachweis der Zulassungsvoraussetzungen (Regelfrist: 6 Monate)"
    reference = "SR 744.10 Art. 8 Abs. 1bis"

    def formula(person, period, parameters):
        hat_anhaltspunkte = person('konkrete_anhaltspunkte_nichterfuellung', period)
        verlaengerung = person('frist_verlaengerung_verkehrsleiter', period)
        basis_frist = where(hat_anhaltspunkte, 6, 0)
        return basis_frist + verlaengerung


class frist_verlaengerung_verkehrsleiter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Fristverlängerung in Monaten bei Ersatz des Verkehrsleiters infolge Tod oder Krankheit (max. 3 Monate)"
    reference = "SR 744.10 Art. 8 Abs. 1bis"

    def formula(person, period, parameters):
        ersatz_notwendig = person('verkehrsleiter_ersatz_tod_krankheit', period)
        beantragte_verlaengerung = person('beantragte_verlaengerung_monate', period)
        return where(ersatz_notwendig, min_(beantragte_verlaengerung, 3), 0)


class verkehrsleiter_ersatz_tod_krankheit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter muss infolge Todes oder Krankheit ersetzt werden"
    reference = "SR 744.10 Art. 8 Abs. 1bis"


class beantragte_verlaengerung_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Beantragte Fristverlängerung in Monaten"
    reference = "SR 744.10 Art. 8 Abs. 1bis"


class wiederherstellung_vorschriftsmaessiger_zustand(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen hat den vorschriftsmässigen Zustand innerhalb der gesetzten Frist wiederhergestellt"
    reference = "SR 744.10 Art. 8 Abs. 1bis"


class wiederholter_oder_schwerwiegender_verstoss(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen hat wiederholt oder schwerwiegend gegen Strassenverkehrsbestimmungen verstossen"
    reference = "SR 744.10 Art. 8 Abs. 2"


class zulassungsbewilligung_entzug_oder_widerruf(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV entzieht oder widerruft die Zulassungsbewilligung entschädigungslos"
    reference = "SR 744.10 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        voraussetzung_nicht_mehr_erfuellt = not_(person('zulassungsvoraussetzungen_erfuellt', period))
        kein_nachweis_und_keine_wiederherstellung = (
            person('konkrete_anhaltspunkte_nichterfuellung', period)
            * not_(person('wiederherstellung_vorschriftsmaessiger_zustand', period))
        )
        schwerwiegender_verstoss = person('wiederholter_oder_schwerwiegender_verstoss', period)
        return (
            voraussetzung_nicht_mehr_erfuellt
            + kein_nachweis_und_keine_wiederherstellung
            + schwerwiegender_verstoss
        )


class zulassungsbewilligung_inhaber(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Inhaber einer Zulassungsbewilligung als Strassentransportunternehmen"
    reference = "SR 744.10 Art. 8"
