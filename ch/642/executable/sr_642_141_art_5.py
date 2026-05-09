"""SR 642.141 Art. 5

Generated from: ch/642/de/642.141.md

Art. 5: Procedural obligations for replacement acquisition of
real estate in intercantonal relations
(Verfahrenspflichten bei Ersatzbeschaffung von Grundstuecken)

Abs. 1: For replacement acquisition of real estate per Art. 8(4),
12(3)(d)(e), and 24(4) StHG in another canton, the taxpayer must
provide the assessment authorities of all involved cantons with
information and documentation on the entire replacement process.

Abs. 2: The canton granting the replacement acquisition communicates
its decision to the assessment authority of the canton where the
replacement property is located.

Procedural article; no calculable formula.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class grundstueck_ersatzbeschaffung_interkantonal(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ersatzbeschaffung eines Grundstuecks in einem anderen Kanton"
    reference = "SR 642.141 Art. 5"
