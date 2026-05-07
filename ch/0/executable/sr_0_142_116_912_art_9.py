"""SR 0.142.116.912 Art. 9

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *

class nationality_repatriation_obligation(Variable):
    value_type = bool
    label = "Obligation to repatriate non-entitled nationals"
    definition_period = YEAR

    def formula_implementation(self, council decisions, periods, parameters):
        def should_repatriate(person_data):
            # Nationality status
            nationality_is_not_entitled = not (person_data['nationality'] == decisions.current_legislative_period['country_nationality'])
            nationality_is_entitled = person_data['nationality'] == decisions.current_legislative_period['country_nationality']

            # Visa and residence status
            visa_is_required = person_data['requires_visitation']
            residence_is_invalid = person_data['residence_status'] == 'invalid'

            # Exception conditions
            visa_exists = person_data.get('country_of_origin_residence_visums') == decisions.current_legislative_period['foreign_country_residence']
            foreigner_has_already_resided_in_another_country = person_data['dual_residence'] == True

            if nationality_is_not_entitled or (visa_is_required and residence_is_invalid):
                return True

            if person_data['time_point_of_residency'] > 0 and (visa_exists or foreigner_has_already_resided_in_another_country):
                return False

            return True

        return should_repatriate
