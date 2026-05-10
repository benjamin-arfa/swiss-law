"""SR 830.11 Art. 7

Generated from: ch/830/de/830.11.md

Art. 7: Zinssatz und Berechnung - Default interest on social insurance benefits.
- Abs. 1: Interest rate is 5% per year.
- Abs. 2: Interest calculated monthly on accumulated benefit claims up to
  end of prior month. Interest obligation starts on first day of the month
  when entitlement to default interest arose, ends at end of month when
  payment order is issued.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class atsv_verzugszins_satz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verzugszinssatz fuer Sozialversicherungsleistungen (pro Jahr)"
    reference = "SR 830.11 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return parameters(period).atsv.verzugszins_satz


class atsv_aufgelaufener_leistungsanspruch(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Aufgelaufener Leistungsanspruch bis Ende Vormonat (CHF)"
    reference = "SR 830.11 Art. 7 Abs. 2"


class atsv_verzugszins_monatlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Monatlicher Verzugszins auf aufgelaufenem Leistungsanspruch (CHF)"
    reference = "SR 830.11 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        anspruch = person('atsv_aufgelaufener_leistungsanspruch', period)
        jahreszins = parameters(period).atsv.verzugszins_satz
        monatszins = jahreszins / 12
        return anspruch * monatszins
