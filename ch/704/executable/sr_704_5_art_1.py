"""SR 704.5 Art. 1

Generated from: ch/704/de/704.5.md

Beschwerdeberechtigte Fachorganisationen: Lists the organizations entitled
to file appeals: ARF, SAW, NFS, SAC, SHS, VCS.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_beschwerdeberechtigte_fachorganisationen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl beschwerdeberechtigte Fachorganisationen fuer Fuss- und Wanderwege"
    reference = "SR 704.5 Art. 1"

    def formula(person, period, parameters):
        return 6  # ARF, SAW, NFS, SAC, SHS, VCS
