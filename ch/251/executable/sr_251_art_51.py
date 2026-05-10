"""SR 251 Art. 51

Generated from: ch/de/251.md

Violations in connection with mergers: fine up to CHF 1 million
for failure to notify, breach of standstill obligation, or
non-compliance with conditions. Repeated violations: up to 10%
of combined Swiss turnover.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zusammenschluss_ohne_meldung_vollzogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein meldepflichtiger Zusammenschluss ohne Meldung vollzogen wurde"
    reference = "SR 251 Art. 51 Abs. 1"


class vollzugsverbot_missachtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das vorlaeufige Vollzugsverbot missachtet wurde"
    reference = "SR 251 Art. 51 Abs. 1"


class zusammenschluss_auflage_verstoss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob gegen eine Auflage zur Zulassung verstossen wurde"
    reference = "SR 251 Art. 51 Abs. 1"


class zusammenschluss_busse_max(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse fuer Verstoesse bei Zusammenschluessen (CHF)"
    reference = "SR 251 Art. 51 Abs. 1"

    def formula(person, period, parameters):
        verstoss = (
            person('zusammenschluss_ohne_meldung_vollzogen', period)
            + person('vollzugsverbot_missachtet', period)
            + person('zusammenschluss_auflage_verstoss', period)
        ) > 0
        return verstoss * 1000000.0
