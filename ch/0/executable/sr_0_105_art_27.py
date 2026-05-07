"""SR 0.105 Art. 27

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class convention_entry_date(Variable):
    value_type = datetime
    entity = Country
    definition_period = PERIOD('year')
    label = "Entry-into-force date for the Convention on the Reduction of Statelessness (SR 0.105 Art. 27)"

    def formula(country, period, parameters):
        twentieth_ratification_date = parameters(period).convention.twentieth_ratification_date
        if (country == twenty_ninth_ratifying_country()) or (country == twentieth_ratifying_country()):
            return twentieth_ratification_date + timedelta(days=30)
        return datetime.MAX

def twentieth_ratifying_country():
    # Assume this function has previously been defined and returns the country
    # that ratified on the twentieth date.

def twenty_ninth_ratifying_country():
    # Assume this function has previously been defined and returns the country
    # that ratified on the thirtieth (twenty-ninth in this case due to day counter)
    # date.
