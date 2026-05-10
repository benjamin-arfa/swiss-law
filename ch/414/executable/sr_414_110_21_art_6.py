"""SR 414.110.21 Art. 6

Generated from: ch/414/de/414.110.21.md

Amtsdauer und Wiederwahl:
1. Amtsdauer betraegt 4 Jahre, richtet sich nach der Legislaturperiode
   des Nationalrats. Beginnt am 1. Januar, endet am 31. Dezember.
2. Mitglieder koennen einmal wiedergewaehlt werden (max. 2 Amtsperioden).
   Vorbehalten bleibt die Altersgrenze nach Art. 4 Abs. 1.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vethbk_anzahl_amtsperioden(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl absolvierter Amtsperioden in der ETH-Beschwerdekommission"
    reference = "SR 414.110.21 Art. 6 Abs. 2"


class vethbk_kann_wiedergewaehlt_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Mitglied wiedergewaehlt werden kann"
    reference = "SR 414.110.21 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        amtsperioden = person('vethbk_anzahl_amtsperioden', period)
        max_perioden = parameters(period).sr_414_110_21.max_amtsperioden
        alter = person('vethbk_alter', period.first_month)
        altersgrenze = parameters(period).sr_414_110_21.altersgrenze

        unter_altersgrenze = alter <= altersgrenze
        hat_amtsperioden_uebrig = amtsperioden < max_perioden

        return unter_altersgrenze * hat_amtsperioden_uebrig


class vethbk_amtsdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Amtsdauer in Jahren (4 Jahre)"
    reference = "SR 414.110.21 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        amtsdauer = parameters(period).sr_414_110_21.amtsdauer_jahre
        return amtsdauer + 0 * person('vethbk_anzahl_amtsperioden', period)
