"""SR 711.4 Art. 4

Generated from: ch/711/de/711.4.md

Infrastructure surcharge or effective workplace costs.
- If presidency/secretary use own infrastructure: +60% surcharge on hourly rate
- Otherwise: effective costs are reimbursed
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class schaetzungskommission_eigene_infrastruktur(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Nutzt eigene Infrastruktur fuer Kommissionstaetigkeit"
    reference = "SR 711.4 Art. 4 Abs. 1"
    default_value = True


class schaetzungskommission_effektive_arbeitsplatzkosten(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Effektive Arbeitsplatzkosten wenn keine eigene Infrastruktur (CHF)"
    reference = "SR 711.4 Art. 4 Abs. 3"


class schaetzungskommission_infrastrukturzuschlag(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Infrastrukturzuschlag oder effektive Arbeitsplatzkosten (CHF)"
    reference = "SR 711.4 Art. 4"

    def formula(person, period, parameters):
        rolle = person('schaetzungskommission_rolle', period)
        eigene_infra = person('schaetzungskommission_eigene_infrastruktur', period)
        entschaedigung = person('schaetzungskommission_entschaedigung', period)
        effektive_kosten = person('schaetzungskommission_effektive_arbeitsplatzkosten', period)

        # Art. 4 Abs. 1: only presidency (1) and secretary (3) eligible
        ist_berechtigt = (rolle == 1) + (rolle == 3)

        # Art. 4 Abs. 1: 60% surcharge when using own infrastructure
        zuschlag = where(eigene_infra, entschaedigung * 0.60, effektive_kosten)

        return where(ist_berechtigt, zuschlag, 0.0)
