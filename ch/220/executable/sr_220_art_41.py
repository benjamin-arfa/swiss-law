"""SR 220 Art. 41

Generated from: ch/de/220.md

Haftung aus unerlaubter Handlung: Wer einem andern widerrechtlich Schaden
zufuegt, sei es mit Absicht, sei es aus Fahrlaessigkeit, wird ihm zum
Ersatze verpflichtet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_schadenersatzpflichtig_art41(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Schadenersatzpflicht aus unerlaubter Handlung besteht (Art. 41 OR)"
    reference = "SR 220 Art. 41"

    def formula(person, period, parameters):
        hat_schaden_zugefuegt = person('hat_schaden_zugefuegt', period)
        ist_widerrechtlich = person('handlung_ist_widerrechtlich', period)
        hat_verschulden = person('hat_verschulden_absicht_oder_fahrlaessigkeit', period)
        gegen_gute_sitten = person('handlung_gegen_gute_sitten', period)
        hat_absicht = person('hat_absicht', period)

        # Abs. 1: Widerrechtlich + Verschulden (Absicht oder Fahrlaessigkeit)
        haftung_abs1 = hat_schaden_zugefuegt * ist_widerrechtlich * hat_verschulden

        # Abs. 2: Gegen gute Sitten + Absicht
        haftung_abs2 = hat_schaden_zugefuegt * gegen_gute_sitten * hat_absicht

        return (haftung_abs1 + haftung_abs2) > 0


class hat_schaden_zugefuegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person einem andern Schaden zugefuegt hat"
    reference = "SR 220 Art. 41 Abs. 1"


class handlung_ist_widerrechtlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Handlung widerrechtlich ist"
    reference = "SR 220 Art. 41 Abs. 1"


class hat_verschulden_absicht_oder_fahrlaessigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Verschulden vorliegt (Absicht oder Fahrlaessigkeit)"
    reference = "SR 220 Art. 41 Abs. 1"


class hat_absicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob absichtliches Handeln vorliegt"
    reference = "SR 220 Art. 41"


class handlung_gegen_gute_sitten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Handlung gegen die guten Sitten verstoesst"
    reference = "SR 220 Art. 41 Abs. 2"
