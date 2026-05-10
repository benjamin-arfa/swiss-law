"""SR 814.01 Art. 13-15

Generated from: ch/fr/814/814.01.md

Art. 13: Valeurs limites d'immissions (Immissionsgrenzwerte)
- Abs. 1: Federal Council sets immission limit values by ordinance.
- Abs. 2: Must consider particularly sensitive groups (children, sick, elderly, pregnant).
Art. 14: Air pollution limits - must not threaten humans, animals, plants, buildings, soil.
Art. 15: Noise/vibration limits - must not significantly disturb well-being.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class usg_immissionswert_luft_aktuell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Aktuelle Luftimmissionswerte am Standort (Index)"
    reference = "SR 814.01 Art. 14"


class usg_immissionsgrenzwert_luft(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Geltender Immissionsgrenzwert fuer Luftverunreinigungen"
    reference = "SR 814.01 Art. 13-14"


class usg_immissionswert_laerm_db(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Aktuelle Laermimmission am Standort in dB(A)"
    reference = "SR 814.01 Art. 15"


class usg_immissionsgrenzwert_laerm_db(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Geltender Immissionsgrenzwert fuer Laerm in dB(A)"
    reference = "SR 814.01 Art. 15"


class usg_immissionsgrenzwert_luft_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Immissionsgrenzwert fuer Luft eingehalten ist"
    reference = "SR 814.01 Art. 13-14"

    def formula(person, period, parameters):
        aktuell = person('usg_immissionswert_luft_aktuell', period)
        grenzwert = person('usg_immissionsgrenzwert_luft', period)
        return aktuell <= grenzwert


class usg_immissionsgrenzwert_laerm_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Immissionsgrenzwert fuer Laerm eingehalten ist"
    reference = "SR 814.01 Art. 15"

    def formula(person, period, parameters):
        aktuell = person('usg_immissionswert_laerm_db', period)
        grenzwert = person('usg_immissionsgrenzwert_laerm_db', period)
        return aktuell <= grenzwert
