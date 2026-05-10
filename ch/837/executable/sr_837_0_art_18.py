"""SR 837.0 Art. 18

Generated from: ch/837/de/837.0.md

Art. 18: Wartezeiten (Waiting periods)
- Abs. 1: Entitlement begins after a waiting period of 5 days of controlled
  unemployment. For persons without support obligations for children under 25:
  a. 10 days for insured income between CHF 60'001 and 90'000
  b. 15 days for insured income between CHF 90'001 and 125'000
  c. 20 days for insured income over CHF 125'000
- Abs. 2: Persons exempt from contribution period (Art. 14) must serve an
  additional special waiting period of up to 12 months before first claim
  in the framework period.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_versicherter_verdienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherter Verdienst (jaehrlich, CHF)"
    reference = "SR 837.0 Art. 23"


class alv_unterhaltspflicht_kinder_unter_25(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unterhaltspflicht gegenueber Kindern unter 25 Jahren"
    reference = "SR 837.0 Art. 18 Abs. 1, Art. 22 Abs. 2 Bst. a"


class alv_wartezeit_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Wartezeit in Tagen nach Art. 18 AVIG"
    reference = "SR 837.0 Art. 18 Abs. 1"

    def formula(person, period, parameters):
        verdienst = person('alv_versicherter_verdienst', period)
        unterhalt = person('alv_unterhaltspflicht_kinder_unter_25', period.first_month)
        p = parameters(period).alv

        # Base waiting period is 5 days for all
        basis = p.wartezeit_allgemein_tage

        # Additional waiting days for persons WITHOUT child support obligations
        # and with higher income
        stufe_1 = (
            (unterhalt == False)
            * (verdienst >= p.wartezeit_stufe_1_min)
            * (verdienst <= p.wartezeit_stufe_1_max)
            * p.wartezeit_stufe_1_tage
        )
        stufe_2 = (
            (unterhalt == False)
            * (verdienst >= p.wartezeit_stufe_2_min)
            * (verdienst <= p.wartezeit_stufe_2_max)
            * p.wartezeit_stufe_2_tage
        )
        stufe_3 = (
            (unterhalt == False)
            * (verdienst >= p.wartezeit_stufe_3_min)
            * p.wartezeit_stufe_3_tage
        )

        # The law specifies the total waiting period for each tier
        # (not additive to the 5-day base), but persons with child support
        # obligations always get only the 5-day base.
        keine_erhoehung = unterhalt + (verdienst <= 60000)
        wartezeit = (
            keine_erhoehung * basis
            + stufe_1
            + stufe_2
            + stufe_3
        )
        return wartezeit
