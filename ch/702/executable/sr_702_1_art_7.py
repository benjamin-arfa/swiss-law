"""SR 702.1 Art. 7

Generated from: ch/702/de/702.1.md

Umnutzung und Meldung: Change of use from tourist to primary dwelling
must be reported within 30 days.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nutzungsaenderung_meldefrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Meldefrist fuer Nutzungsaenderung in Tagen ab Bezug"
    reference = "SR 702.1 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        return 30  # innert 30 Tagen
