"""SR 143.13 Art. 3

Generated from: ch/143/de/143.13.md

Applications for Pass 2010: may be submitted from 24 February 2010.
Personal appearance for biometric data from 1 March 2010.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antrag_pass_2010_ab_datum(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Fruehestes Datum fuer Einreichung eines Antrags fuer Pass 2010"
    reference = "SR 143.13 Art. 3 Abs. 1"
    default_value = "2010-02-24"


class biometrische_erfassung_pass_2010_ab_datum(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Fruehestes Datum fuer persoenliche Vorsprache zur Erfassung biometrischer Daten fuer Pass 2010"
    reference = "SR 143.13 Art. 3 Abs. 2"
    default_value = "2010-03-01"
