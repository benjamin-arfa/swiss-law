"""SR 822.114 Art. 17 - Fenster (Window requirements)

ArGV 4 - Minimum window area and ventilation requirements.
Art. 17:
  Abs. 1: Window area (facade + skylights) must be at least 1/8 of floor area
  Abs. 2: At least half must be transparent facade windows
  Abs. 4: Window sill height should not exceed 1.2 m
  Abs. 6: For natural ventilation: min 3 m2 openable per 100 m2 floor area

Generated from: ch/822/de/822.114.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class argv4_fensterflaeche_gesamt(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total window area (facade + skylights) in m2 (SR 822.114 Art. 17)"
    reference = "SR 822.114 Art. 17"
    default_value = 0.0


class argv4_min_fensterflaeche(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum required window area in m2 - 1/8 of floor area (SR 822.114 Art. 17 Abs. 1)"
    reference = "SR 822.114 Art. 17"

    def formula(person, period, parameters):
        flaeche = person("argv4_bodenflaeche", period)
        return flaeche / 8.0


class argv4_min_fassadenfenster(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum transparent facade window area in m2 - half of required total (SR 822.114 Art. 17 Abs. 2)"
    reference = "SR 822.114 Art. 17"

    def formula(person, period, parameters):
        min_gesamt = person("argv4_min_fensterflaeche", period)
        return min_gesamt / 2.0


class argv4_fenster_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether window area meets minimum requirements (SR 822.114 Art. 17)"
    reference = "SR 822.114 Art. 17"

    def formula(person, period, parameters):
        gesamt = person("argv4_fensterflaeche_gesamt", period)
        minimum = person("argv4_min_fensterflaeche", period)
        return gesamt >= minimum


class argv4_min_lueftungsflaeche(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimum openable window area for ventilation in m2 (SR 822.114 Art. 17 Abs. 6)"
    reference = "SR 822.114 Art. 17"

    def formula(person, period, parameters):
        flaeche = person("argv4_bodenflaeche", period)
        # 3 m2 per 100 m2 floor area
        return flaeche * 3.0 / 100.0


class argv4_max_fensterbruestung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximum window sill height in meters - 1.2 m (SR 822.114 Art. 17 Abs. 4)"
    reference = "SR 822.114 Art. 17"
    default_value = 1.2
