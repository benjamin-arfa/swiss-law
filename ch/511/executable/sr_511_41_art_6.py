"""SR 511.41 Art. 6 – Unverschuldete finanzielle Notlage

Generated from: ch/511/de/511.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class in_unverschuldeter_finanzieller_notlage(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person befindet sich nachweislich in unverschuldeter finanzieller Notlage"
    reference = "SR 511.41 Art. 6 Abs. 1"
    default_value = False


class ratenzahlung_bewilligt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ratenweise Bezahlung der Ausbildungskosten bewilligt"
    reference = "SR 511.41 Art. 6 Abs. 1"
    default_value = False


class teilweiser_erlass_bewilligt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Teilweiser Erlass der Ausbildungskosten bewilligt"
    reference = "SR 511.41 Art. 6 Abs. 1"
    default_value = False


class zahlungsfrist_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zahlungsfrist von 90 Tagen (Art. 4 Abs. 2) ist anwendbar"
    reference = "SR 511.41 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        # Art. 6 Abs. 2: Bei Ratenzahlung kommt die 90-Tage-Frist nicht zur Anwendung
        ratenzahlung = person('ratenzahlung_bewilligt', period)
        return not_(ratenzahlung)
