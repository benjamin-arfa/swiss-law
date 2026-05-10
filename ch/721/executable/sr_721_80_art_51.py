"""SR 721.80 Art. 51

Generated from: ch/721/de/721.80.md

Art. 51 - Calculation of gross capacity for Wasserzins:
1. The gross capacity relevant for Wasserzins is the mean mechanical gross
   capacity of the water, calculated from usable head and water volumes.
2. Usable head = height difference between water intake and return point.
3. Usable water volumes = actually inflowing volumes, insofar as they do not
   exceed the capacity of the concession-approved installations.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Physical constant: water density * gravity = 9810 N/m3
WASSER_SPEZIFISCHES_GEWICHT = 9810  # N/m3


class wrg_nutzbares_gefaelle_m(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Usable head (height difference between intake and return point) in meters"
    reference = "SR 721.80 Art. 51 Abs. 2"


class wrg_nutzbare_wassermenge_m3s(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mean usable water volume (m3/s), capped at installation capacity"
    reference = "SR 721.80 Art. 51 Abs. 3"


class wrg_bruttoleistung_berechnet_kw(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Calculated mean mechanical gross capacity of water (kW)"
    reference = "SR 721.80 Art. 51 Abs. 1"

    def formula(person, period, parameters):
        gefaelle = person('wrg_nutzbares_gefaelle_m', period)
        wassermenge = person('wrg_nutzbare_wassermenge_m3s', period)

        # P = rho * g * Q * H (in Watts), convert to kW
        # rho*g = 9810 N/m3
        return gefaelle * wassermenge * WASSER_SPEZIFISCHES_GEWICHT / 1000
