"""SR 0.142.114.742 Art. 2

Generated from: ch/0/de/0.142.114.742.md
"""

from openfisca_core.model_api import *

class schengen_visit_entitled(Variable):
    value_type = bool
    label = "Entitlement to a Schengen short stay visa-free (Art. 2 SR 0.142.114.742)"

    def formula(person, period, parameters):
        passport = parameters(period).international_migration.passport_required
        return passport != True
