"""SR 235.1 Art. 13

Generated from: ch/235/de/235.1.md

Rechtfertigungsgruende: Einwilligung, ueberwiegendes Interesse, Gesetz.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_einwilligung_des_verletzten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einwilligung des Verletzten liegt vor"
    reference = "SR 235.1 Art. 13 Abs. 1"


class dsg_ueberwiegendes_interesse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ueberwiegendes privates oder oeffentliches Interesse liegt vor"
    reference = "SR 235.1 Art. 13 Abs. 1"


class dsg_gesetzliche_rechtfertigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesetzliche Rechtfertigung fuer die Persoenlichkeitsverletzung"
    reference = "SR 235.1 Art. 13 Abs. 1"


class dsg_vertragszusammenhang_bearbeitung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bearbeitung im Zusammenhang mit Vertragsabschluss/-abwicklung"
    reference = "SR 235.1 Art. 13 Abs. 2 lit. a"


class dsg_wirtschaftlicher_wettbewerb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bearbeitung im wirtschaftlichen Wettbewerb ohne Bekanntgabe an Dritte"
    reference = "SR 235.1 Art. 13 Abs. 2 lit. b"


class dsg_kreditwuerdigkeitspruefung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Pruefung der Kreditwuerdigkeit ohne besonders schuetzenswerte Daten"
    reference = "SR 235.1 Art. 13 Abs. 2 lit. c"


class dsg_rechtfertigung_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Rechtfertigungsgrund nach Art. 13 DSG vorhanden"
    reference = "SR 235.1 Art. 13"

    def formula(person, period, parameters):
        einwilligung = person('dsg_einwilligung_des_verletzten', period)
        interesse = person('dsg_ueberwiegendes_interesse', period)
        gesetz = person('dsg_gesetzliche_rechtfertigung', period)
        return (einwilligung + interesse + gesetz) > 0
