"""SR 731.31 Art. 3

Generated from: ch/731/de/731.31.md

Subsidiary federal financial aid in the form of loans.
No legal entitlement to loans exists (Abs. 2).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_liquiditaetsengpass(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Liquiditaetsengpass infolge unvorhergesehener Entwicklungen"
    reference = "SR 731.31 Art. 3 Abs. 1"


class firevo_selbsthilfemassnahmen_getroffen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Unternehmen und Eigentuemer haben zumutbare Selbsthilfemassnahmen getroffen"
    reference = "SR 731.31 Art. 3 Abs. 1"


class firevo_darlehen_berechtigung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Erfuellt Voraussetzungen fuer subsidiaeere Finanzhilfe (kein Anspruch)"
    reference = "SR 731.31 Art. 3"

    def formula(person, period, parameters):
        """Art. 3 Abs. 1: Subsidiary loans may be granted if the company
        faces liquidity problems despite self-help measures.
        Note: Art. 3 Abs. 2 - no legal entitlement exists.
        """
        systemkritisch = person('firevo_ist_systemkritisch', period.this_year)
        engpass = person('firevo_liquiditaetsengpass', period)
        selbsthilfe = person('firevo_selbsthilfemassnahmen_getroffen', period)
        return systemkritisch * engpass * selbsthilfe
