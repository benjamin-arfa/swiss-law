"""SR 442.125 Art. 6

Generated from: ch/442/de/442.125.md

Foerderkriterien und Bemessung spartenueber. Finanzhilfen:
Max 70% der Kosten fuer Dienstleistungen und Vorhaben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kosten_spartenueber_dienstleistungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten fuer spartenueber. Dienstleistungen und Vorhaben (CHF)"
    reference = "SR 442.125 Art. 6 Abs. 2"


class max_spartenueber_finanzhilfe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale spartenueber. Finanzhilfe (max 70% Kosten)"
    reference = "SR 442.125 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        kosten = person('kosten_spartenueber_dienstleistungen', period)
        return kosten * 0.70
