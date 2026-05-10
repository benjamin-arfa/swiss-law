"""SR 731.31 Art. 11

Generated from: ch/731/de/731.31.md

Securities (Sicherheiten).
If adequate securities are provided, risk surcharge is reduced by at
least 1 percentage point; minimum 4%.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_sicherheiten_bestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angemessene Sicherheiten wurden bestellt"
    reference = "SR 731.31 Art. 11 Abs. 3"


class firevo_risikozuschlag_mit_sicherheiten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Risikozuschlag nach Abzug fuer Sicherheiten (Anteil)"
    reference = "SR 731.31 Art. 11 Abs. 3"

    def formula(person, period, parameters):
        """Art. 11 Abs. 3: With adequate securities, risk surcharge is
        reduced by at least 1 percentage point; never below 4%.
        """
        basis_satz = person('firevo_risikozuschlag_satz', period)
        sicherheiten = person('firevo_sicherheiten_bestellt', period)

        reduktion = 0.01  # at least 1 percentage point
        minimum = 0.04    # never below 4%

        reduzierter_satz = max_(basis_satz - reduktion, minimum)

        return where(sicherheiten, reduzierter_satz, basis_satz)
