"""SR 831.131.11 Art. 2

Generated from: ch/831/de/831.131.11.md

Refugees' entitlement to integration measures of IV:
- Employed refugees: must have paid IV contributions before disability
- Non-employed/minors: must have resided 1 year in Switzerland before disability
- Children born disabled in Switzerland: immediate entitlement
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_erwerbstaetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person erwerbstaetig ist"
    reference = "SR 831.131.11 Art. 2 Abs. 1"


class hat_iv_beitraege_entrichtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person unmittelbar vor Invaliditaet IV-Beitraege entrichtet hat"
    reference = "SR 831.131.11 Art. 2 Abs. 1"


class ist_minderjaehrig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person minderjaehrig ist"
    reference = "SR 831.131.11 Art. 2 Abs. 2"


class aufenthalt_vor_invaliditaet_jahre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ununterbrochene Aufenthaltsdauer in der Schweiz vor Invaliditaetseintritt (Jahre)"
    reference = "SR 831.131.11 Art. 2 Abs. 2"


class in_schweiz_invalid_geboren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in der Schweiz invalid geboren wurde"
    reference = "SR 831.131.11 Art. 2 Abs. 2"


class seit_geburt_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die Person seit Geburt ununterbrochen in der Schweiz aufgehalten hat"
    reference = "SR 831.131.11 Art. 2 Abs. 2"


class fluechtling_anspruch_eingliederung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch eines Fluechtlings auf Eingliederungsmassnahmen der IV"
    reference = "SR 831.131.11 Art. 2"

    def formula(person, period, parameters):
        ist_fl = person('ist_fluechtling', period)
        wohnsitz = person('wohnsitz_schweiz', period)
        erwerbstaetig = person('ist_erwerbstaetig', period)
        beitraege = person('hat_iv_beitraege_entrichtet', period)
        minderjaehrig = person('ist_minderjaehrig', period)
        aufenthalt = person('aufenthalt_vor_invaliditaet_jahre', period)
        invalid_geboren = person('in_schweiz_invalid_geboren', period)
        seit_geburt = person('seit_geburt_in_schweiz', period)

        # Abs. 1: employed refugees who paid contributions
        erwerbstaetig_anspruch = erwerbstaetig * beitraege

        # Abs. 2: non-employed or minors with 1 year residence
        nichterwerbstaetig_anspruch = not_(erwerbstaetig) * (aufenthalt >= 1)

        # Abs. 2: minors born disabled or since birth in CH
        minderjaehrig_anspruch = minderjaehrig * (invalid_geboren + seit_geburt)

        return ist_fl * wohnsitz * (
            erwerbstaetig_anspruch + nichterwerbstaetig_anspruch + minderjaehrig_anspruch > 0
        )
