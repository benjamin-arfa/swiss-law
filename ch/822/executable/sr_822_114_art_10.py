"""SR 822.114 Art. 10 - Türen und Ausgänge in Fluchtwegen (Doors in escape routes)

ArGV 4 - Minimum door widths in escape routes.
Art. 10 Abs. 2:
  - Single-leaf doors: min 0.90 m clear width
  - Double-leaf doors (one direction): one leaf min 0.90 m
  - Double-leaf swing doors: each leaf min 0.65 m

Generated from: ch/822/de/822.114.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class argv4_tuer_typ(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Door type: 1=single-leaf, 2=double-leaf one-direction, 3=double-leaf swing (SR 822.114 Art. 10)"
    reference = "SR 822.114 Art. 10"
    default_value = 1


class argv4_min_tuerbreite(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum clear door width in meters (SR 822.114 Art. 10 Abs. 2)"
    reference = "SR 822.114 Art. 10"

    def formula(person, period, parameters):
        typ = person("argv4_tuer_typ", period)
        # Type 1 (single-leaf): 0.90 m
        # Type 2 (double-leaf, one direction): 0.90 m (one leaf)
        # Type 3 (double-leaf swing): 0.65 m (each leaf)
        return where(typ == 3, 0.65, 0.90)
