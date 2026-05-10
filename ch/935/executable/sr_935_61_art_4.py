"""SR 935.61 Art. 4

Generated from: ch/935/de/935.61.md

Art. 4: Grundsatz der interkantonalen Freizügigkeit
- Anwältinnen und Anwälte, die in einem kantonalen Anwaltsregister eingetragen sind,
  können in der Schweiz ohne weitere Bewilligung Parteien vor Gerichtsbehörden vertreten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class anwalt_in_kantonalem_register_eingetragen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwältin/Anwalt ist in einem kantonalen Anwaltsregister eingetragen"
    reference = "SR 935.61 Art. 4"


class anwalt_interkantonale_freizuegigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Anwältin/Anwalt kann in der Schweiz ohne weitere Bewilligung "
        "Parteien vor Gerichtsbehörden vertreten (interkantonale Freizügigkeit)"
    )
    reference = "SR 935.61 Art. 4"

    def formula(person, period, parameters):
        return person('anwalt_in_kantonalem_register_eingetragen', period)
