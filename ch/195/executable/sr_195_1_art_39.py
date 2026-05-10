"""SR 195.1 Art. 39

Generated from: ch/195/de/195.1.md

Natuerliche Personen: Voraussetzungen fuer konsularischen Schutz.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class haelt_sich_im_ausland_auf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die Person im Ausland aufhaelt"
    reference = "SR 195.1 Art. 39 Abs. 1 lit. a"


class schweiz_uebernimmt_schutzfunktion(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schweiz Schutzfunktionen fuer die Person uebernimmt"
    reference = "SR 195.1 Art. 39 Abs. 1 lit. b"


class anderer_staat_leistet_bereits_unterstuetzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein anderer Staat bereits Unterstuetzung leistet"
    reference = "SR 195.1 Art. 39 Abs. 2"


class hat_staatsangehoerigkeit_empfangsstaat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person auch die Staatsangehoerigkeit des Empfangsstaates besitzt"
    reference = "SR 195.1 Art. 39 Abs. 3"


class empfangsstaat_widersetzt_sich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich der Empfangsstaat dem konsularischen Schutz widersetzt"
    reference = "SR 195.1 Art. 39 Abs. 3"


class konsularischer_schutz_natuerliche_person_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob konsularischer Schutz fuer die natuerliche Person moeglich ist"
    reference = "SR 195.1 Art. 39"

    def formula(person, period, parameters):
        schweizer = person('ist_schweizer_staatsangehoeriger', period)
        im_ausland = person('haelt_sich_im_ausland_auf', period)
        schutzfunktion = person('schweiz_uebernimmt_schutzfunktion', period)
        anderer_staat = person('anderer_staat_leistet_bereits_unterstuetzung', period)
        empfangsstaat_nat = person('hat_staatsangehoerigkeit_empfangsstaat', period)
        widerstand = person('empfangsstaat_widersetzt_sich', period)

        # Abs. 1: Auslandschweizer oder Schutzpersonen
        grundanspruch = (schweizer * im_ausland) + schutzfunktion > 0
        # Abs. 2: Nicht wenn anderer Staat schon hilft (bei Mehrfachstaatlern)
        nicht_anderer_staat = 1 - (person('hat_mehrfache_staatsangehoerigkeit', period) * anderer_staat)
        # Abs. 3: Bei Staatsangehoerigkeit des Empfangsstaats nur wenn dieser sich nicht widersetzt
        nicht_widerstand = 1 - (empfangsstaat_nat * widerstand)

        return grundanspruch * nicht_anderer_staat * nicht_widerstand
