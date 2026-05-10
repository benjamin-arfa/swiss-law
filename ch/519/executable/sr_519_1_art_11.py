"""SR 519.1 Art. 11

Generated from: ch/519/de/519.1.md

Art. 11 Einsatzzulage (Deployment allowance):
1. For each deployment, a deployment allowance of at most CHF 110 per day is granted.
2. It compensates for special deployment conditions (permanent availability,
   isolation, climate, deprivations), increased risks to life and limb, and
   additional costs related to the deployment.
3. The deployment allowance covers claims for Sunday, night, and shift work
   as well as on-call duty.
4. The VBS sets the amount after consulting the EDA.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pvspa_einsatztage_pro_monat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Number of deployment days in the month"
    reference = "SR 519.1 Art. 11 Abs. 1"


class pvspa_einsatzzulage_pro_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Daily deployment allowance set by VBS (CHF), max 110"
    reference = "SR 519.1 Art. 11 Abs. 1, 4"

    def formula(person, period, parameters):
        rate = parameters(period).sr_519_1.einsatzzulage_pro_tag
        return min_(rate, 110)


class pvspa_einsatzzulage_monatlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Monthly deployment allowance (CHF) = days * daily rate (max 110/day)"
    reference = "SR 519.1 Art. 11"

    def formula(person, period, parameters):
        tage = person('pvspa_einsatztage_pro_monat', period)
        zulage_pro_tag = person('pvspa_einsatzzulage_pro_tag', period)
        return tage * zulage_pro_tag


class pvspa_sonntagsarbeit_abgegolten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether Sunday/night/shift/on-call claims are covered by the deployment allowance"
    reference = "SR 519.1 Art. 11 Abs. 3"

    def formula(person, period, parameters):
        einsatzzulage = person('pvspa_einsatzzulage_monatlich', period)
        return einsatzzulage > 0
