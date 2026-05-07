"""SR 0.142.116.909 Art. 14

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *

class mutual_liability_rule(Variable):
    value_type = bool
    label = "Mutual liability rule for contract staff in transit (Art. 14 SR 0.142.116.909)"
    definition_period = DAY

    def formula(person, period, parameters):
        staff_works_in_foreign_territory = person("staff_foreign_transit", period)
        staff_cause_intent_or_gross NEGLIGENCE = person("staff_cause_intent_or_gross_NEGLIGENCE")
        return not (staff_works_in_foreign_territory & staff_cause_intent_or_gross NEGLIGENCE)

class transit_damage_victim_causes(Variable):
    value_type = float
    label = "transit damage victim cause (SR 0.142.116.909)"
    definition_period = DAY

    def formula(person, period, parameters):
        transit_damage_victim = person("transit_damage_victim")
        staff_foreign_transit = person("staff_foreign_transit")
        domestic_rules_damage_causes = person("domestic_rules_damage_causes")
        return (transit_damage_victim & staff_foreign_transit) + (domestic_rules_damage_causes != 0)


class reimbursement_amount(Variable):
    value_type = float
    label = "SR 0.142.116.909: reimbursement for damages caused by foreign staff to victims"
    definition_period = DAY

    def formula(person, period, parameters):
        damage_paid_by_host_country = parameters(period).mutual_liability_rule.damage_paid_by_host_country
        return damage_paid_by_host_country
