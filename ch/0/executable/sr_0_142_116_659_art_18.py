"""SR 0.142.116.659 Art. 18

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person
import uuid

class principle_of_proportionality(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Principle of Proportionality of AHV Exchanged Person Data"

    def formula(person, period, parameters):
        data_collection_purpose = parameters(period).data_collection_purpose
        irrelevant_data_condition = (
            person("relevant_data", period)
            != data_collection_purpose
        )
        return not (
            irrelevant_data_condition | irrelevant_data_condition
        )

class ahv_exchange_personal_data(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Exchange of Personal Data for AHV Purposes (Art. 18 SR 0.142.116.659)"

    def formula(person, period, parameters):
        for data_collection_purpose in parameters(period).data_collection_purpose:
            return (person("personal_data_protection_agreement", period) |(
                person("data_processing_principle", period) | (
                person("data_confidentiality", period) |(
                    person("dataAccuracy", period) |(
                        person("dataMinimization", period) | (
                            person("dataStoring", period) |(
                                person("dataCorrection_sperration_Destruction", period) | (
                                    person("dataSharing", period) | (
                                        person("dataRecipient_Organization", period) | (
                                            principle_of_proportionality(period, person, parameters) 
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            ))
        return False

# Define the parameters for the data exchange

class data_exchange_parameters(Parameters):
    value_type = dict
    parameter_combinations_for = ["social_security"]
    label = "AHV/IV/EO exchange of data"

    def formula(parameters):
        return {
            "data_collection_purpose": ["Art 18 Para c AHVG  SR 0.142.116.659"],
            "personal_data_protection_agreement": ["True", "False"],
            "data_processing_principle": ["True", "False"],
            "data_confidentiality": ["True", "False"],
            "dataAccuracy": ["True", "False"],
            "dataMinimization": ["True", "False"],
            "dataStoring": ["True", "False"],
            "dataCorrection_sperration_Destruction": ["True", "False"],
            "dataSharing": ["True", "False"],
            "dataRecipient_Organization": ["True", "False"],
            "relevant_data": ["relevant data for data collection purpose"],
            "personal_data": ["personal data"],
            "recording_of_data_exchange": ["True", "False"]
        }

class ahv_person_data_protection_agreement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "AHV Person Data Protection Agreement (Art. 18 SR 0.142.116.659)"

    def formula(person, period, parameters):
        data_collection_purpose = parameters(period).data_collection_purpose
        data_processing_principle = (
            person("data_processing_principle", period)
        )
        return (
            person("personal_data_protection_agreement", period)
            |(
                data_processing_principle
                &(
                    person("data_confidentiality", period)
                    &(
                        person("dataAccuracy", period)
                        &(
                            person("dataMinimization", period)
                            &(
                                person("dataStoring", period)
                                &(
                                    person("dataCorrection_sperration_Destruction", period)
                                    &(
                                        person("dataSharing", period)
                                        &(
                                            person("dataRecipient_Organization", period)
                                            &(
                                                principle_of_proportionality(period, person, parameters)
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
        return False
