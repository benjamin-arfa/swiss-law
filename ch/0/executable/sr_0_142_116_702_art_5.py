"""SR 0.142.116.702 Art. 5

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_country_tax_benefit_entities import Country


class is_foreign_partner_country(Variable):
    value_type = bool
    entity = Country
    definition_period = ETERNITY
    label = "Country is partner in passport data sharing agreement"

    def formula(countries, period, parameters):
        partner_countries = parameters(period).international_agreements.passport_data_sharing_partners
        return countries.is_in(partner_countries)


class send_new_passport_must(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Must send new passport information (SR 0.142.116.702 Art. 5)"

    def formula(countries, period, parameters):
        new_features_introduction_date = parameters(period).international_agreements.passport_data_sharing.new_features_introduction_date
        return period.before(new_features_introduction_date) and (period.after(new_features_introduction_date - 30, label='30 days before new features introduction'))


class exchange_passport_must(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Must exchange passport information (SR 0.142.116.702 Art. 5)"

    def formula(countries, period, parameters):
        new_features_introduction_date = parameters(period).international_agreements.passport_data_sharing.new_features_introduction_date
        agreement_signing_date = parameters(period).international_agreements.passport_data_sharing.agreement_signing_date
        return period.overlaps((agreement_signing_date + 30, agreement_signing_date + 31), label='30 days after agreement signing')
