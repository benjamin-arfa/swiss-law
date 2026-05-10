"""SR 170.32 Art. 2

Generated from: ch/170/de/170.32.md

Allgemeine Bestimmungen: Beamtenvorschriften gelten auch für übrige Personen.
Immunitätsregel für Bundesrat/Bundeskanzler bei Parlamentsvoten.

Skipped: Largely procedural/declaratory. Art. 2 Abs. 1 extends scope (already
covered in Art. 1). Art. 2 Abs. 2 is an immunity rule not directly computable.
Art. 2 Abs. 3 is a reservation clause.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_parlamentarische_immunitaet_voten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat Immunität für Voten in der Bundesversammlung (Art. 2 Abs. 2 VG)"
    reference = "SR 170.32, Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_bundesratsmitglied', period)
