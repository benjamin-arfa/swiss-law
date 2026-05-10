"""SR 734.0 Art. 2

Generated from: ch/734/de/734.0.md

Art. 2: Definitionen Schwachstrom / Starkstrom
- Abs. 1: Schwachstromanlagen = Anlagen, bei welchen normalerweise keine
  Stroeme auftreten koennen, die fuer Personen oder Sachen gefaehrlich sind.
- Abs. 2: Starkstromanlagen = Anlagen, bei welchen Stroeme benuetzt werden
  oder auftreten, die unter Umstaenden fuer Personen oder Sachen gefaehrlich sind.
- Abs. 3: Bei Zweifel entscheidet das UVEK endgueltig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eleg_anlage_ist_schwachstrom(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Anlage gilt als Schwachstromanlage "
        "(normalerweise keine gefaehrlichen Stroeme)"
    )
    reference = "SR 734.0 Art. 2 Abs. 1"


class eleg_anlage_ist_starkstrom(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Anlage gilt als Starkstromanlage "
        "(Stroeme die unter Umstaenden fuer Personen oder Sachen gefaehrlich sind)"
    )
    reference = "SR 734.0 Art. 2 Abs. 2"


class eleg_anlage_klassifikation(Variable):
    """0 = unbekannt, 1 = Schwachstrom, 2 = Starkstrom"""
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Klassifikation der elektrischen Anlage (1=Schwachstrom, 2=Starkstrom)"
    reference = "SR 734.0 Art. 2"

    def formula(person, period, parameters):
        schwach = person('eleg_anlage_ist_schwachstrom', period)
        stark = person('eleg_anlage_ist_starkstrom', period)
        return select(
            [stark, schwach],
            [2, 1],
            default=0,
        )
