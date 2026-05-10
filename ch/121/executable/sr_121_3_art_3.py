"""SR 121.3 Art. 3

Generated from: ch/121/de/121.3.md

Geschäftsordnung: AB-ND establishes its own rules of procedure and publishes them.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ab_nd_geschaeftsordnung_erstellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die AB-ND eine Geschaeftsordnung gibt"
    reference = "SR 121.3 Art. 3"


class ab_nd_geschaeftsordnung_veroeffentlicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Geschaeftsordnung der AB-ND veroeffentlicht wird"
    reference = "SR 121.3 Art. 3"

    def formula(person, period, parameters):
        return person('ab_nd_geschaeftsordnung_erstellt', period)


class ab_nd_geschaeftsordnung_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die AB-ND eine gueltige und veroeffentlichte Geschaeftsordnung hat"
    reference = "SR 121.3 Art. 3"

    def formula(person, period, parameters):
        erstellt = person('ab_nd_geschaeftsordnung_erstellt', period)
        veroeffentlicht = person('ab_nd_geschaeftsordnung_veroeffentlicht', period)
        return erstellt & veroeffentlicht
