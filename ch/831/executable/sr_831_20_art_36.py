"""SR 831.20 Art. 36

Generated from: ch/831/de/831.20.md

Art. 36: Bezügerkreis und Berechnung
- Abs. 1: Entitlement to an ordinary pension requires at least 3 years of
  contributions at the onset of disability.
- Abs. 2: Calculation follows AHV rules (AHVG) by analogy.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_beitragsjahre_bei_invaliditaet(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Beitragsjahre bei Eintritt der Invaliditaet"
    reference = "SR 831.20 Art. 36 Abs. 1"


class iv_anspruch_ordentliche_rente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf ordentliche IV-Rente (mindestens 3 Beitragsjahre)"
    reference = "SR 831.20 Art. 36 Abs. 1"

    def formula(person, period, parameters):
        beitragsjahre = person('iv_beitragsjahre_bei_invaliditaet', period)
        return beitragsjahre >= 3
