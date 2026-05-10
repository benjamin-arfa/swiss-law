"""SR 235.1 Art. 10a

Generated from: ch/235/de/235.1.md

Datenbearbeitung durch Dritte: Bedingungen fuer die Uebertragung
der Datenbearbeitung an Dritte.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_dritter_bearbeitet_wie_auftraggeber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Dritter bearbeitet Daten nur so, wie der Auftraggeber es selbst duerfte"
    reference = "SR 235.1 Art. 10a Abs. 1 lit. a"


class dsg_keine_geheimhaltungspflicht_verbietet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Keine gesetzliche/vertragliche Geheimhaltungspflicht verbietet die Uebertragung"
    reference = "SR 235.1 Art. 10a Abs. 1 lit. b"


class dsg_dritter_datensicherheit_gewaehrleistet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auftraggeber hat sich vergewissert, dass Dritter Datensicherheit gewaehrleistet"
    reference = "SR 235.1 Art. 10a Abs. 2"


class dsg_datenbearbeitung_durch_dritte_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Uebertragung der Datenbearbeitung an Dritte ist zulaessig"
    reference = "SR 235.1 Art. 10a"

    def formula(person, period, parameters):
        wie_auftraggeber = person('dsg_dritter_bearbeitet_wie_auftraggeber', period)
        keine_geheimhaltung = person('dsg_keine_geheimhaltungspflicht_verbietet', period)
        sicherheit = person('dsg_dritter_datensicherheit_gewaehrleistet', period)
        return wie_auftraggeber * keine_geheimhaltung * sicherheit
