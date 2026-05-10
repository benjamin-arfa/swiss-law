"""SR 322.1 Art. 5

Generated from: ch/322/de/322.1.md

Sachliche Zustaendigkeit: Die Militaergerichte beurteilen erstinstanzlich
die der Militaergerichtsbarkeit unterworfenen strafbaren Handlungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class handlung_unterliegt_militaergerichtsbarkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die strafbare Handlung der Militaergerichtsbarkeit unterworfen ist"
    reference = "SR 322.1 Art. 5"


class militaergericht_erstinstanzlich_zustaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Militaergericht erstinstanzlich zustaendig ist"
    reference = "SR 322.1 Art. 5"

    def formula_1979(person, period, parameters):
        return person('handlung_unterliegt_militaergerichtsbarkeit', period)
