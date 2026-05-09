"""SR 810.211 Art. 11

Generated from: ch/810/de/810.211.md

Art. 11: Versicherungsschutz fuer Lebendspender.

Abs. 1: Wer einer lebenden Person Organe, Gewebe oder Zellen entnimmt,
muss sicherstellen, dass fuer diese Person mindestens 12 Monate ab der
Entnahme ein Versicherungsvertrag besteht fuer die Risiken Tod und
Invaliditaet.

Abs. 2: Im Todesfall betraegt die Versicherungsleistung 250'000 Franken.
Anspruchsberechtigt sind die Hinterbliebenen.

Abs. 3: Fuer den Invaliditaetsfall ist eine Summe von 250'000 Franken
zu versichern. Berechnung nach Anhang 3 UVV (SR 832.202).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_lebendspender(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist Lebendspender/in von Organen, Geweben oder Zellen"
    reference = "SR 810.211 Art. 11 Abs. 1"


class monate_seit_entnahme(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Monate seit der Entnahme von Organen, Geweben oder Zellen"
    reference = "SR 810.211 Art. 11 Abs. 1"


class versicherungspflicht_lebendspende(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Versicherungsvertrag fuer Lebendspender muss bestehen (min. 12 Monate ab Entnahme)"
    reference = "SR 810.211 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        ist_spender = person('ist_lebendspender', period)
        monate = person('monate_seit_entnahme', period)
        min_dauer = parameters(period).sr_810_211.art_11.mindestdauer_versicherung_monate
        return ist_spender * (monate <= min_dauer)


class versicherungssumme_todesfall(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherungsleistung im Todesfall fuer Lebendspender (CHF)"
    reference = "SR 810.211 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return parameters(period).sr_810_211.art_11.versicherungssumme_todesfall


class versicherungssumme_invaliditaet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherungssumme im Invaliditaetsfall fuer Lebendspender (CHF)"
    reference = "SR 810.211 Art. 11 Abs. 3"

    def formula(person, period, parameters):
        return parameters(period).sr_810_211.art_11.versicherungssumme_invaliditaet
