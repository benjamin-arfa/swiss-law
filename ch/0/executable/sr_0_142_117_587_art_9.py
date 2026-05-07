"""SR 0.142.117.587 Art. 9

Generated from: ch/0/de/0.142.117.587.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country, Institution

class responsible_authorities_for_agreement(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Competent authorities responsible for implementing the SR 0.142.117.587 Art. 9 agreement"

    def formula(countries, period, parameters):
        swiss_institutions = ["EJPD", "BFM", "SEM"]
        tunisian_institutions = ["Ministerium für Berufsbildung und Beschäftigung", "Büro für Einwanderung und ausländische Arbeitskräfte", "Ministerium für Soziales", "Amt für Auslandtunesier"]
        current_tunisian_authorities = ", ".join([i for i in (countries("tunisian_authority_1", period), countries("tunisian_authority_2", period), countries("tunisian_authority_3", period), countries("tunisian_authority_4", period)) if i == 'YES' or i == 'True']).split(",")

        def check_institutions(institutions, country, institutions_list):
            return countries(country, period).indicate(
                "institutions" in [i for i in countries(institutions + "_1", period), countries(institutions + "_2", period), countries(institutions + "_3", period), countries(institutions + "_4", period)] if countries(institutions + "_1", period) == 'YES' or countries(institutions + "_1", period) == 'True' or countries(institutions + "_2", period) == 'YES' or countries(institutions + "_2", period) == 'True' or countries(institutions + "_3", period) == 'YES' or countries(institutions + "_3", period) == 'True' or countries(institutions + "_4", period) == 'YES' or countries(institutions + "_4", period) == 'True')
                | countries(institutions + "_1", period) == 'YES' or countries(institutions + "_1", period) == 'True'
                | countries(institutions + "_2", period) == 'YES' or countries(institutions + "_2", period) == 'True'
                | countries(institutions + "_3", period) == 'YES' or countries(institutions + "_3", period) == 'True'
                | countries(institutions + "_4", period) == 'YES' or countries(institutions + "_4", period) == 'True'
            )

        return (check_institutions("EJPD", "Switzerland", swiss_institutions) | check_institutions("SEM", "Switzerland", swiss_institutions)
            | check_institutions("Ministerium für Berufsbildung und Beschäftigung", "Tunisia", tunisian_institutions)
            | check_institutions("Büro für Einwanderung und ausländische Arbeitskräfte", "Tunisia", tunisian_institutions)
            | check_institutions("Ministerium für Soziales", "Tunisia", tunisian_institutions)
            | check_institutions("Amt für Auslandtunesier", "Tunisia", tunisian_institutions)
            | countries("tunisian_authority_1", period) == 'YES' or countries("tunisian_authority_1", period) == 'True' 
            | countries("tunisian_authority_2", period) == 'YES' or countries("tunisian_authority_2", period) == 'True'
            | countries("tunisian_authority_3", period) == 'YES' or countries("tunisian_authority_3", period) == 'True'
            | countries("tunisian_authority_4", period) == 'YES' or countries("tunisian_authority_4", period) == 'True'
            | current_tunisian_authorities in ['YES', 'True'])
