"""SR 364.3 Art. 2

Generated from: ch/364/de/364.3.md

Grundsatz: Polizeiorgane duerfen nur geprueft/empfohlene Zwangsmittel einsetzen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zwangsmittel_von_fachinstitution_geprueft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zwangsmittel wurde von einer Fachinstitution auf Einsatztauglichkeit geprueft und empfohlen"
    reference = "SR 364.3 Art. 2 Abs. 1"


class zwangsmittel_einsatz_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einsatz des Zwangsmittels bei polizeilichem Zwang ist zulaessig"
    reference = "SR 364.3 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return person('zwangsmittel_von_fachinstitution_geprueft', period)
