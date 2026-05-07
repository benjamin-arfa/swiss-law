"""SR 0.142.117.121 Art. 22

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person, Agreements


class has_suspended_agreement(Variable):
    value_type = bool
    entity = Person
    definition_period = "HISTORY"
    label = "Has suspended agreement"
    scope = ["state", "period"]

    def formula(person, period, parameters):
        # person is of type "Person" defined elsewhere
        agreement_entity = person("agreement_entity", period)
        is_other_party_suspended = agreement_entity["is_other_party_suspended"]
        has_acknowledged_notification = agreement_entity["has_acknowledged_notification"]
        
        # suspended and notification made 48 hours prior to the notification's current month
        return (is_other_party_suspended & ~has_acknowledged_notification & (period.index_in_period_last() - 48) >= 0)

class Suspended_agreements(Agreements):
    description = "Has an agreement being suspended."
    def create_agreement(self, parties: list):
        agreement_entity = Suspended_agreements.create(self, parties)
        agreement_entity["is_other_party_suspended"] = False
        agreement_entity["has_acknowledged_notification"] = False
        agreement_entity["effective_date"] = None # default value set
        return agreement_entity
    def notify_suspended(self, person: Person, effective: date):
        if effective + timedelta(days=3)
            is_other_party_suspended = True
            agreement_entity.notify_suspended(person)
    def notify_resolved(self, person: Person):
        if effective > self.get_agreement(person).effective_date() + timedelta(days=48):
            is_other_party_suspended = False # lift suspension
            agreement_entity.notify_resolved(person)

class agreement_entity(AgreementsEntity):
    description = "Agreement Entity"
    
    def create_agreement(self, parties: list):
        agreement_entity = agreement_entity.create(self, parties)
        agreement_entity["has_acknowledged_notification"] = False
        # do nothing more with 'is_other_party_suspended'; no notification history stored.
        return agreement_entity
    # notify and notify_resolved are likely not needed, as suspension is automatically lifted after 48 hours.
