"""SR 744.10 Art. 9a

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erfuellt_tatsaechlichen_und_dauerhaften_sitz_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strassentransportunternehmen erfüllt Voraussetzung des tatsächlichen und dauerhaften Sitzes in der Schweiz (SR 744.10 Art. 9a Abs. 1)"
    reference = "SR 744.10 Art. 9a Abs. 1"

    def formula(person, period, parameters):
        return person('tatsaechlicher_sitz_in_schweiz', period) * person('dauerhafter_sitz_in_schweiz', period)


class tatsaechlicher_sitz_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen hat tatsächlichen Sitz in der Schweiz"
    reference = "SR 744.10 Art. 9a Abs. 1"

    def formula(person, period, parameters):
        return person('sitz_schweiz', period)


class dauerhafter_sitz_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen hat dauerhaften Sitz in der Schweiz"
    reference = "SR 744.10 Art. 9a Abs. 1"

    def formula(person, period, parameters):
        return person('sitz_dauerhaft', period)


class amtshilfe_auskunft_bav_an_eu_mitgliedstaat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV erteilt auf Anfrage eines EU-Mitgliedstaats Auskunft über Sitzvoraussetzung (SR 744.10 Art. 9a Abs. 1)"
    reference = "SR 744.10 Art. 9a Abs. 1"

    def formula(person, period, parameters):
        anfrage_eu = person('anfrage_von_eu_mitgliedstaat', period)
        erfuellt_sitz = person('erfuellt_tatsaechlichen_und_dauerhaften_sitz_in_schweiz', period)
        return anfrage_eu * erfuellt_sitz


class amtshilfe_auskunft_bav_an_drittstaat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV erteilt auf Anfrage eines Drittstaats Auskunft über Sitzvoraussetzung (SR 744.10 Art. 9a Abs. 1)"
    reference = "SR 744.10 Art. 9a Abs. 1"

    def formula(person, period, parameters):
        anfrage_drittstaat = person('anfrage_von_drittstaat', period)
        erfuellt_sitz = person('erfuellt_tatsaechlichen_und_dauerhaften_sitz_in_schweiz', period)
        return anfrage_drittstaat * erfuellt_sitz


class informationsaustausch_ueber_eu_informationssystem(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Informationsaustausch mit EU-Mitgliedstaaten über EU-Informationssystem gemäss DVO (EU) 2016/480 (SR 744.10 Art. 9a Abs. 2)"
    reference = "SR 744.10 Art. 9a Abs. 2"

    def formula(person, period, parameters):
        ist_eu_mitgliedstaat = person('anfrage_von_eu_mitgliedstaat', period)
        return ist_eu_mitgliedstaat


class datenbekanntgabe_an_drittstaat_auf_anfrage(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV gibt Daten nach Art. 9 Abs. 2 und 3 lit. a, d, e an Drittstaat bekannt nach Massgabe anwendbarer Abkommen (SR 744.10 Art. 9a Abs. 4)"
    reference = "SR 744.10 Art. 9a Abs. 4"

    def formula(person, period, parameters):
        anfrage_drittstaat = person('anfrage_von_drittstaat', period)
        abkommen_anwendbar = person('voelkerrechtliches_abkommen_anwendbar', period)
        return anfrage_drittstaat * abkommen_anwendbar


class daten_im_abrufverfahren_zugaenglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV macht Daten im Abrufverfahren für Drittstaaten zugänglich (SR 744.10 Art. 9a Abs. 4)"
    reference = "SR 744.10 Art. 9a Abs. 4"

    def formula(person, period, parameters):
        datenbekanntgabe = person('datenbekanntgabe_an_drittstaat_auf_anfrage', period)
        abrufverfahren_erlaubt = person('abrufverfahren_durch_bav_erlaubt', period)
        return datenbekanntgabe * abrufverfahren_erlaubt


class anfrage_von_eu_mitgliedstaat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegt eine Anfrage eines zuständigen EU-Mitgliedstaats vor"
    reference = "SR 744.10 Art. 9a"


class anfrage_von_drittstaat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegt eine Anfrage eines Drittstaats vor"
    reference = "SR 744.10 Art. 9a"


class voelkerrechtliches_abkommen_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Im Einzelfall anwendbares völkerrechtliches Abkommen mit dem anfragenden Drittstaat besteht"
    reference = "SR 744.10 Art. 9a Abs. 4"


class sitz_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen hat Sitz in der Schweiz"
    reference = "SR 744.10 Art. 9a"


class sitz_dauerhaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sitz des Unternehmens ist dauerhaft"
    reference = "SR 744.10 Art. 9a"


class abrufverfahren_durch_bav_erlaubt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV hat Abrufverfahren für Datenzugang eingerichtet"
    reference = "SR 744.10 Art. 9a Abs. 4"
