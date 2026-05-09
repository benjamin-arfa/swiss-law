"""SR 641.811 Art. 8 - Rueckerstattung fuer unbegleiteten kombinierten Verkehr (UKV)

Refund per loading unit transferred between road and rail/ship:
a. Containers/semi-trailers 4.8-5.5m: CHF 15
b. Containers/semi-trailers >5.5-6.1m: CHF 22
c. Containers/semi-trailers >6.1m: CHF 33

The refund may not exceed the total tax for UKV vehicles per period.

Generated from: ch/641/de/641.811.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class svav_ukv_ladebehaelter_laenge_m(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Laenge des Ladebehaelters/Sattelanhaengers in Metern (Art. 8 Abs. 2 SVAV)"
    reference = "SR 641.811 Art. 8 Abs. 2"


class svav_ukv_anzahl_umschlaege(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Umschlaege Strasse-Bahn/Schiff pro Monat (Art. 8 Abs. 2 SVAV)"
    reference = "SR 641.811 Art. 8 Abs. 2"


class svav_ukv_rueckerstattung_pro_umschlag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Rueckerstattungsbetrag pro Umschlag in CHF (Art. 8 Abs. 2 SVAV)"
    reference = "SR 641.811 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        laenge = person('svav_ukv_ladebehaelter_laenge_m', period)
        # a. 4.8-5.5m: CHF 15
        # b. >5.5-6.1m: CHF 22
        # c. >6.1m: CHF 33
        return (
            (laenge >= 4.8) * (laenge <= 5.5) * 15 +
            (laenge > 5.5) * (laenge <= 6.1) * 22 +
            (laenge > 6.1) * 33
        )


class svav_ukv_rueckerstattung_monatlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Monatliche Rueckerstattung UKV in CHF (Art. 8 Abs. 2-4 SVAV)"
    reference = "SR 641.811 Art. 8"

    def formula(person, period, parameters):
        pro_umschlag = person('svav_ukv_rueckerstattung_pro_umschlag', period)
        anzahl = person('svav_ukv_anzahl_umschlaege', period)
        return pro_umschlag * anzahl
