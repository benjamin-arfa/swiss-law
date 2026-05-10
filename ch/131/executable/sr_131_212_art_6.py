"""SR 131.212 Art. 6

Generated from: ch/131/de/131.212.md

Sprachen: German and French are the official languages of Canton Bern.
Defines which administrative regions use which languages.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verwaltungsregion(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Verwaltungsregion im Kanton Bern"
    reference = "SR 131.212 Art. 6"


class amtssprache_bern(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Amtssprache(n) in der jeweiligen Verwaltungsregion"
    reference = "SR 131.212 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        region = person('verwaltungsregion', period)
        # Berner Jura: French
        # Seeland/Biel: German and French
        # Others: German
        return np.where(
            region == 'berner_jura', 'franzoesisch',
            np.where(
                np.isin(region, ['seeland', 'biel_bienne']),
                'deutsch_franzoesisch',
                'deutsch'
            )
        )
