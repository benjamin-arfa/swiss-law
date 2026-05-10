"""SR 235.1 Art. 35

Generated from: ch/235/de/235.1.md

Verletzung der beruflichen Schweigepflicht.
Strafbestimmung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_geheime_daten_unbefugt_bekanntgegeben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Geheime besonders schuetzenswerte Daten/Profile vorsaetzlich unbefugt bekannt gegeben"
    reference = "SR 235.1 Art. 35 Abs. 1"


class dsg_kenntnis_bei_berufsausuebung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kenntnis der Daten bei Berufsausuebung/Taetigkeit/Ausbildung erlangt"
    reference = "SR 235.1 Art. 35 Abs. 1-2"


class dsg_strafbar_art35(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Strafbarkeit wegen Verletzung der beruflichen Schweigepflicht (Busse, auf Antrag)"
    reference = "SR 235.1 Art. 35"

    def formula(person, period, parameters):
        unbefugt = person('dsg_geheime_daten_unbefugt_bekanntgegeben', period)
        beruf = person('dsg_kenntnis_bei_berufsausuebung', period)
        return unbefugt * beruf
