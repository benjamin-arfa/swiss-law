"""SR 251 Art. 49a

Generated from: ch/de/251.md

Administrative sanctions for inadmissible competition restraints:
fine up to 10% of Swiss turnover over the last 3 years.
Self-reporting and cooperation can reduce or eliminate the fine.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class umsatz_schweiz_letzte_3_jahre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "In der Schweiz erzielter Umsatz der letzten 3 Geschaeftsjahre (CHF)"
    reference = "SR 251 Art. 49a Abs. 1"


class mitwirkung_aufdeckung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen bei Aufdeckung und Beseitigung mitwirkt"
    reference = "SR 251 Art. 49a Abs. 2"


class selbstanzeige_vor_wirkung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen die Wettbewerbsbeschraenkung meldet bevor sie Wirkung entfaltet"
    reference = "SR 251 Art. 49a Abs. 3 Bst. a"


class beschraenkung_seit_5_jahren_nicht_ausgeuebt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Wettbewerbsbeschraenkung seit mehr als 5 Jahren nicht mehr ausgeuebt wird"
    reference = "SR 251 Art. 49a Abs. 3 Bst. b"


class sanktion_max_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Sanktionsbetrag (10% des CH-Umsatzes der letzten 3 Jahre)"
    reference = "SR 251 Art. 49a Abs. 1"

    def formula(person, period, parameters):
        umsatz = person('umsatz_schweiz_letzte_3_jahre', period)
        return umsatz * 0.10


class sanktion_entfaellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sanktion entfaellt"
    reference = "SR 251 Art. 49a Abs. 3"

    def formula(person, period, parameters):
        return (
            person('selbstanzeige_vor_wirkung', period)
            + person('beschraenkung_seit_5_jahren_nicht_ausgeuebt', period)
        ) > 0
