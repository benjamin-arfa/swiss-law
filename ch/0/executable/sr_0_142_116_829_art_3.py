"""SR 0.142.116.829 Art. 3

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from enum import Enum




class individual_type(str, Enum):
    serbian= "Serb"
    stateless = "Stateless"


class SerbAndStatelessRepatriationReq(Variable):
    value_type = bool
    entity = Person
    label = 'Repatriation request to Serbia for Person of Serb or Stateless nationality'
    definition_period = ETERNITY


    def formula(person, period, parameters):
        is_serbian_or_stateless = ((person("is_serbian", period)) | (person("is_stateless", period)))

        no_transit_only = person("passed_only_transit_of_international_airports_serbia", period) 
        in_ch = person("resides_in_switzerland", period)
        valid_visum = person("valid_visum_before_ent_2022", period)
        valid_visum_after_ent_2022 = person("valid_visum_after_ent_serbia_2022", period)

        if valid_visum & valid_visum_after_ent_2022 or valid_visum_before_ent_2022:
            is_repatriable = False

        elif (not is_serbian_or_stateless) or no_transit_only or in_ch & (~valid_visum): 
            is_repatriable = False
            
        else:
            is_repatriable = True

        return is_repatriable
