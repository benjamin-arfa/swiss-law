"""SR 0.142.117.439 Art. 8

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class transited_air(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Transiting through Switzerland Air (Art. 8 SR 0.142.117.439)"

    def formula(person, period, parameters):
        is_air_transit = parameters(period).foreign_policy.transit.air_transit
        transiting_via_chair = parameters(period).foreign_policy.transit.chair
        is_drittstaatenangehoeriger = person("is_drittstaatenangehoeriger", period)
        officer_from_requesting_country = person("officer_from_requesting_country", period)
        officer_from_requesting_country_role = parameters(period).foreign_policy.transit.requesting_country_role
        officer_from_requesting_country_equipped = person("officer_from_requesting_country_equipped", period)
        officer_from_hosting_country_equipped = person("officer_from_hosting_country_equipped", period)
        is_in_transit_area = person("is_in_transit_area", period)

        return is_air_transit & is_drittstaatenangehoeriger & (officer_from_requesting_country == officer_from_transiting_via_chair) & (officer_from_requesting_country_role == "chair") & (officer_from_requesting_country_equipped == True) & is_in_transit_area


class transited_by_land(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Transiting through Switzerland Land (Art. 8 SR 0.142.117.439)"

    def formula(person, period, parameters):
        is_land_transit = parameters(period).foreign_policy.transit.land_transit
        is_drittstaatenangehoeriger = person("is_drittstaatenangehoeriger", period)
        officer_from_hosting_country = person("officer_from_hosting_country", period)
        officer_from_hosting_country_equipped = person("officer_from_hosting_country_equipped", period)

        return is_land_transit & is_drittstaatenangehoeriger & (officer_from_hosting_country_equipped == True)
