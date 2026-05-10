"""SR 748.0 Art. 1

Generated from: ch/748/de/748.0.md

Art. 1: Grundsatz und Definitionen - Use of Swiss airspace:
- Aircraft: devices that can stay in the atmosphere through air effects
  (excluding ground-effect/hovercraft)
- Flying objects (Flugkörper): flight devices that are not aircraft
- Air navigation services: services ensuring safe, orderly, fluid air traffic
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lfg_ist_luftfahrzeug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fluggerät ist ein Luftfahrzeug (hält sich durch Einwirkung der Luft in der Atmosphäre)"
    reference = "SR 748.0 Art. 1 Abs. 2"


class lfg_ist_flugkoerper(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fluggerät ist ein Flugkörper (kein Luftfahrzeug)"
    reference = "SR 748.0 Art. 1 Abs. 3"


class lfg_benuetzung_luftraum_gestattet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Benützung des Luftraums über der Schweiz ist gestattet"
    reference = "SR 748.0 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        ist_lfz = person('lfg_ist_luftfahrzeug', period)
        ist_fk = person('lfg_ist_flugkoerper', period)
        # Both aircraft and flying objects may use Swiss airspace
        return ist_lfz + ist_fk > 0
