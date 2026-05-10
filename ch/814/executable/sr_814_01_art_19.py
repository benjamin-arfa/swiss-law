"""SR 814.01 Art. 19-20

Generated from: ch/fr/814/814.01.md

Art. 19: Valeurs d'alarme (Alarmwerte)
- Federal Council may set alarm values for noise immissions
  above immission limit values to assess urgency of remediation.
Art. 20: Isolation acoustique des immeubles existants
- When source measures cannot bring noise below alarm value for existing buildings
  near roads/airports/railways, owners must install soundproofing.
- Costs borne by installation owner unless building was built after threshold exceeded.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class usg_alarmwert_laerm_db(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Geltender Alarmwert fuer Laerm in dB(A)"
    reference = "SR 814.01 Art. 19"


class usg_laerm_ueber_alarmwert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Laermimmissionen den Alarmwert ueberschreiten"
    reference = "SR 814.01 Art. 19"

    def formula(person, period, parameters):
        aktuell = person('usg_immissionswert_laerm_db', period)
        alarmwert = person('usg_alarmwert_laerm_db', period)
        return aktuell > alarmwert


class usg_schallschutzfenster_pflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Pflicht zum Einbau von Schallschutzfenstern besteht"
    reference = "SR 814.01 Art. 20 Abs. 1"

    def formula(person, period, parameters):
        ueber_alarmwert = person('usg_laerm_ueber_alarmwert', period)
        return ueber_alarmwert


class usg_gebaeude_vor_grenzwertuebersch_gebaut(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob das Gebaeude gebaut wurde, bevor die Immissionsgrenzwerte ueberschritten wurden"
    reference = "SR 814.01 Art. 20 Abs. 2"


class usg_kostentraeger_schallschutz_ist_anlagebetreiber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Anlagenbetreiber die Kosten fuer den Schallschutz traegt"
    reference = "SR 814.01 Art. 20 Abs. 2"

    def formula(person, period, parameters):
        pflicht = person('usg_schallschutzfenster_pflicht', period)
        vor_ueberschreitung = person('usg_gebaeude_vor_grenzwertuebersch_gebaut', period)
        # Installation owner pays if building was built before threshold was exceeded
        return pflicht * not_(vor_ueberschreitung)
