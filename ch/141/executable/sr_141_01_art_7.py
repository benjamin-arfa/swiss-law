"""SR 141.01 Art. 7

Generated from: ch/141/de/141.01.md

Teilnahme am Wirtschaftsleben oder am Erwerb von Bildung: Deckung der
Lebenshaltungskosten durch Einkommen/Vermoegen/Rechtsansprueche; oder
in Aus-/Weiterbildung. Kein Sozialhilfebezug in den letzten 3 Jahren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class deckt_lebenshaltungskosten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Lebenshaltungskosten und Unterhaltsverpflichtungen durch Einkommen, Vermoegen oder Rechtsansprueche gedeckt werden"
    reference = "SR 141.01 Art. 7 Abs. 1"


class in_aus_oder_weiterbildung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in Aus- oder Weiterbildung ist"
    reference = "SR 141.01 Art. 7 Abs. 2"


class sozialhilfe_bezug_letzte_3_jahre(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob in den drei Jahren vor Gesuchstellung oder waehrend des Verfahrens Sozialhilfe bezogen wurde"
    reference = "SR 141.01 Art. 7 Abs. 3"


class sozialhilfe_vollstaendig_zurueckerstattet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die bezogene Sozialhilfe vollstaendig zurueckerstattet wurde"
    reference = "SR 141.01 Art. 7 Abs. 3"


class teilnahme_wirtschaftsleben_oder_bildung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Teilnahme am Wirtschaftsleben oder am Erwerb von Bildung erfuellt ist"
    reference = "SR 141.01 Art. 7"

    def formula(person, period, parameters):
        wirtschaft_oder_bildung = (
            person('deckt_lebenshaltungskosten', period)
            + person('in_aus_oder_weiterbildung', period)
        ) > 0
        sozialhilfe = person('sozialhilfe_bezug_letzte_3_jahre', period)
        rueckerstattet = person('sozialhilfe_vollstaendig_zurueckerstattet', period)
        sozialhilfe_kein_hindernis = (1 - sozialhilfe) + rueckerstattet > 0
        return wirtschaft_oder_bildung * sozialhilfe_kein_hindernis
