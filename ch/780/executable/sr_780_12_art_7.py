"""SR 780.12 Art. 7

Generated from: ch/780/de/780.12.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class benutzerkonto_verarbeitungssystem_berechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Person hat ein persoenliches Benutzerkonto fuer den Zugriff "
        "auf das Verarbeitungssystem des Dienstes UePF"
    )
    reference = "SR 780.12 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        ist_behoerde = person('ist_mitarbeiter_behoerde_uepf', period)
        ist_mitwirkend = person('ist_mitarbeiter_mitwirkungspflichtige', period)
        ist_dienst = person('ist_mitarbeiter_dienst_uepf', period)
        ist_beauftragt = person('ist_beauftragte_person_uepf', period)
        aufgabe_erfordert = person('zugriff_zur_aufgabenerfuellung_notwendig', period)
        return (ist_behoerde + ist_mitwirkend + ist_dienst + ist_beauftragt) * aufgabe_erfordert


class ist_mitarbeiter_behoerde_uepf(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mitarbeiter/in einer Behoerde gemaess BUEPF"
    reference = "SR 780.12 Art. 7 Abs. 1 Bst. a"


class ist_mitarbeiter_mitwirkungspflichtige(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mitarbeiter/in einer mitwirkungspflichtigen Stelle"
    reference = "SR 780.12 Art. 7 Abs. 1 Bst. b"


class ist_mitarbeiter_dienst_uepf(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mitarbeiter/in des Dienstes UePF"
    reference = "SR 780.12 Art. 7 Abs. 1 Bst. c"


class ist_beauftragte_person_uepf(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vom Dienst UePF mit Wartungs-, Betriebs- oder Programmieraufgaben betraut"
    reference = "SR 780.12 Art. 7 Abs. 1 Bst. d"


class zugriff_zur_aufgabenerfuellung_notwendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zugriff auf das Verarbeitungssystem ist zur Erfuellung der Aufgaben notwendig"
    reference = "SR 780.12 Art. 7 Abs. 1"
