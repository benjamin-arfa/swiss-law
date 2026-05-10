"""SR 0.104 Art. 13

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

def response_status(participating_countries):
    for country in participating_countries:
        response_status = country.get("response_status")
        if response_status is None:
            return "PENDING_RESPONSE"
        if response_status == "ACCEPTE":
            return "ACCEPTED"
        if response_status == "REJECTED":
            return "REJECTED"
    return "PENDING_RESPONSE"

class mediation_conflict_resolution(Variable):
    value_type = str
    label = "Mediation conflict resolution status"
    
    def formula(participating_countries, period, parameters):
        deadline_date = period.date.add(delta=3 * MONTH)
        if deadline_date < now().date:
            return response_status(participating_countries)
        else:
            return "NOT_MEETING_DEADLINE"
