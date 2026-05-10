"""SR 142.209 Art. 13

Generated from: ch/142/de/142.209.md

Gebuehrenfreie Visumerteilung fuer bestimmte Personengruppen:
Kinder unter 6, offizielle Missionen, Diplomaten, Studierende,
Forscher, Stipendiaten, Ehegatten von Schweizern, EU/EFTA-Familien, etc.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_kind_unter_6(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ein Kind unter 6 Jahren ist"
    reference = "SR 142.209 Art. 13 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return person('alter_visumantragsteller', period) < 6


class ist_offizielle_mission(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person sich in offizieller Mission in die Schweiz begibt"
    reference = "SR 142.209 Art. 13 Abs. 1 Bst. b"


class ist_inhaber_offizieller_pass(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Inhaber/in eines offiziellen Passes (Diplomaten-/Dienstpass) ist"
    reference = "SR 142.209 Art. 13 Abs. 1 Bst. c"


class ist_student_studienreise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Schueler/in oder Studierende/r auf Studienreise ist"
    reference = "SR 142.209 Art. 13 Abs. 1 Bst. d"


class ist_ehegatte_schweizer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person mit einer/einem Schweizer/in verheiratet ist oder in Partnerschaft lebt"
    reference = "SR 142.209 Art. 13 Abs. 1 Bst. l"


class ist_visum_gebuehrenfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Visum gebuehrenfrei erteilt wird"
    reference = "SR 142.209 Art. 13"

    def formula(person, period, parameters):
        return (
            person('ist_kind_unter_6', period)
            + person('ist_offizielle_mission', period)
            + person('ist_inhaber_offizieller_pass', period)
            + person('ist_student_studienreise', period)
            + person('ist_ehegatte_schweizer', period)
        ) > 0
