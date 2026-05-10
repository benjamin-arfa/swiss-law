"""SR 170.32 Art. 20

Generated from: ch/170/de/170.32.md

Verjährung der Ansprüche gegen den Bund.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class datum_schadensereignis(Variable):
    value_type = date
    entity = Person
    definition_period = YEAR
    label = "Datum des Schadensereignisses"
    reference = "SR 170.32, Art. 20 Abs. 1"


class datum_geltendmachung_efd(Variable):
    value_type = date
    entity = Person
    definition_period = YEAR
    label = "Datum der schriftlichen Geltendmachung beim EFD (Art. 20 Abs. 2 VG)"
    reference = "SR 170.32, Art. 20 Abs. 2"


class verjehrung_unterbrochen_durch_efd(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verjährung wurde durch schriftliche Geltendmachung beim EFD unterbrochen (Art. 20 Abs. 2 VG)"
    reference = "SR 170.32, Art. 20 Abs. 2"

    def formula(person, period, parameters):
        datum = person('datum_geltendmachung_efd', period)
        # Verjährung wird durch schriftliche Geltendmachung unterbrochen
        return datum > 0


class klagefrist_art_10_abs_2_verstrichen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "6-monatige Klagefrist nach Art. 10 Abs. 2 ist verstrichen (Art. 20 Abs. 3 VG)"
    reference = "SR 170.32, Art. 20 Abs. 3"
