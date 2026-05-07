"""SR 702.1 Art. 9

Generated from: ch/702/de/702.1.md

Sistierung nach Art. 14 Abs. 1 lit. b des Gesetzes:
Suspension max 2 years, renewable if conditions still met.
Owner must prove advertising, market conditions, and availability.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class sistierung_art14b_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Dauer der Sistierung nach Art. 14 Abs. 1 lit. b in Jahren"
    reference = "SR 702.1 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return 2  # hoechstens zwei Jahre


class nachweis_regelmaessige_inserate(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob regelmaessig Inserate auf marktuebliche Art erschienen sind"
    reference = "SR 702.1 Art. 9 Abs. 2 lit. a"


class nachweis_marktuebliche_bedingungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Wohnung zu markt- und ortsueblichen Bedingungen ausgeschrieben wurde"
    reference = "SR 702.1 Art. 9 Abs. 2 lit. b"


class nachweis_bezugsbereitschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Wohnung jederzeit bezugsbereit gewesen ist"
    reference = "SR 702.1 Art. 9 Abs. 2 lit. c"


class sistierung_art14b_nachweis_erbracht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Nachweis fuer die Sistierung nach Art. 14 Abs. 1 lit. b erbracht ist"
    reference = "SR 702.1 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('nachweis_regelmaessige_inserate', period) *
            person('nachweis_marktuebliche_bedingungen', period) *
            person('nachweis_bezugsbereitschaft', period)
        )


class sistierung_art14b_verlaengerung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verlaengerung der Sistierung zulaessig ist"
    reference = "SR 702.1 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return person('sistierung_art14b_nachweis_erbracht', period)
