"""SR 510.518 Art. 7 - Strafbestimmungen

Generated from: ch/510/de/510.518.md

Wer eine militaerische Anlage beschaedigt, zerstoert oder unbrauchbar macht,
oder den Bestimmungen der Art. 2-6 zuwiderhandelt, wird mit Freiheitsstrafe
bis zu drei Jahren oder Geldstrafe bestraft. In leichten Faellen erfolgt
disziplinarische Bestrafung. Die fahrlaessige Begehung ist strafbar.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_mil_anlage_beschaedigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine militaerische Anlage beschaedigt, zerstoert oder unbrauchbar gemacht hat"
    reference = "SR 510.518 Art. 7 Abs. 1"


class hat_schutzgesetz_zuwidergehandelt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person den Bestimmungen der Art. 2-6 oder sich darauf stuetzenden Erlassen zuwidergehandelt hat"
    reference = "SR 510.518 Art. 7 Abs. 1"


class ist_leichter_fall_510_518(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein leichter Fall im Sinne von Art. 7 Abs. 1 vorliegt"
    reference = "SR 510.518 Art. 7 Abs. 1"


class fahrlaessige_begehung_510_518(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Tat fahrlaessig begangen wurde"
    reference = "SR 510.518 Art. 7 Abs. 2"


class strafbar_nach_510_518(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person nach dem BG ueber den Schutz militaerischer Anlagen strafbar ist"
    reference = "SR 510.518 Art. 7"

    def formula(person, period, parameters):
        beschaedigt = person('hat_mil_anlage_beschaedigt', period)
        zuwidergehandelt = person('hat_schutzgesetz_zuwidergehandelt', period)
        fahrlaessig = person('fahrlaessige_begehung_510_518', period)
        return (beschaedigt + zuwidergehandelt + fahrlaessig) > 0


class max_freiheitsstrafe_jahre_510_518(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Freiheitsstrafe in Jahren bei Verstoss gegen das Schutzgesetz"
    reference = "SR 510.518 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return 3
