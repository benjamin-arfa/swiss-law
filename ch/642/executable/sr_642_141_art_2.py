"""SR 642.141 Art. 2

Generated from: ch/642/de/642.141.md

Art. 2: Persons taxable in multiple cantons
(In mehreren Kantonen steuerpflichtige Personen)

Abs. 1: If economic affiliation creates tax liability in cantons other
than the domicile/seat canton, an assessment procedure is also conducted
in those cantons.

Abs. 2: Persons taxable in multiple cantons can fulfill their tax
return obligation by submitting a copy of the domicile/seat canton's
return.

Abs. 3: The domicile/seat canton's tax authority communicates its
assessment including intercantonal tax allocation and deviations
to the other cantons' authorities free of charge.

Abs. 4: Procedure follows the respective cantonal procedural law.

Procedural article; no calculable formula.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class steuerpflicht_mehrere_kantone(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist in mehreren Kantonen steuerpflichtig"
    reference = "SR 642.141 Art. 2 Abs. 1"
