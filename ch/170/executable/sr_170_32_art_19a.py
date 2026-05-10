"""SR 170.32 Art. 19a

Generated from: ch/170/de/170.32.md

Haftung des Bundes für Schäden beim Betrieb von Schengen/Dublin-
Informationssystemen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schaden_durch_schengen_dublin_system(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schaden wurde beim Betrieb/Nutzung eines Schengen/Dublin-Informationssystems zugefügt (Art. 19a Abs. 1 VG)"
    reference = "SR 170.32, Art. 19a Abs. 1"


class person_im_dienste_des_kantons(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die schadensverursachende Person steht im Dienste eines Kantons (Art. 19a Abs. 2 VG)"
    reference = "SR 170.32, Art. 19a Abs. 2"


class bund_haftet_schengen_dublin(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund haftet für den Schengen/Dublin-Schaden (Art. 19a Abs. 1 VG)"
    reference = "SR 170.32, Art. 19a Abs. 1"

    def formula(person, period, parameters):
        return person('schaden_durch_schengen_dublin_system', period)


class bund_hat_rueckgriff_auf_kanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Dem Bund steht der Rückgriff auf den Kanton zu (Art. 19a Abs. 2 VG)"
    reference = "SR 170.32, Art. 19a Abs. 2"

    def formula(person, period, parameters):
        schengen = person('schaden_durch_schengen_dublin_system', period)
        bund_geleistet = person('bund_hat_ersatz_geleistet', period)
        kanton = person('person_im_dienste_des_kantons', period)
        return schengen * bund_geleistet * kanton
