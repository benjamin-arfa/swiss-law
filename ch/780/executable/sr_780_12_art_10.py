"""SR 780.12 Art. 10

Generated from: ch/780/de/780.12.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class datensicherheit_zugriffsschutz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Sichere Authentifizierung und detaillierte Beschreibung der "
        "Lese- und Schreibrechte sind sichergestellt"
    )
    reference = "SR 780.12 Art. 10 Abs. 1 Bst. a"


class datensicherheit_transportkontrolle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesicherte Uebermittlung der Daten des Verarbeitungssystems ist sichergestellt"
    reference = "SR 780.12 Art. 10 Abs. 1 Bst. b"


class datensicherheit_zugriffskontrolle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Protokollierung aller Datenzugriffe und -aenderungen und "
        "regelmaessige stichprobenweise Auswertung sind sichergestellt"
    )
    reference = "SR 780.12 Art. 10 Abs. 1 Bst. c"


class datensicherheit_gewaehrleistet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Datensicherheitsmassnahmen gemaess Art. 10 sind gewaehrleistet"
    reference = "SR 780.12 Art. 10"

    def formula(person, period, parameters):
        zugriff = person('datensicherheit_zugriffsschutz', period)
        transport = person('datensicherheit_transportkontrolle', period)
        kontrolle = person('datensicherheit_zugriffskontrolle', period)
        return zugriff * transport * kontrolle
