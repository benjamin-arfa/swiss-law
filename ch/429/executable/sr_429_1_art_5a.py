"""SR 429.1 Art. 5a

Generated from: ch/429/de/429.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 5a - Beitraege fuer Beteiligungen an internationalen Programmen
# Der Bund kann Beitraege gewaehren fuer die Beteiligung an internationalen Programmen.

# --- Input variables ---

class bewilligter_kredit_meteo_international(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bewilligter Kredit fuer internationale Meteorologie-Programme in CHF"
    reference = "SR 429.1 Art. 5a Abs. 1"


class beantragter_beitrag_meteo_international(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Beantragter Beitrag fuer internationale Meteorologie-Beteiligung in CHF"
    reference = "SR 429.1 Art. 5a Abs. 1"


# --- Computed variables ---

class beitrag_meteo_international_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beitrag fuer internationale Beteiligung ist im Rahmen der bewilligten Kredite zulaessig (Art. 5a Abs. 1 MetG)"
    reference = "SR 429.1 Art. 5a Abs. 1"

    def formula(self, period, parameters):
        beantragt = self('beantragter_beitrag_meteo_international', period)
        kredit = self('bewilligter_kredit_meteo_international', period)
        return beantragt <= kredit
