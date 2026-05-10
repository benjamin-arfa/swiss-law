"""SR 641.811 Art. 2 - Abgabeobjekt (Taxable vehicles)

Heavy vehicle tax applies to transport motor vehicles and transport trailers
with a gross weight exceeding 3.5 tonnes (Art. 11(1) and 20(1) VTS).

Generated from: ch/641/de/641.811.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class svav_gesamtgewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtgewicht des Fahrzeugs in kg (Art. 2 Abs. 1 SVAV)"
    reference = "SR 641.811 Art. 2 Abs. 1"


class svav_ist_transportmotorwagen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrzeug ist ein Transportmotorwagen nach Art. 11 Abs. 1 VTS"
    reference = "SR 641.811 Art. 2 Abs. 1"


class svav_ist_transportanhaenger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrzeug ist ein Transportanhaenger nach Art. 20 Abs. 1 VTS"
    reference = "SR 641.811 Art. 2 Abs. 1"


class svav_abgabepflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrzeug unterliegt der Schwerverkehrsabgabe (Art. 2 SVAV)"
    reference = "SR 641.811 Art. 2"

    def formula(person, period, parameters):
        gewicht = person('svav_gesamtgewicht_kg', period)
        ist_motor = person('svav_ist_transportmotorwagen', period)
        ist_anhaenger = person('svav_ist_transportanhaenger', period)
        return (ist_motor + ist_anhaenger) * (gewicht > 3500)
