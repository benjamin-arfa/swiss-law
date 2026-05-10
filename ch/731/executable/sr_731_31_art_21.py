"""SR 731.31 Art. 21

Generated from: ch/731/de/731.31.md

Insufficient cantonal liquidity assurances - if cantonal measures no longer
meet the requirements, all provisions apply after 10 days.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_kantonale_massnahmen_ungenuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kantonale Massnahmen erfuellen Anforderungen nicht mehr"
    reference = "SR 731.31 Art. 21"


class firevo_volle_anwendung_nach_frist(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Alle FiREVO-Bestimmungen anwendbar (10 Tage nach Ungenuegenheit)"
    reference = "SR 731.31 Art. 21"

    def formula(person, period, parameters):
        """Art. 21: Full application after 10 days if cantonal measures fail."""
        ungenuegend = person('firevo_kantonale_massnahmen_ungenuegend', period)
        ausnahme = person('firevo_kantonale_ausnahme', period.this_year)
        return ungenuegend * ausnahme
