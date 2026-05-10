"""SR 141.01 Art. 3

Generated from: ch/141/de/141.01.md

Bedrohung der inneren oder aeusseren Sicherheit der Schweiz: Eine konkrete
Bedrohung liegt vor bei Teilnahme an nachrichtendienstlich relevanten
Aktivitaeten oder organisierter Kriminalitaet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class teilnahme_nachrichtendienstliche_aktivitaeten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person an Aktivitaeten nach Art. 6 Abs. 1 Bst. a Ziff. 1-5 NDG teilnimmt, diese unterstuetzt oder foerdert"
    reference = "SR 141.01 Art. 3"


class teilnahme_organisierte_kriminalitaet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person an Aktivitaeten der organisierten Kriminalitaet teilnimmt"
    reference = "SR 141.01 Art. 3"


class bedrohung_sicherheit_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine konkrete Bedrohung der inneren oder aeusseren Sicherheit der Schweiz vorliegt"
    reference = "SR 141.01 Art. 3"

    def formula(person, period, parameters):
        ndg = person('teilnahme_nachrichtendienstliche_aktivitaeten', period)
        ok = person('teilnahme_organisierte_kriminalitaet', period)
        return ndg + ok > 0
