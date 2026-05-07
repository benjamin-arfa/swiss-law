"""SR 0.103.1 Art. 8

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *

class trade_union_formation_right(Variable):
    value_type = bool
    label = "Right to form a trade union"
    
    def formula(variables, period, parameters):
        context = variables.get(context, period)
        is_military_employee = context("is_military_employee", variables period)
        is_police_employee = context("is_police_employee", variables, period)
        is_public_admin_employee = context("is_public_admin_employee", variables, period)

        trade_union = variables("trade_union_status", period)

        if not is_military_employee and not is_police_employee and not is_public_admin_employee:
            return trade_union & (trade_union_status not in ["former_member", " expelled"])
        else:
            return False

class trade_union_participation_right(Variable):
    value_type = bool

    def formula(variables, period, parameters):
        context = variables.get(context, period)
        is_military_employee = context("is_military_employee", variables, period)
        is_police_employee = context("is_police_employee", variables, period)
        is_public_admin_employee = context("is_public_admin_employee", variables, period)

        trade_union = variables("trade_union_status", period)

        if not is_military_employee and not is_police_employee and not is_public_admin_employee:
            return trade_union
        else:
            return False

class strike_right(Variable):
    value_type = bool
    
    def formula(variables, period, parameters):
        context = variables.get(context, period)
        is_military_employee = context("is_military_employee", variables, period)
        is_police_employee = context("is_police_employee", variables, period)
        is_public_admin_employee = context("is_public_admin_employee", variables, period)

        if not is_military_employee and not is_police_employee and not is_public_admin_employee:
            return variables("trade_union_status", period) == "member"
        else:
            return False
