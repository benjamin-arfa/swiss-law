"""SR 170.32 Art. 6

Generated from: ch/170/de/170.32.md

Genugtuung bei Tötung, Körperverletzung oder Persönlichkeitsverletzung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beamter_hat_verschulden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Den Beamten trifft ein Verschulden (Art. 6 Abs. 1 VG)"
    reference = "SR 170.32, Art. 6 Abs. 1"


class persoenlichkeit_widerrechtlich_verletzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person wurde in ihrer Persönlichkeit widerrechtlich verletzt (Art. 6 Abs. 2 VG)"
    reference = "SR 170.32, Art. 6 Abs. 2"


class schwere_der_verletzung_rechtfertigt_genugtuung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schwere der Verletzung rechtfertigt eine Genugtuung (Art. 6 Abs. 2 VG)"
    reference = "SR 170.32, Art. 6 Abs. 2"


class verletzung_anderweitig_wiedergutgemacht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verletzung wurde anders wiedergutgemacht (Art. 6 Abs. 2 VG)"
    reference = "SR 170.32, Art. 6 Abs. 2"


class anspruch_genugtuung_toetung_koerperverletzung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf Genugtuung bei Tötung oder Körperverletzung (Art. 6 Abs. 1 VG)"
    reference = "SR 170.32, Art. 6 Abs. 1"

    def formula(person, period, parameters):
        toetung = person('toetung_eingetreten', period)
        verletzung = person('koerperverletzung_eingetreten', period)
        verschulden = person('beamter_hat_verschulden', period)
        return (toetung + verletzung > 0) * verschulden


class anspruch_genugtuung_persoenlichkeitsverletzung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf Genugtuung bei Persönlichkeitsverletzung (Art. 6 Abs. 2 VG)"
    reference = "SR 170.32, Art. 6 Abs. 2"

    def formula(person, period, parameters):
        verletzt = person('persoenlichkeit_widerrechtlich_verletzt', period)
        verschulden = person('beamter_hat_verschulden', period)
        schwere = person('schwere_der_verletzung_rechtfertigt_genugtuung', period)
        wiedergutgemacht = person('verletzung_anderweitig_wiedergutgemacht', period)
        return verletzt * verschulden * schwere * (1 - wiedergutgemacht)
