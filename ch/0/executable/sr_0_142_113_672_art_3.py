"""SR 0.142.113.672 Art. 3

Generated from: ch/0/de/0.142.113.672.md
"""

from openfisca_core.model_api import *
import numpy as np
from openfisca_core.exceptions import identify_country


class agreement_applicability(Variable):
    value_type = bool
    entity = MeshedRegion
    definition_period = ANY
    label = "Country of applicability of the agreement (Art. 3)"


    def formula(m, period, parameters):
        country_names = ['CH', 'GB']
        countries = m.entities('country')
        countries_dict = {}
        for country in countries:
            countries_dict[country] = country.code
        country_identifier = parameters(period).countries.identifier
        apply_country = np.any(countries_dict[country_identifier] == country_names)
        return apply_country
