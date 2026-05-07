"""SR 0.103.2 Art. 30

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

This article does not describe a monetary or quantifiable variable, but rather a process and a timeline. Therefore, we cannot create an OpenFisca variable directly from this article.

However, let's create a simple variable that captures some essential information from the article.

class _next_election_year(Variable):
    value_type = int
    entity = None
    definition_period = YEAR
    label = "Year when the next election should take place, according to Art. 30 SR 0.103.2"

    def formula(s, period, parameters):
        year_since_effective_date = (period.date - parameters(period).general.next_effective_date).days / 365.25
        first_election_year = int(period.start_date.year) + int(6 * year_since_effective_date)
        election_interval = 5  # Since Paragraph 2 describes a process every (every 5 intervals or approximately every 5 years)
        return first_election_year + (election_interval * (period.year - first_election_year) // election_interval) + (1 if (election_interval * (period.year - first_election_year) % election_interval != 0) else 0)
