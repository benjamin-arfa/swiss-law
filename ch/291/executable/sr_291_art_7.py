"""SR 291 Art. 7

Generated from: ch/291/de/291.md

Schiedsvereinbarung: Haben die Parteien ueber eine schiedsfaehige Streitsache
eine Schiedsvereinbarung getroffen, so lehnt das schweizerische Gericht seine
Zustaendigkeit ab, es sei denn:
a) der Beklagte hat sich vorbehaltlos eingelassen;
b) die Schiedsvereinbarung ist hinfaellig, unwirksam oder nicht erfuellbar;
c) das Schiedsgericht kann nicht bestellt werden aus Gruenden, die der
   Beklagte zu verantworten hat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class schiedsvereinbarung_getroffen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Parteien eine Schiedsvereinbarung getroffen haben"
    reference = "SR 291 Art. 7"


class schiedsvereinbarung_hinfaellig_oder_unwirksam(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schiedsvereinbarung hinfaellig, unwirksam oder nicht erfuellbar ist"
    reference = "SR 291 Art. 7 lit. b"


class schiedsgericht_nicht_bestellbar_durch_beklagten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Schiedsgericht aus Gruenden des Beklagten nicht bestellt werden kann"
    reference = "SR 291 Art. 7 lit. c"


class gericht_lehnt_zustaendigkeit_wegen_schiedsvereinbarung_ab(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gericht seine Zustaendigkeit wegen Schiedsvereinbarung ablehnt"
    reference = "SR 291 Art. 7"

    def formula(person, period, parameters):
        schiedsvereinbarung = person('schiedsvereinbarung_getroffen', period)
        einlassung = person('vorbehaltlose_einlassung_erfolgt', period)
        hinfaellig = person('schiedsvereinbarung_hinfaellig_oder_unwirksam', period)
        nicht_bestellbar = person(
            'schiedsgericht_nicht_bestellbar_durch_beklagten', period
        )
        # Gericht lehnt ab, wenn Schiedsvereinbarung besteht
        # UND keine der drei Ausnahmen (a, b, c) vorliegt
        ausnahme = einlassung + hinfaellig + nicht_bestellbar
        return schiedsvereinbarung * not_(ausnahme > 0)
