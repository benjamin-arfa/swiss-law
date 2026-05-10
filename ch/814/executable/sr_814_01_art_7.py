"""SR 814.01 Art. 7

Generated from: ch/fr/814/814.01.md

Art. 7: Definitions (Begriffsbestimmungen)
- Abs. 1: Atteintes = air pollution, noise, vibrations, rays, water pollution,
  soil impacts, genetic modifications.
- Abs. 2: Emissions (at source) vs Immissions (at point of impact).
- Abs. 3: Air pollution: modifications of natural air state.
- Abs. 6: Waste: movable things the holder disposes of.
- Abs. 7: Installations: buildings, roads, fixed structures. Tools, vehicles assimilated.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class usg_ist_anlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Objekt eine Anlage im Sinne des USG ist (Bauten, Verkehrswege, feste Einrichtungen)"
    reference = "SR 814.01 Art. 7 Abs. 7"


class usg_verursacht_luftverunreinigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Luftverunreinigungen verursacht werden"
    reference = "SR 814.01 Art. 7 Abs. 3"


class usg_verursacht_laerm(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Laerm oder Erschuetterungen verursacht werden"
    reference = "SR 814.01 Art. 7 Abs. 2, 4"


class usg_erzeugt_abfaelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Abfaelle erzeugt werden"
    reference = "SR 814.01 Art. 7 Abs. 6"


class usg_verursacht_einwirkungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob umweltrelevante Einwirkungen verursacht werden"
    reference = "SR 814.01 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        luft = person('usg_verursacht_luftverunreinigung', period)
        laerm = person('usg_verursacht_laerm', period)
        abfall = person('usg_erzeugt_abfaelle', period)
        return luft + laerm + abfall
