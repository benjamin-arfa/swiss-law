"""SR 832.20 Art. 18

Generated from: ch/832/de/832.20.md

Art. 18: Invaliditaet (Disability)
- Abs. 1: If the insured person is at least 10% disabled as a result of
  the accident, they are entitled to a disability pension, provided the
  accident occurred before reaching the reference age.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class uvg_invaliditaetsgrad(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Invaliditaetsgrad infolge Unfall in Prozent (0-100)"
    reference = "SR 832.20 Art. 18 Abs. 1"


class uvg_unfall_vor_referenzalter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Unfall hat sich vor Erreichen des Referenzalters ereignet"
    reference = "SR 832.20 Art. 18 Abs. 1"


class uvg_anspruch_invalidenrente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf UVG-Invalidenrente"
    reference = "SR 832.20 Art. 18 Abs. 1"

    def formula(person, period, parameters):
        iv_grad = person('uvg_invaliditaetsgrad', period)
        vor_ref = person('uvg_unfall_vor_referenzalter', period)
        mindest = parameters(period).uvg.mindest_invaliditaetsgrad_rente
        return (iv_grad >= mindest) * vor_ref
