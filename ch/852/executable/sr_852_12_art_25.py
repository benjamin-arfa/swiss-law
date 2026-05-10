"""SR 852.12 Art. 25

Generated from: ch/852/fr/852.12.md

Art. 25: Logging requirements:
- al. 1: All access and modifications are logged continuously.
- al. 2: Logs are kept for 1 year, stored separately from the system
  containing personal data.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class edassist_duree_conservation_journaux(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duration for which access logs must be kept (years)"
    reference = "SR 852.12 Art. 25 al. 2"

    def formula(person, period, parameters):
        return parameters(period).sr_852_12.duree_conservation_journaux
