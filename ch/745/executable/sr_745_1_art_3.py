"""SR 745.1 Art. 3

Generated from: ch/745/de/745.1.md

Erschliessungsfunktion der Personenbefoerderung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class personenbefoerderung_erschliessungsfunktion(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Personenbefoerderung hat Erschliessungsfunktion (erschliesst ganzjaehrig bewohnte Ortschaften)"
    reference = "SR 745.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        # Art. 3 Abs. 1: Erschliessungsfunktion liegt vor, wenn die
        # regelmaessige und gewerbsmaessige Personenbefoerderung
        # ganzjaehrig bewohnte Ortschaften erschliesst.
        ist_regelmaessig = person('personenbefoerderung_regelmaessig', period)
        ist_gewerbsmaessig = person('personenbefoerderung_gewerbsmaessig', period)
        erschliesst_ortschaft = person('erschliesst_ganzjaehrig_bewohnte_ortschaft', period)
        return ist_regelmaessig * ist_gewerbsmaessig * erschliesst_ortschaft


class erschliesst_ganzjaehrig_bewohnte_ortschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befoerderungsangebot erschliesst eine ganzjaehrig bewohnte Ortschaft"
    reference = "SR 745.1 Art. 3 Abs. 1"
