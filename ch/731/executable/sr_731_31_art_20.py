"""SR 731.31 Art. 20

Generated from: ch/731/de/731.31.md

Exceptions for systemically critical companies where cantons provide
equivalent measures.  Conditions for cantonal measures to qualify.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_kantonale_massnahmen_materiell(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kantonale Massnahmen sind materiell geeignet (Art. 20 Abs. 2)"
    reference = "SR 731.31 Art. 20 Abs. 2"


class firevo_kantonale_massnahmen_formell(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kantonale Massnahmen sind formell geeignet (Art. 20 Abs. 3)"
    reference = "SR 731.31 Art. 20 Abs. 3"


class firevo_kantonale_ausnahme(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen profitiert von kantonaler Ausnahmeregelung"
    reference = "SR 731.31 Art. 20 Abs. 1"

    def formula(person, period, parameters):
        """Art. 20 Abs. 1: If cantonal law provides materially and formally
        adequate measures, only Art. 1, 2, 20, 21, 23, 24 apply.
        """
        materiell = person('firevo_kantonale_massnahmen_materiell', period)
        formell = person('firevo_kantonale_massnahmen_formell', period)
        return materiell * formell
