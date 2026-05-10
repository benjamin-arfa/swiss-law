"""SR 446.21 Art. 21

Generated from: ch/446/de/446.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_nicht_gewinnorientiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist nicht gewinnorientiert"
    reference = "SR 446.21 Art. 21 Abs. 1"


class aktivitaet_ist_ueberregional(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aktivitaet ist ueberregional"
    reference = "SR 446.21 Art. 21 Abs. 2"


class anzahl_fr_kantone_aktivitaet(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl franzoesischsprachige Kantone in denen Aktivitaet durchgefuehrt wird"
    reference = "SR 446.21 Art. 21 Abs. 2"


class anzahl_de_kantone_aktivitaet(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl deutschsprachige Kantone in denen Aktivitaet durchgefuehrt wird"
    reference = "SR 446.21 Art. 21 Abs. 2"


class aktivitaet_in_it_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aktivitaet wird in der italienischsprachigen Schweiz durchgefuehrt"
    reference = "SR 446.21 Art. 21 Abs. 2"


class aktivitaet_in_rm_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aktivitaet wird in der raetoromanischen Schweiz durchgefuehrt"
    reference = "SR 446.21 Art. 21 Abs. 2"


class ist_ueberregional_jsfvv(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aktivitaet gilt als ueberregional nach JSFVV Art. 21 Abs. 2"
    reference = "SR 446.21 Art. 21 Abs. 2"

    def formula(person, period, parameters):
        fr = person('anzahl_fr_kantone_aktivitaet', period) >= 2
        de = person('anzahl_de_kantone_aktivitaet', period) >= 3
        it = person('aktivitaet_in_it_schweiz', period)
        rm = person('aktivitaet_in_rm_schweiz', period)
        return (fr + de + it + rm) >= 1


class ist_modellprojekt_jsfvv(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Qualifiziert als Modellprojekt nach JSFVV Art. 21 Abs. 3"
    reference = "SR 446.21 Art. 21 Abs. 3"


class modellprojekt_oertlich_uebertragbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Modellprojekt ist oertlich uebertragbar und verwaltungsunabhaengig"
    reference = "SR 446.21 Art. 21 Abs. 3 Bst. a"


class modellprojekt_neue_formen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Modellprojekt entwickelt neue Formen der Medienkompetenzfoerderung"
    reference = "SR 446.21 Art. 21 Abs. 3 Bst. b"


class modellprojekt_kontextuebertragbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Modellprojekt ist auf andere Kontexte uebertragbar"
    reference = "SR 446.21 Art. 21 Abs. 3 Bst. c"


class modellprojekt_beduerfnis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Modellprojekt entspricht einem nachgewiesenen Beduerfnis"
    reference = "SR 446.21 Art. 21 Abs. 3 Bst. d"


class modellprojekt_wissenstransfer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Modellprojekt stellt Wissenstransfer sicher"
    reference = "SR 446.21 Art. 21 Abs. 3 Bst. e"


class erfuellt_modellprojekt_kriterien_jsfvv(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfuellt alle Modellprojekt-Kriterien nach JSFVV Art. 21 Abs. 3"
    reference = "SR 446.21 Art. 21 Abs. 3"

    def formula(person, period, parameters):
        uebertragbar = person('modellprojekt_oertlich_uebertragbar', period)
        neue_formen = person('modellprojekt_neue_formen', period)
        kontext = person('modellprojekt_kontextuebertragbar', period)
        beduerfnis = person('modellprojekt_beduerfnis', period)
        wissenstransfer = person('modellprojekt_wissenstransfer', period)
        return uebertragbar * neue_formen * kontext * beduerfnis * wissenstransfer
