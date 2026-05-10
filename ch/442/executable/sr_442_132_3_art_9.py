"""SR 442.132.3 Art. 9

Generated from: ch/442/de/442.132.3.md

Lohnanspruch bei Krankheit und Unfall:
- 100% waehrend 12 Monaten
- 80% danach (Krankheit: 730 Taggelder in 900 Tagen, Wartefrist 60 Tage;
  Unfall: weitere 12 Monate)
- Praemien Krankentaggeld: 1/3 Mitarbeitende, 2/3 Stiftung (umgekehrt bei NBU)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class monate_seit_arbeitsverhinderung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Monate seit Beginn der Arbeitsverhinderung"
    reference = "SR 442.132.3 Art. 9 Abs. 1"


class arbeitsverhinderung_grund(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Grund der Arbeitsverhinderung (0=keine, 1=Krankheit, 2=Unfall)"
    reference = "SR 442.132.3 Art. 9 Abs. 1"


class lohnfortzahlung_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Lohnfortzahlung in Prozent bei Krankheit/Unfall"
    reference = "SR 442.132.3 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        monate = person('monate_seit_arbeitsverhinderung', period)
        grund = person('arbeitsverhinderung_grund', period)
        # Keine Arbeitsverhinderung: 100%
        keine = (grund == 0) * 100
        # Erste 12 Monate: 100%
        erste_phase = (grund > 0) * (monate <= 12) * 100
        # Nach 12 Monaten: 80% (bei Unfall max weitere 12 Monate)
        zweite_phase_krankheit = (grund == 1) * (monate > 12) * (monate <= 36) * 80
        zweite_phase_unfall = (grund == 2) * (monate > 12) * (monate <= 24) * 80
        return keine + erste_phase + zweite_phase_krankheit + zweite_phase_unfall


class anteil_praemien_krankentaggeld_mitarbeiter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Mitarbeitenden an Krankentaggeld-Praemien (1/3)"
    reference = "SR 442.132.3 Art. 9 Abs. 6"
    default_value = 0.3333


class anteil_praemien_nbu_mitarbeiter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Mitarbeitenden an NBU-Praemien (2/3)"
    reference = "SR 442.132.3 Art. 9 Abs. 6"
    default_value = 0.6667
