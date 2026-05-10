"""SR 0.101.06 Art. 8

Generated from: ch/0/de/0.101.06.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_country_es import CountryTaxBenefitSystem

class ProtokollArt8Date(CountryTaxBenefitSystem):
    def definition_class_tax_benefit_system():
        from dateutil.relativedelta import relativedelta
        from dateutil.parser import parse

        # Get the current date
        today = parse('today')

        # Hardcoded parameter for the number of member states that need to give consent to enable the protocol
        _parameter = 'protokoll_art8_member_states'
        _value = 5  # Must be set in the parameters file

        def formula(person, period):
            # Get the consent dates for all relevant member states
            consent_dates = {name: person('consent_date_' + name, period) for name in _get_member_states(person, period)}
            
            # If there are enough consent dates, determine when the protocol applies
            if len(_get_member_states(person, period)) >= _value:
                # If the person or one of the member states has given consent in the past year, 
                # determine when the protocol comes into effect
                if (today - parse('1 year')).replace(day=1) > today:
                    first_day = parse('1 month').replace(year=today.year, month=1)
                else:
                    first_day = today.replace(day=1)

                for name in _get_member_states(person, period):
                    if consent_dates[name] is not None and consent_dates[name] > first_day:
                        first_day = consent_dates[name]
            else:
                # If the person has given consent in the past year, it only comes into effect on the next month
                first_day = today.replace(day=1)

            return first_day

        def _get_member_states(person, period):
            # This function is assumed to be implemented elsewhere
            # and returns the names of the member states as OpenFisca variables
            pass
        
        # Must be implemented elsewhere, along with the function to get consent dates
        return first_day

    class variable(definition_class_tax_benefit_system):
        value = formula
