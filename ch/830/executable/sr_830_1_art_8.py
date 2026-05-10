"""SR 830.1 Art. 8

Generated from: ch/830/de/830.1.md

Art. 8: Invalidität - Disability is a presumably permanent or long-lasting
full or partial incapacity to earn. Special rules for minors and adults
who were not gainfully employed.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_minderjaehrig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist minderjährig"
    reference = "SR 830.1 Art. 8 Abs. 2"


class ist_nicht_erwerbstaetig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist nicht erwerbstätig"
    reference = "SR 830.1 Art. 8 Abs. 2-3"


class erwerbstaetigkeit_nicht_zumutbar(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person kann eine Erwerbstätigkeit nicht zugemutet werden (Art. 8 Abs. 3)"
    reference = "SR 830.1 Art. 8 Abs. 3"


class unmoeglich_im_aufgabenbereich_zu_betaetigen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Unmöglichkeit, sich im bisherigen Aufgabenbereich zu betätigen (Art. 8 Abs. 3)"
    reference = "SR 830.1 Art. 8 Abs. 3"


class erwerbsunfaehigkeit_voraussichtlich_bleibend_oder_langdauernd(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Erwerbsunfähigkeit ist voraussichtlich bleibend oder längere Zeit dauernd"
    reference = "SR 830.1 Art. 8 Abs. 1"


class beeintraechtigung_wird_erwerbsunfaehigkeit_zur_folge_haben(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = (
        "Gesundheitsbeeinträchtigung wird voraussichtlich ganze oder teilweise "
        "Erwerbsunfähigkeit zur Folge haben (Minderjährige, Art. 8 Abs. 2)"
    )
    reference = "SR 830.1 Art. 8 Abs. 2"


class ist_invalid(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist invalid im Sinne von Art. 8 ATSG"
    reference = "SR 830.1 Art. 8"

    def formula(person, period, parameters):
        # Abs. 1: Erwerbsunfähigkeit voraussichtlich bleibend/langdauernd
        ist_erwerbsunfaehig = person('ist_erwerbsunfaehig', period)
        bleibend = person('erwerbsunfaehigkeit_voraussichtlich_bleibend_oder_langdauernd', period)
        invaliditaet_abs1 = ist_erwerbsunfaehig * bleibend

        # Abs. 2: Nicht erwerbstätige Minderjährige
        minderjaehrig = person('ist_minderjaehrig', period)
        nicht_erwerbstaetig = person('ist_nicht_erwerbstaetig', period)
        wird_folge_haben = person('beeintraechtigung_wird_erwerbsunfaehigkeit_zur_folge_haben', period)
        invaliditaet_abs2 = minderjaehrig * nicht_erwerbstaetig * wird_folge_haben

        # Abs. 3: Volljährige, die vor Beeinträchtigung nicht erwerbstätig waren
        volljaehrig = 1 - minderjaehrig
        nicht_zumutbar = person('erwerbstaetigkeit_nicht_zumutbar', period)
        unmoeglich = person('unmoeglich_im_aufgabenbereich_zu_betaetigen', period)
        invaliditaet_abs3 = volljaehrig * nicht_erwerbstaetig * nicht_zumutbar * unmoeglich

        return invaliditaet_abs1 + invaliditaet_abs2 + invaliditaet_abs3 > 0
