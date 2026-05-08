"""SR 711.4 Art. 5

Generated from: ch/711/de/711.4.md

Expenses (Auslagen) for members of the valuation commissions.
Presidency: all expense types; other members and secretary: travel only.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class schaetzungskommission_reisekosten(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Dienstreisekosten (Verpflegung, Uebernachtung, Fahrt) nach Bundespersonal-Ansaetzen (CHF)"
    reference = "SR 711.4 Art. 5 Abs. 2 lit. a, Abs. 3"


class schaetzungskommission_hilfskraefte_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Kosten fuer beigezogene Hilfskraefte und Sachverstaendige (CHF)"
    reference = "SR 711.4 Art. 5 Abs. 2 lit. b, Abs. 4"


class schaetzungskommission_ausserordentliche_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Ausserordentliche Zusatzkosten (Buero, Archiv, Informatik) (CHF)"
    reference = "SR 711.4 Art. 5 Abs. 2 lit. c"


class schaetzungskommission_auslagen_total(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Total erstattungsfaehige Auslagen (CHF)"
    reference = "SR 711.4 Art. 5"

    def formula(person, period, parameters):
        rolle = person('schaetzungskommission_rolle', period)
        reise = person('schaetzungskommission_reisekosten', period)
        hilfs = person('schaetzungskommission_hilfskraefte_kosten', period)
        extra = person('schaetzungskommission_ausserordentliche_kosten', period)

        # Art. 5 Abs. 1: presidency gets all expense types (a, b, c)
        # Other members and secretary only get travel costs (a)
        ist_praesidium = (rolle == 1)

        return where(ist_praesidium,
                     reise + hilfs + extra,
                     reise)
