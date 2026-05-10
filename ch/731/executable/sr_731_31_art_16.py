"""SR 731.31 Art. 16

Generated from: ch/731/de/731.31.md

Cantonal share of loan losses and risk surcharges.
- Cantons reimburse 50% of definitive losses (plus interest & surcharges)
- 50% of risk surcharges collected by the Confederation are passed to cantons
- Distribution among cantons based on their share of 2020 GDP
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_darlehensverlust(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Definitiver Verlust auf Darlehen (CHF)"
    reference = "SR 731.31 Art. 16 Abs. 1"


class firevo_kantonsanteil_verlust(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kantonsanteil an Darlehensverlusten (CHF)"
    reference = "SR 731.31 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        """Art. 16 Abs. 1: Cantons reimburse 50% of definitive losses."""
        verlust = person('firevo_darlehensverlust', period)
        return verlust * 0.50


class firevo_risikozuschlag_vereinnahmt(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Vom Bund vereinnahmte Risikozuschlaege (CHF)"
    reference = "SR 731.31 Art. 16 Abs. 2"


class firevo_kantonsanteil_risikozuschlag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "An Kantone weitergeleitete Risikozuschlaege (CHF)"
    reference = "SR 731.31 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        """Art. 16 Abs. 2: 50% of collected risk surcharges go to cantons."""
        zuschlag = person('firevo_risikozuschlag_vereinnahmt', period)
        return zuschlag * 0.50
