"""SR 981 Art. 13

Generated from: ch/de/981.md

Transitional provision: tasks of the commission and appeals commission
for wartime aid to Swiss abroad transfer to the Commission for
Foreign Compensations (now: Federal Administrative Court).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aufgaben_kriegsgeschaedigte_uebertragen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Aufgaben der Kommission fuer kriegsgeschaedigte Auslandschweizer an die Kommission fuer auslaendische Entschaedigungen uebergegangen sind"
    reference = "SR 981 Art. 13"

    def formula(person, period, parameters):
        return True
