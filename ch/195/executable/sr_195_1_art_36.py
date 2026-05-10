"""SR 195.1 Art. 36

Generated from: ch/195/de/195.1.md

Befristung der Rueckerstattungspflicht und Unverzinslichkeit: 10 Jahre
ab letzter Auszahlung, Forderungen sind unverzinslich.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_letzter_auszahlung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Jahre seit der letzten Auszahlung der Sozialhilfeleistung"
    reference = "SR 195.1 Art. 36 Abs. 1"


class forderung_vertraglich_oder_kd_festgesetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Forderung vertraglich oder durch die KD festgesetzt wurde"
    reference = "SR 195.1 Art. 36 Abs. 1"


class rueckforderung_noch_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sozialhilfeleistung noch zurueckgefordert werden kann (max 10 Jahre)"
    reference = "SR 195.1 Art. 36 Abs. 1"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_letzter_auszahlung', period)
        festgesetzt = person('forderung_vertraglich_oder_kd_festgesetzt', period)
        # Hoechstens 10 Jahre, ausser bei Festsetzung
        return (jahre <= 10) + festgesetzt > 0
