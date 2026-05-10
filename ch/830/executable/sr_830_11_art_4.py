"""SR 830.11 Art. 4

Generated from: ch/830/de/830.11.md

Art. 4: Erlass - Waiver of repayment of unlawfully received benefits.
- Abs. 1: Full or partial waiver if received in good faith and repayment
  would cause great hardship.
- Abs. 4: Written request required within 30 days of the repayment decision
  becoming legally binding.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class atsv_leistungen_in_gutem_glauben_empfangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unrechtmaessig gewaehlte Leistungen wurden in gutem Glauben empfangen"
    reference = "SR 830.11 Art. 4 Abs. 1"


class atsv_grosse_haerte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Rueckerstattung wuerde eine grosse Haerte darstellen"
    reference = "SR 830.11 Art. 4 Abs. 1"


class atsv_erlass_rueckerstattung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Erlass der Rueckerstattung unrechtmaessig bezogener Leistungen"
    reference = "SR 830.11 Art. 4"

    def formula(person, period, parameters):
        guter_glaube = person('atsv_leistungen_in_gutem_glauben_empfangen', period)
        haerte = person('atsv_grosse_haerte', period)
        return guter_glaube * haerte


class atsv_erlass_antragsfrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Erlassgesuch in Tagen nach Rechtskraft der Rueckforderungsverfuegung"
    reference = "SR 830.11 Art. 4 Abs. 4"

    def formula(person, period, parameters):
        return 30
