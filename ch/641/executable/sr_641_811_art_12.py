"""SR 641.811 Art. 12 - Transporte von offener Milch und landwirtschaftlichen Nutztieren

Vehicles exclusively transporting open milk or agricultural livestock
(excluding horse transport) pay 75% of the standard rates per Art. 14(1).

Generated from: ch/641/de/641.811.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class svav_milchtransport_ausschliesslich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Milch-Transportfahrzeug fuer ausschliesslich offene Milch (Art. 12 Bst. a SVAV)"
    reference = "SR 641.811 Art. 12 Bst. a"


class svav_viehtransport_ausschliesslich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Viehtransportfahrzeug fuer ausschliesslich landwirtschaftliche Nutztiere, "
        "ausgenommen Pferde (Art. 12 Bst. b SVAV)"
    )
    reference = "SR 641.811 Art. 12 Bst. b"


class svav_milch_vieh_ermaessigung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Ermaessigungsfaktor fuer Milch-/Viehtransport (Art. 12 SVAV)"
    reference = "SR 641.811 Art. 12"

    def formula(person, period, parameters):
        milch = person('svav_milchtransport_ausschliesslich', period)
        vieh = person('svav_viehtransport_ausschliesslich', period)
        # 75% of standard rate for exclusive milk/livestock transport
        berechtigt = milch + vieh
        return berechtigt * 0.75 + (1 - berechtigt) * 1.0
