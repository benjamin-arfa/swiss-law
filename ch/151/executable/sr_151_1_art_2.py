"""SR 151.1 Art. 2

Generated from: ch/151/de/151.1.md

Grundsatz: Dieser Abschnitt gilt fuer Arbeitsverhaeltnisse nach OR
sowie fuer alle oeffentlich-rechtlichen Arbeitsverhaeltnisse.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_arbeitsverhaeltnis_nach_or(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Arbeitsverhaeltnis nach Obligationenrecht vorliegt"
    reference = "SR 151.1 Art. 2"


class ist_oeffentlich_rechtliches_arbeitsverhaeltnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein oeffentlich-rechtliches Arbeitsverhaeltnis vorliegt"
    reference = "SR 151.1 Art. 2"


class glg_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gleichstellungsgesetz (Abschnitt 2) anwendbar ist"
    reference = "SR 151.1 Art. 2"

    def formula(person, period, parameters):
        or_verhaeltnis = person('ist_arbeitsverhaeltnis_nach_or', period)
        oer_verhaeltnis = person('ist_oeffentlich_rechtliches_arbeitsverhaeltnis', period)
        return or_verhaeltnis + oer_verhaeltnis > 0
