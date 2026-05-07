"""SR 0.101.094 Art. 16

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core import periods, variables
from openfisca_country_templates import entities

class sanction_when_party_refuse_follow_court_decision(entities.MacroEntity period),
    variables.DecimalVariable:

    set_attribute(
        label = "Amount of the penalty applied when a party ignores a court decision",
        entity = entities.HoheVertragspartei,
        definition_period = periods.year,
        value_type = 'decimal',
        unit = 'chf'
    )

    set_formula = formula(decimal_lumpsum(
        "sanction_amount",
        0,  # no penalty if the party follows the decision
        max(0, sanction_amount),  # penalty if the party refuses to follow the decision
        max(0, ((sanction_amount) )  # maximum penalty
    )).over(periods.year)

    set_parameter(min_rate = 0.0, max_rate = 1000.0, threshold = 0.5)
