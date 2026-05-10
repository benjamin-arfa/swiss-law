"""SR 744.103 Art. 14a

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zulassungsbewilligung_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Zulassungsbewilligung ist noch gültig"
    reference = "SR 744.103 Art. 14a lit. a"

    def formula(person, period, parameters):
        return person('zulassungsbewilligung_gueltig_raw', period)


class daten_benoetigt_fuer_zulassung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "BAV benötigt die Daten noch für die Erteilung oder Überprüfung der Zulassungsbewilligung"
    reference = "SR 744.103 Art. 14a lit. b"

    def formula(person, period, parameters):
        return person('daten_benoetigt_fuer_zulassung_raw', period)


class bav_loescht_daten_nach_stug_art9(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "BAV löscht die Daten nach Art. 9 STUG"
    reference = "SR 744.103 Art. 14a"

    def formula(person, period, parameters):
        bewilligung_gueltig = person('zulassungsbewilligung_gueltig', period)
        daten_benoetigt = person('daten_benoetigt_fuer_zulassung', period)

        # Löschpflicht tritt ein wenn:
        # a. Zulassungsbewilligung nicht mehr gültig, oder
        # b. Daten nicht mehr für Zwecke der Erteilung/Überprüfung benötigt
        return not_(bewilligung_gueltig) + not_(daten_benoetigt)
