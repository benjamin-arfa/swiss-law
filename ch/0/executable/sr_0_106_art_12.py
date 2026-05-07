"""SR 0.106 Art. 12

Generated from: ch/0/de/0.106.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import Variable

class ahv_annual_report_published(Variable):
    value_type = bool
    definition_period = YEAR
    label = "AHV committee annual report published (Art. 12 AHVG)"

    def formula(variables, period, parameters):
        return True  # Annual report is a mandatory obligation, will be true each year
