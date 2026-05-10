"""SR 744.103 Art. 5

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class has_verkehrsleiter_anstellung_oder_auftrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen hat Verkehrsleiter/in im Anstellungs- oder Auftragsverhältnis"
    reference = "SR 744.103 Art. 5 (Einleitungssatz)"

    def formula(person, period, parameters):
        return person('verkehrsleiter_anstellungsverhaeltnis', period) + person('verkehrsleiter_auftragsverhaeltnis', period)


class verkehrsleiter_anstellungsverhaeltnis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter/in steht im Anstellungsverhältnis zum Unternehmen"
    reference = "SR 744.103 Art. 5 (Einleitungssatz)"


class verkehrsleiter_auftragsverhaeltnis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter/in steht im Auftragsverhältnis zum Unternehmen"
    reference = "SR 744.103 Art. 5 (Einleitungssatz)"


class bestaetigung_verkehrsleiter_verhaeltnis_eingereicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bestätigung des Anstellungs- oder Auftragsverhältnisses des Verkehrsleiters/der Verkehrsleiterin eingereicht"
    reference = "SR 744.103 Art. 5 Bst. a"

    def formula(person, period, parameters):
        hat_verhaeltnis = person('has_verkehrsleiter_anstellung_oder_auftrag', period)
        return hat_verhaeltnis * person('bestaetigung_verkehrsleiter_vorhanden', period)


class bestaetigung_verkehrsleiter_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bestätigungsdokument über Verhältnis Verkehrsleiter/in vorhanden"
    reference = "SR 744.103 Art. 5 Bst. a"


class vereinbarung_aufgaben_verkehrsleiter_eingereicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vereinbarung über Aufgaben und Verantwortlichkeiten des Verkehrsleiters/der Verkehrsleiterin eingereicht"
    reference = "SR 744.103 Art. 5 Bst. b"

    def formula(person, period, parameters):
        hat_verhaeltnis = person('has_verkehrsleiter_anstellung_oder_auftrag', period)
        return hat_verhaeltnis * person('vereinbarung_aufgaben_verkehrsleiter_vorhanden', period)


class vereinbarung_aufgaben_verkehrsleiter_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vereinbarungsdokument über Aufgaben und Verantwortlichkeiten des Verkehrsleiters/der Verkehrsleiterin vorhanden"
    reference = "SR 744.103 Art. 5 Bst. b"


class verzeichnis_weitere_unternehmen_eingereicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verzeichnis weiterer Strassentransportunternehmen des Verkehrsleiters/der Verkehrsleiterin eingereicht"
    reference = "SR 744.103 Art. 5 Bst. c"

    def formula(person, period, parameters):
        hat_verhaeltnis = person('has_verkehrsleiter_anstellung_oder_auftrag', period)
        return hat_verhaeltnis * person('verzeichnis_weitere_unternehmen_vorhanden', period)


class verzeichnis_weitere_unternehmen_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verzeichnisdokument weiterer Strassentransportunternehmen des Verkehrsleiters/der Verkehrsleiterin vorhanden"
    reference = "SR 744.103 Art. 5 Bst. c"


class besondere_nachweise_verkehrsleiter_vollstaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle besonderen Nachweise für Verkehrsleiter/in gemäss Art. 5 vollständig eingereicht"
    reference = "SR 744.103 Art. 5"

    def formula(person, period, parameters):
        hat_verhaeltnis = person('has_verkehrsleiter_anstellung_oder_auftrag', period)
        bestaetigung = person('bestaetigung_verkehrsleiter_verhaeltnis_eingereicht', period)
        vereinbarung = person('vereinbarung_aufgaben_verkehrsleiter_eingereicht', period)
        verzeichnis = person('verzeichnis_weitere_unternehmen_eingereicht', period)
        return not_(hat_verhaeltnis) + (bestaetigung * vereinbarung * verzeichnis)
