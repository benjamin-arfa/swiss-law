"""SR 362.2 Art. 12

Generated from: ch/362/de/362.2.md
Grounds for refusal of information exchange.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Fakultative Verweigerungsgruende (Abs. 1 - "kann verweigert werden")

class beeintraechtigt_nationale_sicherheit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Austausch koennte wesentliche nationale Sicherheitsinteressen beeintraechtigen"
    reference = "SR 362.2 Art. 12 Abs. 1 lit. a"


class gefaehrdet_ermittlungen_oder_sicherheit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Austausch koennte Erfolg laufender Ermittlungen oder Sicherheit von Personen gefaehrden"
    reference = "SR 362.2 Art. 12 Abs. 1 lit. b"


class informationen_nicht_sachdienlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Informationen erscheinen nicht sachdienlich oder erforderlich"
    reference = "SR 362.2 Art. 12 Abs. 1 lit. c"


class fakultative_verweigerung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Informationsaustausch kann verweigert werden (fakultativer Verweigerungsgrund)"
    reference = "SR 362.2 Art. 12 Abs. 1"

    def formula(person, period):
        sicherheit = person('beeintraechtigt_nationale_sicherheit', period)
        ermittlungen = person('gefaehrdet_ermittlungen_oder_sicherheit', period)
        nicht_sachdienlich = person('informationen_nicht_sachdienlich', period)
        return sicherheit + ermittlungen + nicht_sachdienlich


# Obligatorische Verweigerungsgruende (Abs. 2 - "ist zu verweigern")

class informationen_als_beweismittel_vor_gericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Informationen sollen als Beweismittel vor Justizbehoerde verwendet werden"
    reference = "SR 362.2 Art. 12 Abs. 2 lit. a"


class straftat_hoechststrafe_unter_1_jahr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Straftat ist mit Freiheitsstrafe von einem Jahr oder weniger bedroht"
    reference = "SR 362.2 Art. 12 Abs. 2 lit. b"


class justizbehoerde_verweigert_genehmigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Justizbehoerde hat Genehmigung des Zugangs/Austauschs verweigert"
    reference = "SR 362.2 Art. 12 Abs. 2 lit. c"


class obligatorische_verweigerung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Informationsaustausch muss verweigert werden (obligatorischer Verweigerungsgrund)"
    reference = "SR 362.2 Art. 12 Abs. 2"

    def formula(person, period):
        beweismittel = person('informationen_als_beweismittel_vor_gericht', period)
        unter_1_jahr = person('straftat_hoechststrafe_unter_1_jahr', period)
        verweigert = person('justizbehoerde_verweigert_genehmigung', period)
        return beweismittel + unter_1_jahr + verweigert


class informationsaustausch_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Informationsaustausch ist zulaessig (kein obligatorischer Verweigerungsgrund)"
    reference = "SR 362.2 Art. 12"

    def formula(person, period):
        obligatorisch = person('obligatorische_verweigerung', period)
        return not_(obligatorisch)
