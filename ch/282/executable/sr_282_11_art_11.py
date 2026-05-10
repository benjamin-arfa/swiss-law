"""SR 282.11 Art. 11 - Widmung eines belasteten Grundstuecks

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class grundstueck_mit_pfandrecht_belastet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Grundstueck ist mit einem Pfandrecht belastet"
    reference = "SR 282.11 Art. 11 Abs. 1"


class grundstueck_oeffentlichen_aufgaben_gewidmet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Grundstueck wird oeffentlichen Aufgaben gewidmet"
    reference = "SR 282.11 Art. 11 Abs. 1"


class pfandglaeubiger_befriedigt_oder_sichergestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Pfandglaeubiger ist befriedigt oder sichergestellt worden"
    reference = "SR 282.11 Art. 11 Abs. 1"


# Computed variables

class grundstueck_als_finanzvermoegen_behandeln(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Grundstueck ist als Finanzvermoegen zu behandeln"
    reference = "SR 282.11 Art. 11 Abs. 2"

    def formula(self, period, parameters):
        belastet = self('grundstueck_mit_pfandrecht_belastet', period)
        gewidmet = self('grundstueck_oeffentlichen_aufgaben_gewidmet', period)
        befriedigt = self('pfandglaeubiger_befriedigt_oder_sichergestellt', period)
        # Bis Pfandglaeubiger befriedigt, als Finanzvermoegen behandeln
        return belastet * gewidmet * (1 - befriedigt)
