"""SR 0.142.116.909 Art. 1

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *

class citizenship_verification_status(Variable):
    value_type = bool
    label = "citizenship verification status"
    definition_period = YEAR

    def formula(person, period, parameters):
        # No parameter required, as this is a direct implementation of art. 1 para. 1
        
        citizenship_verified = parameters(period).international_affairs.citizenship_verification_status
        return citizenship_verified

class removedIndividualStatus(Variable):
    value_type = bool
    label = "removed individual's status"
    definition_period = year

    def formula(person, period, parameters):
        removed = (parameters(period).international_affairs.removed_individuals
                   [person("country_of_birth", period)] >= person("year_of_birth", period) +
        (parameters(period).international_affairs.removed_individuals
          [person("country_of_birth", period)] <= person("year_of_birth", period)))
        status = ((removed >= parameters(period).international_affairs.removed_period) +
                                            ((removed + parameters(period).international_affairs.removed_period)
                                  >= parameters(period).international_affairs.end_period)
        return status

class returnedIndividualStatus(Variable):
    value_type = bool
    label = "removed individual's status"
    definition_period = YEAR

    def formula(person, period, parameters):
        # Not implemented due to missing information on parameters used in formula 3
        pass
