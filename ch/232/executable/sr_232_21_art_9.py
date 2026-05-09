"""SR 232.21 Art. 9

Generated from: ch/232/de/232.21.md

Art. 9 regulates the use of official designations (amtliche Bezeichnungen).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_berechtigtes_gemeinwesen_bezeichnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ist das Gemeinwesen, zu dem die amtliche Bezeichnung gehoert"
    reference = "SR 232.21 Art. 9 Abs. 1"


class uebt_behoerdliche_taetigkeit_aus(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person uebt eine behoerdliche oder behoerdennahe Taetigkeit aus"
    reference = "SR 232.21 Art. 9 Abs. 2"


class darf_amtliche_bezeichnung_verwenden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Darf amtliche Bezeichnungen (Eidgenossenschaft, Bund, kantonal etc.) verwenden"
    reference = "SR 232.21 Art. 9"

    def formula(person, period, parameters):
        # Abs. 1: nur das berechtigte Gemeinwesen fuer sich allein
        ist_gemeinwesen = person('ist_berechtigtes_gemeinwesen_bezeichnung', period)
        # Abs. 2: andere Personen nur bei behoerdlicher Taetigkeit
        behoerdlich = person('uebt_behoerdliche_taetigkeit_aus', period)
        return ist_gemeinwesen + behoerdlich > 0
