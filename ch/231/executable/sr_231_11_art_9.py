"""SR 231.11 Art. 9

Generated from: ch/231/de/231.11.md

Antragstellung: Verwertungsgesellschaften muessen Tarifantraege
mindestens 7 Monate vor geplantem Inkrafttreten einreichen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tarif_inkrafttreten_datum(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Geplantes Inkrafttretendatum des neuen Tarifs"
    reference = "SR 231.11 Art. 9 Abs. 2"


class tarif_einreichung_datum(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum der Einreichung des Tarifantrags bei der Schiedskommission"
    reference = "SR 231.11 Art. 9 Abs. 2"


class mindestfrist_tarif_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestfrist fuer Tarifeinreichung in Monaten (7 Monate)"
    reference = "SR 231.11 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        return 7


class verhandlungen_einlaesslich_gefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verhandlungen mit den Nutzerverbaenden mit gebotener Einlaesslichkeit gefuehrt wurden"
    reference = "SR 231.11 Art. 9 Abs. 3"
