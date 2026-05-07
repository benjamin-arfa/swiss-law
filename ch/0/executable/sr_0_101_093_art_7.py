"""SR 0.101.093 Art. 7

Generated from: ch/0/de/0.101.093.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

from datetime import datetime, timedelta

def calculate_legal_protocol_entry_date(year, month, country_code, consent_date=None):
    three_months_duration = timedelta(days=90)
    entry_date = datetime(year=year, month=month, day=1)
    
    if consent_date:
        # For countries that have already expressed their consent
        consent_date = datetime.fromisoformat(consent_date)
        if country_code not in consent_countries:
            raise Exception(f"Country {country_code} has not expressed its consent yet.")
        entry_date = consent_date + three_months_duration
        
    return entry_date

def legal_protocol_entry_date(countries, person, period):
    country_code = person('country')  # assuming 'country' returns the country code
    consent_date = person('consent_date', period)  # assuming 'consent_date' returns the date of consent
    
    if country_code in consent_countries:
        # Set the entry date based on the deposit date
        consent_date = person('consent_deposit_date', period)
    
    return calculate_legal_protocol_entry_date(period.year, period.month, country_code, consent_date)

consent_countries = {'CH', 'DE', 'FR'}  # List of countries that have expressed their consent
