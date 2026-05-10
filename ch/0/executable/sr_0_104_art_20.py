"""SR 0.104 Art. 20

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class formal_complaint_status(Variable):
    value_type = bool
    entity = Country
    definition_period = DAY
    label = "Status of formal complaint regarding a reservation (SR 0.104 Art. 20)"

    def formula(countries, period, parameters):
        complaint_registered = countries("reservations_complaint", period)
        notification_delay = 90
        complaint_days_affecting = countries("reservations_complaint_days_affecting", period)
        return (complaint_registered == "yes") & (complaint_days_affecting <= notification_delay)
        
class reservations_complaint(Variable):
    value_type = str
    entity = Country
    definition_period = DAY
    label = "Has a formal complaint regarding a reservation been registered (SR 0.104 Art. 20)"

    def formula(countries, period, parameters):
        return "yes" if countries("has_reserved_state objected", period) == "yes" else "no"
        
class reservations_complaint_days_affecting(Variable):
    value_type = int
    entity = Country
    definition_period = DAY
    label = "Days since formal complaint regarding a reservation (SR 0.104 Art. 20)"

    def formula(countries, period, parameters):
        last_complaint_date = countries("last_complaint_notification", period)
        current_date = period.date
        days_affecting = (current_date - last_complaint_date).days
        return days_affecting

class last_complaint_notification(Variable):
    value_type = date
    entity = Country
    definition_period = DAY
    label = "Date of the last complaint notification regarding a reservation (SR 0.104 Art. 20)"

    def formula(countries, period, parameters):
        return countries.last_notification_date
