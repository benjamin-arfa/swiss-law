"""SR 642.118.2 Art. 8

Generated from: ch/642/de/642.118.2.md

Art. 8: Bundessteueranteil bei Grenzgaengern aus Deutschland -
Federal tax share is 10% of total withholding tax for German cross-border
commuters (tariff codes L, M, N, P, Q).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class quellensteuer_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Gesamter Quellensteuerabzug (CHF)"
    reference = "SR 642.118.2 Art. 2"


class quellensteuer_bundessteueranteil_grenzgaenger_de(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Anteil direkte Bundessteuer bei Grenzgaengern aus Deutschland (10% des Quellensteuerbetrags)"
    reference = "SR 642.118.2 Art. 8"

    def formula(person, period, parameters):
        tarifcode = person('quellensteuer_tarifcode', period.this_year)
        quellensteuer = person('quellensteuer_betrag', period)

        ist_de_grenzgaenger = (
            (tarifcode == 'L') + (tarifcode == 'M') +
            (tarifcode == 'N') + (tarifcode == 'P') +
            (tarifcode == 'Q')
        )

        # Art. 8: Bundessteueranteil betraegt 10 Prozent
        return where(ist_de_grenzgaenger, quellensteuer * 0.10, 0)
