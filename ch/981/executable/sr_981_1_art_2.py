"""SR 981.1 Art. 2 - Kammern

Generated from: ch/981/de/981.1.md

Kammern von mindestens 3 Mitgliedern, beschlussfaehig nur bei
vollstaendiger Besetzung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class anzahl_kammermitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Mitglieder der Kammer"
    reference = "SR 981.1 Art. 2 Abs. 1"


class anzahl_anwesende_kammermitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl anwesende Kammermitglieder"
    reference = "SR 981.1 Art. 2 Abs. 2"


class kammer_beschlussfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Kammer ist beschlussfaehig (vollstaendige Besetzung)"
    reference = "SR 981.1 Art. 2 Abs. 2"

    def formula(self, period, parameters):
        total = self('anzahl_kammermitglieder', period)
        anwesend = self('anzahl_anwesende_kammermitglieder', period)
        return (anwesend >= total) * (total >= 3)
