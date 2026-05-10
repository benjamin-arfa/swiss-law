"""SR 741.01 Art. 15a - Fuehrerausweis auf Probe

Generated from: ch/de/741/741.01.md

Probationary driving license:
- Probation period: 3 years
- Extension by 1 year for medium/severe violation
- Expiry upon second medium/severe violation during probation
- New learner permit: earliest 1 year after offense + psych assessment
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fuehrerausweis_auf_probe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person einen Fuehrerausweis auf Probe besitzt"
    reference = "SR 741.01 Art. 15a Abs. 1"


class probezeit_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer der Probezeit in Jahren (Grunddauer 3)"
    reference = "SR 741.01 Art. 15a Abs. 1"

    def formula(person, period, parameters):
        return 3


class widerhandlung_mittelschwer_oder_schwer_in_probezeit(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl mittelschwerer oder schwerer Widerhandlungen waehrend Probezeit"
    reference = "SR 741.01 Art. 15a Abs. 3-4"


class probezeit_verlaengerung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Verlaengerung der Probezeit in Jahren"
    reference = "SR 741.01 Art. 15a Abs. 3"

    def formula(person, period, parameters):
        widerhandlungen = person('widerhandlung_mittelschwer_oder_schwer_in_probezeit', period)
        auf_probe = person('fuehrerausweis_auf_probe', period)
        # First violation: extend by 1 year
        return auf_probe * (widerhandlungen >= 1) * 1


class probeausweis_verfallen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Fuehrerausweis auf Probe verfallen ist (2. Widerhandlung)"
    reference = "SR 741.01 Art. 15a Abs. 4"

    def formula(person, period, parameters):
        widerhandlungen = person('widerhandlung_mittelschwer_oder_schwer_in_probezeit', period)
        auf_probe = person('fuehrerausweis_auf_probe', period)
        return auf_probe * (widerhandlungen >= 2)


class sperrfrist_neuer_lernfahrausweis_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Sperrfrist fuer neuen Lernfahrausweis nach Verfall in Monaten"
    reference = "SR 741.01 Art. 15a Abs. 5"

    def formula(person, period, parameters):
        verfallen = person('probeausweis_verfallen', period)
        # Earliest 1 year after offense; +1 year if drove during ban
        return verfallen * 12
