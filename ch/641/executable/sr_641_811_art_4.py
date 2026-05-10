"""SR 641.811 Art. 4 - Pauschale Abgabeerhebung (Flat-rate tax collection)

Flat-rate annual fees for specific vehicle categories:
a. Heavy passenger transport vehicles >3.5t: CHF 650
b. Coaches/articulated buses >3.5-8.5t: CHF 2200
c. Coaches/articulated buses >8.5-19.5t: CHF 3300
d. Coaches/articulated buses >19.5-26t: CHF 4400
e. Coaches/articulated buses >26t: CHF 5000
f. Slow vehicles <=45km/h: CHF 11 per 100kg
g. Showman/circus vehicles: CHF 8 per 100kg

Generated from: ch/641/de/641.811.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class svav_ist_personentransport_schwer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Schwerer Motorwagen fuer Personentransport >3.5t (Art. 4 Abs. 1 Bst. a SVAV)"
    reference = "SR 641.811 Art. 4 Abs. 1 Bst. a"


class svav_ist_gesellschaftswagen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesellschaftswagen oder Gelenkbus (Art. 4 Abs. 1 Bst. b-e SVAV)"
    reference = "SR 641.811 Art. 4 Abs. 1 Bst. b-e"


class svav_ist_langsames_fahrzeug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Motorkarren/Traktor/Sachentransport mit Hoechstgeschwindigkeit bis 45 km/h (Art. 4 Abs. 1 Bst. f)"
    reference = "SR 641.811 Art. 4 Abs. 1 Bst. f"


class svav_ist_schausteller_fahrzeug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Schausteller- oder Zirkusfahrzeug (Art. 4 Abs. 1 Bst. g SVAV)"
    reference = "SR 641.811 Art. 4 Abs. 1 Bst. g"


class svav_pauschale_abgabe_jaehrlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche pauschale Schwerverkehrsabgabe in CHF (Art. 4 SVAV)"
    reference = "SR 641.811 Art. 4"

    def formula(person, period, parameters):
        gewicht = person('svav_gesamtgewicht_kg', period)
        gewicht_100kg = gewicht / 100

        ist_person = person('svav_ist_personentransport_schwer', period)
        ist_gesellschaft = person('svav_ist_gesellschaftswagen', period)
        ist_langsam = person('svav_ist_langsames_fahrzeug', period)
        ist_schausteller = person('svav_ist_schausteller_fahrzeug', period)

        # a. Heavy passenger transport >3.5t: CHF 650/year
        pauschale_person = ist_person * 650

        # b-e. Coaches/articulated buses by weight class
        pauschale_gesellschaft = ist_gesellschaft * (
            (gewicht <= 8500) * 2200 +
            (gewicht > 8500) * (gewicht <= 19500) * 3300 +
            (gewicht > 19500) * (gewicht <= 26000) * 4400 +
            (gewicht > 26000) * 5000
        )

        # f. Slow vehicles: CHF 11 per 100kg
        pauschale_langsam = ist_langsam * gewicht_100kg * 11

        # g. Showman/circus: CHF 8 per 100kg
        pauschale_schausteller = ist_schausteller * gewicht_100kg * 8

        return pauschale_person + pauschale_gesellschaft + pauschale_langsam + pauschale_schausteller
