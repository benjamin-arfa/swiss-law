"""SR 923.0 Art. 4 & 5

Generated from: ch/923/de/923.0.md

Art. 4: Schonbestimmungen - Conservation provisions:
1. Federal Council sets: a. closed season durations; b. minimum catch sizes
2. Conditions for cantonal deviations
3. Cantons: a. conservation areas; b. return of live fish/crayfish caught during closed season

Art. 5: Gefährdete Arten und Rassen - Endangered species:
1. Federal Council designates endangered species/breeds
2. Cantons take measures to protect habitats; may order catch bans
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bgf_ist_in_schonzeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Fisch-/Krebsart befindet sich aktuell in der Schonzeit"
    reference = "SR 923.0 Art. 4 Abs. 1 Bst. a"


class bgf_fangmindestmass_cm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Fangmindestmass für die betreffende Art (cm)"
    reference = "SR 923.0 Art. 4 Abs. 1 Bst. b"


class bgf_fisch_erreicht_mindestmass(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gefangener Fisch/Krebs erreicht das Fangmindestmass"
    reference = "SR 923.0 Art. 4 Abs. 1 Bst. b"


class bgf_art_ist_gefaehrdet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Art/Rasse ist als gefährdet bezeichnet (Art. 5 Abs. 1)"
    reference = "SR 923.0 Art. 5 Abs. 1"


class bgf_fang_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Fang ist zulässig (nicht in Schonzeit, Mindestmass erreicht, Art nicht gesperrt)"
    reference = "SR 923.0 Art. 4"

    def formula(person, period, parameters):
        schonzeit = person('bgf_ist_in_schonzeit', period)
        mindestmass = person('bgf_fisch_erreicht_mindestmass', period)
        gefaehrdet = person('bgf_art_ist_gefaehrdet', period)
        # Catch allowed if: not in closed season, meets minimum size, not endangered
        return (1 - schonzeit) * mindestmass * (1 - gefaehrdet)
