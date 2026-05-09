"""SR 641.811 Art. 3 - Ausnahmen von der Abgabepflicht

Exemptions from heavy vehicle tax: military vehicles, civil protection,
police/fire/ambulance, public transport concession vehicles, agricultural
vehicles, electric motor vehicles, veteran vehicles, etc.

Generated from: ch/641/de/641.811.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class svav_fahrzeug_militaer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrzeug fuer Armee mit Militaerkontrollschildern (Art. 3 Abs. 1 Bst. a SVAV)"
    reference = "SR 641.811 Art. 3 Abs. 1 Bst. a"


class svav_fahrzeug_zivilschutz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrzeug fuer Zivilschutz (Art. 3 Abs. 1 Bst. abis SVAV)"
    reference = "SR 641.811 Art. 3 Abs. 1 Bst. abis"


class svav_fahrzeug_polizei_feuerwehr_ambulanz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrzeug der Polizei, Feuerwehr, Chemiewehr oder Ambulanz (Art. 3 Abs. 1 Bst. b SVAV)"
    reference = "SR 641.811 Art. 3 Abs. 1 Bst. b"


class svav_fahrzeug_linienverkehr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrzeug mit Personenbefoerderungskonzession im Linienverkehr (Art. 3 Abs. 1 Bst. c SVAV)"
    reference = "SR 641.811 Art. 3 Abs. 1 Bst. c"


class svav_fahrzeug_landwirtschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Land- und forstwirtschaftliches Fahrzeug (Art. 3 Abs. 1 Bst. d SVAV)"
    reference = "SR 641.811 Art. 3 Abs. 1 Bst. d"


class svav_fahrzeug_elektrisch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Motorwagen mit elektrischem Antrieb (Art. 3 Abs. 1 Bst. j SVAV)"
    reference = "SR 641.811 Art. 3 Abs. 1 Bst. j"


class svav_fahrzeug_veteran(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Veteranenfahrzeug gemaess Fahrzeugausweis (Art. 3 Abs. 1 Bst. i SVAV)"
    reference = "SR 641.811 Art. 3 Abs. 1 Bst. i"


class svav_von_abgabe_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Von der Schwerverkehrsabgabe befreit (Art. 3 SVAV)"
    reference = "SR 641.811 Art. 3"

    def formula(person, period, parameters):
        militaer = person('svav_fahrzeug_militaer', period)
        zivilschutz = person('svav_fahrzeug_zivilschutz', period)
        polizei = person('svav_fahrzeug_polizei_feuerwehr_ambulanz', period)
        linien = person('svav_fahrzeug_linienverkehr', period)
        landw = person('svav_fahrzeug_landwirtschaft', period)
        elektro = person('svav_fahrzeug_elektrisch', period)
        veteran = person('svav_fahrzeug_veteran', period)
        return militaer + zivilschutz + polizei + linien + landw + elektro + veteran
