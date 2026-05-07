"""SR 0.103.3 Art. 36

Generated from: ch/0/de/0.103.3.md
"""

]
from openfisca_core.model_api import *
from openfisca_core.variables import Variable


class committee_report_notification(Variable):
    value_type = bool
    label = "Notified in advance about inclusion in annual report (Art. 36)"

    def formula(e, period, parameters):
        published_in_report = e("published_in_committee_report", period)
        notified = e("notified_by_committee", period)
        return published_in_report & notified

class published_in_committee_report(Variable):
    value_type = bool
    label = "Included in annual committee report (Art. 36)"

    def formula(e, period, parameters):
        committee_report_status = e("committee_report_status", period)
        return committee_report_status == 'published'

class notified_by_committee(Variable):
    value_type = bool
    label = "Notified by Committee of inclusion in annual report (Art. 36)"

    def formula(e, period, parameters):
        notification_status = e("committee_notification_status", period)
        return notification_status == 'sent'
