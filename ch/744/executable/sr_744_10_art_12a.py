"""SR 744.10 Art. 12a

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zulassungsbewilligung_vor_inkrafttreten_2024(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person verfügte bei Inkrafttreten der Änderung vom 14. Juni 2024 über eine Zulassungsbewilligung"
    reference = "SR 744.10 Art. 12a Abs. 1"


class bewilligung_entzogen_oder_widerrufen_nach_neuem_recht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zulassungsbewilligung nach neuem Recht entzogen oder widerrufen"
    reference = "SR 744.10 Art. 12a Abs. 1"


class zulassungsbewilligung_bleibt_nach_altem_recht_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bestehende Zulassungsbewilligung bleibt nach bisherigem Recht gültig (Übergangsbestimmung zur Änderung vom 14. Juni 2024)"
    reference = "SR 744.10 Art. 12a Abs. 1"

    def formula(person, period, parameters):
        hat_bewilligung = person('zulassungsbewilligung_vor_inkrafttreten_2024', period)
        nicht_entzogen = ~person('bewilligung_entzogen_oder_widerrufen_nach_neuem_recht', period)
        return hat_bewilligung * nicht_entzogen


class ist_strassentransportunternehmen_art3_abs1bis_b(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strassentransportunternehmen gemäss Artikel 3 Absatz 1bis Buchstabe b"
    reference = "SR 744.10 Art. 12a Abs. 2"


class fahrzeug_gesamtgewicht_tonnen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtgewicht des Fahrzeugs nach Fahrzeugausweis (in Tonnen)"
    reference = "SR 744.10 Art. 12a Abs. 2"


class neue_zulassungsbewilligung_uebergangsrecht_2_5_bis_3_5_tonnen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf neue Zulassungsbewilligung für verbleibende Gültigkeitsdauer bei Fahrzeugen zwischen 2,5 und 3,5 Tonnen Gesamtgewicht (Übergangsbestimmung zur Änderung vom 14. Juni 2024)"
    reference = "SR 744.10 Art. 12a Abs. 2"

    def formula(person, period, parameters):
        ist_unternehmen_art3 = person('ist_strassentransportunternehmen_art3_abs1bis_b', period)
        hat_bewilligung_altes_recht = person('zulassungsbewilligung_vor_inkrafttreten_2024', period)
        gewicht = person('fahrzeug_gesamtgewicht_tonnen', period)
        gewicht_ueber_2_5 = gewicht > 2.5
        gewicht_hoechstens_3_5 = gewicht <= 3.5
        return (
            ist_unternehmen_art3
            * hat_bewilligung_altes_recht
            * gewicht_ueber_2_5
            * gewicht_hoechstens_3_5
        )


class abkommen_informationsaustausch_art9a_abs2_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Abkommen für den Informationsaustausch nach Artikel 9a Absatz 2 ist in Kraft getreten"
    reference = "SR 744.10 Art. 12a Abs. 3"


class bav_datenweitergabe_auf_anfrage_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV gibt Daten den zuständigen Behörden der EU-Mitgliedstaaten auf Anfrage bekannt (gilt bis Inkrafttreten der Abkommen nach Art. 9a Abs. 2)"
    reference = "SR 744.10 Art. 12a Abs. 3"

    def formula(person, period, parameters):
        abkommen_in_kraft = person('abkommen_informationsaustausch_art9a_abs2_in_kraft', period)
        return ~abkommen_in_kraft
