"""SR 0.142.117.121 Art. 23

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# This is a non-standard use-case for OpenFisca.

# Note about Art. 23:
# From a strictly simulation and OpenFisca perspective, it would not immediately apply for any entities on particular specific dates.

# Consider adding conditions into the formula as desired.
# However, there would not be much value if considering the typical case for Swiss regulation on taxes and social insurances.

# Example for demonstration purposes:

# This formula is purely illustrative since the given use case does not map perfectly to OpenFisca usage and cannot be applied directly to the variable below:





class any_abkommen_kündigung(Variable):
    value_type = bool
    label = "Notification for Kündigung and termination as per Art. 23"

    def formula(survey, period, parameters):
        # Demonstrative formula showing how to apply notification condition, but does not have any real-world application in OpenFisca for this purpose.
        # Notification flag based on the date and parties' specific agreement would depend on external information which isn't directly provided by the legislation

        notification_date = survey("notification_date", period)
        thirty_days_notification_period = survey("thirty_days_notification_period", period)
        kundigung_date = survey("kundigung_date", period)

        return (notification_date <= kundigung_date or thirty_days_notification_period > 0)
