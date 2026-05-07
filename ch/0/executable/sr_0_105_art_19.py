"""SR 0.105 Art. 19

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class art_19_reporting_progress(Variable):
    value_type = str
    entity = Country
    definition_period = YEAR
    label = "Reporting progress under SR 0.105 Art. 19"

    def formula(countries, period, parameters):
        # Assume countries maintain records of report submissions as string.
        report_submissions = countries("report_submissions", period)
        return report_submissions
