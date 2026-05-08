"""SR 822.11 Art. 9

Generated from: ch/822/de/822.11.md

Art. 9: Hoechstarbeitszeit
- Abs. 1: Woechentliche Hoechstarbeitszeit betraegt:
  a. 45 Stunden fuer Arbeitnehmer in industriellen Betrieben, Bueropersonal,
     technische und andere Angestellte inkl. Verkaufspersonal in Grossbetrieben
  b. 50 Stunden fuer alle uebrigen Arbeitnehmer
- Abs. 3: Verlaengerung um max. 4 Stunden durch Verordnung moeglich
- Abs. 4: Verlaengerung um max. 4 Stunden durch SECO-Bewilligung moeglich
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arg_industrieller_betrieb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitnehmer ist in einem industriellen Betrieb taetig"
    reference = "SR 822.11 Art. 9 Abs. 1 Bst. a"


class arg_bueropersonal_oder_angestellte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Arbeitnehmer ist Bueropersonal, technischer oder anderer Angestellter "
        "inkl. Verkaufspersonal in Grossbetrieben des Detailhandels"
    )
    reference = "SR 822.11 Art. 9 Abs. 1 Bst. a"


class arg_woechentliche_hoechstarbeitszeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Woechentliche Hoechstarbeitszeit in Stunden (45 oder 50)"
    reference = "SR 822.11 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        industriell = person('arg_industrieller_betrieb', period)
        buero = person('arg_bueropersonal_oder_angestellte', period)
        # 45h for industrial workers and office/technical staff; 50h for all others
        return where(industriell + buero > 0, 45.0, 50.0)


class arg_hoechstarbeitszeit_verlaengerung_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    default_value = 0.0
    label = (
        "Verlaengerung der woechentlichen Hoechstarbeitszeit durch Verordnung "
        "oder SECO-Bewilligung (max. 4 Stunden)"
    )
    reference = "SR 822.11 Art. 9 Abs. 3-4"


class arg_effektive_woechentliche_hoechstarbeitszeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Effektive woechentliche Hoechstarbeitszeit inkl. allfaelliger Verlaengerung"
    reference = "SR 822.11 Art. 9"

    def formula(person, period, parameters):
        basis = person('arg_woechentliche_hoechstarbeitszeit', period)
        verlaengerung = person('arg_hoechstarbeitszeit_verlaengerung_stunden', period)
        # Extension capped at 4 hours
        verlaengerung_begrenzt = min_(verlaengerung, 4.0)
        return basis + verlaengerung_begrenzt
