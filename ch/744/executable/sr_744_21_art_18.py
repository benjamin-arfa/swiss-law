"""SR 744.21 Art. 18

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strassenverkehrsgesetz_strafbestimmungen_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strafbestimmungen des BG vom 19. Dezember 1958 über den Strassenverkehr (SR 741.01) finden Anwendung, mit Ausnahme derjenigen über das Fahren ohne Fahrzeugausweis und über das Kontrollschild"
    reference = "SR 744.21 Art. 18 Abs. 1"

    def formula(person, period, parameters):
        fahren_ohne_fahrzeugausweis = person('fahren_ohne_fahrzeugausweis', period)
        kontrollschild_vergehen = person('kontrollschild_vergehen', period)
        unterliegt_sr_744_21 = person('unterliegt_sr_744_21', period)
        return unterliegt_sr_744_21 * not_(fahren_ohne_fahrzeugausweis) * not_(kontrollschild_vergehen)


class fahren_ohne_fahrzeugausweis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vergehen: Fahren ohne Fahrzeugausweis"
    reference = "SR 744.21 Art. 18 Abs. 1"


class kontrollschild_vergehen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vergehen betreffend das Kontrollschild"
    reference = "SR 744.21 Art. 18 Abs. 1"


class unterliegt_sr_744_21(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person unterliegt dem Anwendungsbereich von SR 744.21"
    reference = "SR 744.21 Art. 18 Abs. 1"


class eisenbahngesetz_dienstunfahigkeit_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bestimmungen des Eisenbahngesetzes vom 20. Dezember 1957 (SR 742.101) über die Dienstunfähigkeit gelten sinngemäss"
    reference = "SR 744.21 Art. 18 Abs. 2"

    def formula(person, period, parameters):
        return person('unterliegt_sr_744_21', period)
