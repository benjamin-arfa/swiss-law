"""SR 744.103 Art. 12

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_verkehrsleiter_in(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Verkehrsleiter oder Verkehrsleiterin eines Strassentransportunternehmens"
    reference = "SR 744.103 Art. 12"

    def formula(person, period, parameters):
        return person('im_bav_register_eingetragen', period)


class im_bav_register_eingetragen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist im Register der Strassentransportunternehmen des BAV eingetragen"
    reference = "SR 744.103 Art. 12"

    def formula(person, period, parameters):
        hat_name = person('bav_name_erfasst', period)
        hat_vorname = person('bav_vorname_erfasst', period)
        hat_geburtsdatum = person('bav_geburtsdatum_erfasst', period)
        hat_heimat_oder_geburtsort = person('bav_heimat_oder_geburtsort_erfasst', period)
        hat_adresse = person('bav_adresse_erfasst', period)
        return hat_name * hat_vorname * hat_geburtsdatum * hat_heimat_oder_geburtsort * hat_adresse


class bav_name_erfasst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Name der Verkehrsleiterin / des Verkehrsleiters im BAV-Register erfasst"
    reference = "SR 744.103 Art. 12"


class bav_vorname_erfasst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorname der Verkehrsleiterin / des Verkehrsleiters im BAV-Register erfasst"
    reference = "SR 744.103 Art. 12"


class bav_geburtsdatum_erfasst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geburtsdatum der Verkehrsleiterin / des Verkehrsleiters im BAV-Register erfasst"
    reference = "SR 744.103 Art. 12"


class bav_heimat_oder_geburtsort_erfasst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Heimat- oder Geburtsort der Verkehrsleiterin / des Verkehrsleiters im BAV-Register erfasst"
    reference = "SR 744.103 Art. 12"


class bav_adresse_erfasst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Adresse der Verkehrsleiterin / des Verkehrsleiters im BAV-Register erfasst"
    reference = "SR 744.103 Art. 12"
