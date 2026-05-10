"""SR 0.103.2 Art. 49

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class treaty_entry_into_force(Variable):
    value_type = bool
    label = "Treaty entry into force (Art. 49 SR 0.103.2)"
    entity = World
    definition_period = DAY
    reference = "SR 0.103.2 Art. 49"

    def formula(world, period, parameters):
        # parameters.countries contains historical data for countries' ratification dates
        countries_ratified = parameters(period).treaties.country_ratification
        cumulation_date = None
        num_ratified = 0

        for date in countries_ratified:
            if cumulation_date:
                if date < cumulation_date:
                    num_ratified += 1
                    if num_ratified == 35:
                        cumulation_date = date
                        break
            else:
                if date >= parameters(period).treaties.min_ratification_date:
                    cumulation_date = date
                    num_ratified += 1

        # for each country check if its entry into force is less than or equals to its signatory date
        treaty_entry_into_force_date = cumulation_date
        if treaty_entry_into_force_date:
            return (treaty_entry_into_force_date <= (treaty_entry_into_force_date + MONTHS(3)))
        else:
            return False
