"""SR 834.1 Art. 6

Generated from: ch/834/de/834.1.md

Kinderzulagen:
- Abs. 1: Dienstleistende haben Anspruch fuer jedes Kind unter 18 Jahren.
  Fuer Kinder in Ausbildung bis zum vollendeten 25. Altersjahr.
- Abs. 2: Anspruch fuer eigene Kinder und unentgeltliche Pflegekinder.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eo_anzahl_kinder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl anspruchsberechtigte Kinder (unter 18, oder in Ausbildung bis 25)"
    reference = "SR 834.1 Art. 6 Abs. 1"


class eo_kinderzulage_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Kinderzulagen nach Art. 6 EOG"
    reference = "SR 834.1 Art. 6"

    def formula_2005(person, period, parameters):
        ist_dienstleistend = person('eo_ist_dienstleistend', period)
        anzahl_kinder = person('eo_anzahl_kinder', period)
        return ist_dienstleistend * (anzahl_kinder > 0)
