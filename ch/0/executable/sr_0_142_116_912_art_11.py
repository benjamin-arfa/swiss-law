"""SR 0.142.116.912 Art. 11

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *
from openfisca_core.parameters import set_parameters
from openfisca_country_template import Country


class implemented_agreement(Art.11, Country):
    value_type = bool
    entity = Country
    definition_period = PERIOD('year')
    label = "Agreement SR 0.142.116.912 Art. 11 implemented"

    def formula(countries, period, parameters):
        signed_date = countries("signed_date", period)
        shared_departments_date = countries("shared_departments_date", period)
        time_elapsed = (period - signed_date).days
        return (shared_departments_date >= signed_date.add(days=30)) or (time_elapsed > 0)
