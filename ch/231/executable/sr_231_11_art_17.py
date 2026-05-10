"""SR 231.11 Art. 17

Generated from: ch/231/de/231.11.md

Schutz von Computerprogrammen: Definiert den zulaessigen Gebrauch,
Schnittstelleninformationen und unzumutbare Beeintraechtigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_rechtmaessiger_erwerber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ein rechtmaessiger Erwerber des Computerprogramms ist"
    reference = "SR 231.11 Art. 17 Abs. 1"


class bestimmungsgemaesse_verwendung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Programm bestimmungsgemaess verwendet wird (Laden, Anzeigen, Ablaufen, Uebertragen, Speichern)"
    reference = "SR 231.11 Art. 17 Abs. 1 Bst. a"


class untersuchung_programmelement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Programm zum Zweck der Ermittlung zugrundeliegender Ideen untersucht wird"
    reference = "SR 231.11 Art. 17 Abs. 1 Bst. b"


class zulaessiger_gebrauch_computerprogramm(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Gebrauch des Computerprogramms nach Art. 12 Abs. 2 URG zulaessig ist"
    reference = "SR 231.11 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('ist_rechtmaessiger_erwerber', period)
            * (
                person('bestimmungsgemaesse_verwendung', period)
                + person('untersuchung_programmelement', period)
            )
        )


class schnittstelleninformation_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Schnittstelleninformationen fuer die Interoperabilitaet unerlässlich und nicht zugaenglich sind"
    reference = "SR 231.11 Art. 17 Abs. 2"


class aehnliche_ausdrucksform_verwendet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob gewonnene Schnittstelleninformationen fuer ein wesentlich aehnliches Programm verwendet werden"
    reference = "SR 231.11 Art. 17 Abs. 3"


class unzumutbare_beeintraechtigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine unzumutbare Beeintraechtigung der normalen Auswertung des Programms vorliegt"
    reference = "SR 231.11 Art. 17 Abs. 3"

    def formula(person, period, parameters):
        return person('aehnliche_ausdrucksform_verwendet', period)
