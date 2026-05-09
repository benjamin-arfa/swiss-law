"""SR 641.81 Art. 6 - Grundsatz der Bemessungsgrundlage (Tax base)

Heavy Vehicle Tax Act (SVAG) - Tax is based on maximum permitted gross weight
and kilometers driven in the customs territory.

Generated from: ch/641/de/641.81.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class svag_hoechstzulaessiges_gesamtgewicht(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximum permitted gross weight of vehicle in tonnes (SR 641.81 Art. 6 Abs. 1)"
    reference = "SR 641.81 Art. 6"
    default_value = 0.0


class svag_gefahrene_kilometer(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kilometers driven in customs territory (SR 641.81 Art. 6 Abs. 1)"
    reference = "SR 641.81 Art. 6"
    default_value = 0.0


class svag_gesamtzugsgewicht_als_basis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Use maximum gross train weight as tax basis for vehicle combinations (SR 641.81 Art. 6 Abs. 2)"
    reference = "SR 641.81 Art. 6"
    default_value = False
