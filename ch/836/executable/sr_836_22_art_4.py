"""SR 836.22 Art. 4

Generated from: ch/836/de/836.22.md

Art. 4: Geografische Abdeckung.
Eine Familienorganisation gilt als in der ganzen Schweiz taetig,
wenn sich ihr Angebot an Familien in mindestens drei der vier
Sprachregionen richtet und sie in diesen Sprachregionen ueber
ein aehnlich breites Angebot verfuegt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class anzahl_sprachregionen_abgedeckt(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Sprachregionen, in denen die Organisation ein Angebot hat"
    reference = "SR 836.22 Art. 4"


class aehnlich_breites_angebot_in_regionen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation verfuegt in den abgedeckten Sprachregionen ueber ein aehnlich breites Angebot"
    reference = "SR 836.22 Art. 4"


class gilt_als_gesamtschweizerisch_taetig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation gilt als in der ganzen Schweiz taetig (Art. 4 FOrgV)"
    reference = "SR 836.22 Art. 4"

    def formula(person, period, parameters):
        regionen = person('anzahl_sprachregionen_abgedeckt', period)
        breites_angebot = person('aehnlich_breites_angebot_in_regionen', period)
        # Mindestens 3 von 4 Sprachregionen mit aehnlich breitem Angebot
        return (regionen >= 3) * breites_angebot
