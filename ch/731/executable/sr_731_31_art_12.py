"""SR 731.31 Art. 12

Generated from: ch/731/de/731.31.md

Subordination (Nachrangigkeit).
If the loan claim is declared subordinate, the risk surcharge increases
by at least 1 percentage point; maximum 10%.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_nachrangig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Darlehensforderung wurde als nachrangig erklaert"
    reference = "SR 731.31 Art. 12 Abs. 1"


class firevo_risikozuschlag_mit_nachrang(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Risikozuschlag bei Nachrangigkeit (Anteil)"
    reference = "SR 731.31 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        """Art. 12 Abs. 2: When subordinated, risk surcharge increases by
        at least 1 percentage point; never above 10%.
        """
        basis_satz = person('firevo_risikozuschlag_satz', period)
        nachrangig = person('firevo_nachrangig', period)

        erhoehung = 0.01  # at least 1 percentage point
        maximum = 0.10    # never above 10%

        erhoehter_satz = min_(basis_satz + erhoehung, maximum)

        return where(nachrangig, erhoehter_satz, basis_satz)
