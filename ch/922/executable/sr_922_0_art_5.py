"""SR 922.0 Art. 5

Generated from: ch/922/de/922.0.md

Art. 5: Jagdbare Arten und Schonzeiten - Huntable species and closed seasons.
Defines closed season periods for each huntable species.
Cantons may extend closed seasons or restrict the list of huntable species.
Certain species (raccoon dog, raccoon, feral domestic cat, etc.) may be hunted year-round.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
import numpy as np


class jsg_jagdbare_art_code(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Code der jagdbaren Art nach JSG Art. 5 (1=Rothirsch, 2=Wildschwein, 3=Damhirsch/Sika/Mufflon, 4=Reh, 5=Gämse, 6=Feldhase/Schneehase/Wildkaninchen, 7=Murmeltier, 8=Fuchs, 9=Dachs, 10=Marder, 11=Birkhahn/Schneehuhn/Rebhuhn, 12=Tauben/Raben/Krähe, 13=Fasan, 14=Wasservögel, 15=Waldschnepfe, 99=ganzjährig jagdbar, 0=nicht jagdbar)"
    reference = "SR 922.0 Art. 5"


class jsg_ist_jagdbare_art(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Tier gehört zu einer jagdbaren Art nach JSG"
    reference = "SR 922.0 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        art_code = person('jsg_jagdbare_art_code', period)
        return art_code > 0


class jsg_schonzeit_beginn_monat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Beginn der Schonzeit (Monat, 1-12) nach Art. 5 Abs. 1"
    reference = "SR 922.0 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        code = person('jsg_jagdbare_art_code', period)
        # Closed season start month per species group
        # a. Rothirsch: 1.Feb; b. Wildschwein: 1.Feb; c. Dam/Sika/Mufflon: 1.Feb
        # d. Reh: 1.Feb; e. Gämse: 1.Jan; f. Hasenartige: 1.Jan
        # g. Murmeltier: 16.Okt; h. Fuchs: 1.März; i. Dachs: 16.Jan
        # j. Marder: 16.Feb; k. Birkhahn etc: 1.Dez; l. Tauben etc: 16.Feb
        # m. Fasan: 1.Feb; n. Wasservögel: 1.Feb; o. Waldschnepfe: 15.Dez
        result = np.select(
            [code == 1, code == 2, code == 3, code == 4, code == 5,
             code == 6, code == 7, code == 8, code == 9, code == 10,
             code == 11, code == 12, code == 13, code == 14, code == 15],
            [2, 2, 2, 2, 1, 1, 10, 3, 1, 2, 12, 2, 2, 2, 12],
            default=0
        )
        return result


class jsg_schonzeit_ende_monat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Ende der Schonzeit (Monat, 1-12) nach Art. 5 Abs. 1"
    reference = "SR 922.0 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        code = person('jsg_jagdbare_art_code', period)
        # Closed season end month per species group
        # a. Rothirsch: 31.Jul; b. Wildschwein: 30.Jun; c. Dam/Sika/Mufflon: 31.Jul
        # d. Reh: 30.Apr; e. Gämse: 31.Jul; f. Hasenartige: 30.Sep
        # g. Murmeltier: 31.Aug; h. Fuchs: 15.Jun; i. Dachs: 15.Jun
        # j. Marder: 31.Aug; k. Birkhahn etc: 15.Okt; l. Tauben etc: 31.Jul
        # m. Fasan: 31.Aug; n. Wasservögel: 31.Aug; o. Waldschnepfe: 15.Sep
        result = np.select(
            [code == 1, code == 2, code == 3, code == 4, code == 5,
             code == 6, code == 7, code == 8, code == 9, code == 10,
             code == 11, code == 12, code == 13, code == 14, code == 15],
            [7, 6, 7, 4, 7, 9, 8, 6, 6, 8, 10, 7, 8, 8, 9],
            default=0
        )
        return result


class jsg_ganzjaehrig_jagdbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Tier darf ganzjährig gejagt werden (Art. 5 Abs. 3)"
    reference = "SR 922.0 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        code = person('jsg_jagdbare_art_code', period)
        # Code 99 = year-round huntable (raccoon dog, raccoon, feral cat, carrion crow, magpie, jay, feral pigeon)
        return code == 99
