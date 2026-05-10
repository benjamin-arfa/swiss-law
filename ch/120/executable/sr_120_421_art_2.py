"""SR 120.421 Art. 2

Generated from: ch/120/de/120.421.md

Aktualisierung der Anhaenge: Update of annexes at least every 5 years,
or within 6 months of changes to PSPV Annex 1.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pspv_bk_anhang_aktualisierung_intervall_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aktualisierungsintervall des PSPV-BK Anhangs in Jahren"
    reference = "SR 120.421 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return 5


class pspv_bk_anhang_aenderungsfrist_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer Anpassung nach Aenderung von Anhang 1 PSPV in Monaten"
    reference = "SR 120.421 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return 6
