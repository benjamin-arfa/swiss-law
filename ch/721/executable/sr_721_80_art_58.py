"""SR 721.80 Art. 58 & 58a

Generated from: ch/721/de/721.80.md

Art. 58 - Maximum concession duration: 80 years from start of operations.
Art. 58a - Concession renewal:
2. Renewal request must be filed at least 15 years before expiry.
   Authorities must decide on willingness to renew at least 10 years before expiry.
3. New residual water requirements apply fully at most 5 years after expiry.
4. Maximum duration of early-renewed concession runs from agreed effective date,
   which must be no later than 25 years after the concession decision.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wrg_konzession_startjahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Year of start of operations (Betriebseröffnung)"
    reference = "SR 721.80 Art. 58"


class wrg_konzession_ablaufjahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Year the concession expires"
    reference = "SR 721.80 Art. 58"

    def formula(person, period, parameters):
        startjahr = person('wrg_konzession_startjahr', period)
        max_dauer = parameters(period).sr_721_80.konzession_maximaldauer_jahre
        return startjahr + max_dauer


class wrg_erneuerung_gesuchsfrist_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Latest year by which renewal request must be filed"
    reference = "SR 721.80 Art. 58a Abs. 2"

    def formula(person, period, parameters):
        ablaufjahr = person('wrg_konzession_ablaufjahr', period)
        frist = parameters(period).sr_721_80.konzession_erneuerung_gesuchsfrist_jahre
        return ablaufjahr - frist


class wrg_erneuerung_entscheid_frist_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Latest year by which authorities must decide on renewal willingness"
    reference = "SR 721.80 Art. 58a Abs. 2"

    def formula(person, period, parameters):
        ablaufjahr = person('wrg_konzession_ablaufjahr', period)
        frist = parameters(period).sr_721_80.konzession_erneuerung_entscheid_frist_jahre
        return ablaufjahr - frist
