"""SR 446.11 Art. 8

Generated from: ch/446/de/446.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class projekt_hat_innovative_aspekte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Projekt enthaelt innovative Aspekte"
    reference = "SR 446.11 Art. 8 Abs. 1 Bst. a"


class projekt_ist_uebertragbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Projekt ist auf andere Kontexte uebertragbar"
    reference = "SR 446.11 Art. 8 Abs. 1 Bst. b"


class projekt_beduerfnis_nachgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beduerfnis fuer das Projekt ist nachgewiesen"
    reference = "SR 446.11 Art. 8 Abs. 1 Bst. c"


class projekt_wissenstransfer_sichergestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wissenstransfer des Projekts ist sichergestellt"
    reference = "SR 446.11 Art. 8 Abs. 1 Bst. d"


class projekt_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer des Projekts in Jahren"
    reference = "SR 446.11 Art. 8 Abs. 1"


class projekt_ist_einmalig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Projekt ist einmalig (nicht wiederkehrend)"
    reference = "SR 446.11 Art. 8 Abs. 1"


class ist_modellvorhaben_kjfv(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Qualifiziert als Modellvorhaben nach Art. 8 KJFG"
    reference = "SR 446.11 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        einmalig = person('projekt_ist_einmalig', period)
        dauer = person('projekt_dauer_jahre', period)
        innovativ = person('projekt_hat_innovative_aspekte', period)
        uebertragbar = person('projekt_ist_uebertragbar', period)
        beduerfnis = person('projekt_beduerfnis_nachgewiesen', period)
        wissenstransfer = person('projekt_wissenstransfer_sichergestellt', period)
        return einmalig * (dauer <= 3) * innovativ * uebertragbar * beduerfnis * wissenstransfer


class projekt_massgeblich_von_kindern_erarbeitet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Projekt wird massgeblich von Kindern oder Jugendlichen erarbeitet, geleitet und umgesetzt"
    reference = "SR 446.11 Art. 8 Abs. 2 Bst. a"


class kinder_mit_foerderungsbedarf_zentrale_rolle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kinder oder Jugendliche mit besonderem Foerderungsbedarf nehmen zentrale und aktive Rolle ein"
    reference = "SR 446.11 Art. 8 Abs. 2 Bst. b"


class ist_partizipationsprojekt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Qualifiziert als Partizipationsprojekt"
    reference = "SR 446.11 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        einmalig = person('projekt_ist_einmalig', period)
        dauer = person('projekt_dauer_jahre', period)
        von_kindern = person('projekt_massgeblich_von_kindern_erarbeitet', period)
        foerderungsbedarf = person('kinder_mit_foerderungsbedarf_zentrale_rolle', period)
        return einmalig * (dauer <= 3) * (von_kindern + foerderungsbedarf >= 1)
