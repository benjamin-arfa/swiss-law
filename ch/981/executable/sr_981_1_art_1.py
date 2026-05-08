"""SR 981.1 Art. 1 - Zusammensetzung

Generated from: ch/981/de/981.1.md

Kommission fuer auslaendische Entschaedigungen: 5–15 Mitglieder,
beschlussfaehig bei mindestens Haelfte (min. 3) anwesend.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class anzahl_kommissionsmitglieder_981(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der Kommission fuer auslaendische Entschaedigungen"
    reference = "SR 981.1 Art. 1 Abs. 2"


class anzahl_anwesende_mitglieder_981(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl anwesende Mitglieder bei der Sitzung"
    reference = "SR 981.1 Art. 1 Abs. 3"


class kommission_beschlussfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Kommission ist beschlussfaehig"
    reference = "SR 981.1 Art. 1 Abs. 3"

    def formula(self, period, parameters):
        total = self('anzahl_kommissionsmitglieder_981', period.this_year)
        anwesend = self('anzahl_anwesende_mitglieder_981', period)
        haelfte = total / 2
        return (anwesend >= haelfte) * (anwesend >= 3)
