"""SR 946.101 Art. 3

Generated from: ch/946/de/946.101.md

Schweizerischer Ursprung oder schweizerischer Wertschoepfungsanteil:
- Abs. 1: Ware ist schweizerischen Ursprungs nach Art. 9-16 der Ursprungsverordnung.
- Abs. 2: Ist die Ware nicht schweizerischen Ursprungs, muss der schweizerische
  Wertschoepfungsanteil am Auftragswert mindestens 20% betragen.
- Abs. 3: SERV kann Versicherung auch bei <20% gewaehren unter bestimmten Bedingungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ware_schweizerischen_ursprungs(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Ware schweizerischen Ursprungs ist (Art. 9-16 Ursprungsverordnung)"
    reference = "SR 946.101 Art. 3 Abs. 1"


class auftragswert_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Auftragswert des Exportvertrags (CHF)"
    reference = "SR 946.101 Art. 3 Abs. 2"


class wert_auslaendische_zulieferungen_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wert der auslaendischen Zu- und Unterlieferungen oder Leistungen (CHF)"
    reference = "SR 946.101 Art. 3 Abs. 2"


class schweizerischer_wertschoepfungsanteil_pct(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Schweizerischer Wertschoepfungsanteil am Auftragswert (%)"
    reference = "SR 946.101 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        auftragswert = person('auftragswert_chf', period)
        auslaendisch = person('wert_auslaendische_zulieferungen_chf', period)
        wertschoepfung = auftragswert - auslaendisch
        return where(auftragswert > 0, wertschoepfung / auftragswert * 100, 0)


class serv_ausnahme_unter_mindestwertschoepfung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob SERV eine Ausnahme bei Wertschoepfungsanteil unter Mindestgrenze gewaehrt"
    reference = "SR 946.101 Art. 3 Abs. 3"


class serv_versicherung_ursprung_zulassig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die SERV-Versicherung bezueglich Ursprung/Wertschoepfung zulaessig ist"
    reference = "SR 946.101 Art. 3"

    def formula(person, period, parameters):
        schweizer_ursprung = person('ware_schweizerischen_ursprungs', period)
        wertschoepfung_pct = person('schweizerischer_wertschoepfungsanteil_pct', period)
        ausnahme = person('serv_ausnahme_unter_mindestwertschoepfung', period)
        mindest_pct = parameters(period).sr_946_101.mindest_wertschoepfungsanteil_pct
        # Art. 3 Abs. 1: Swiss origin => OK
        # Art. 3 Abs. 2: Non-Swiss but >= 20% Swiss value added => OK
        # Art. 3 Abs. 3: Exception granted by SERV => OK
        genuegend_wertschoepfung = wertschoepfung_pct >= mindest_pct
        return schweizer_ursprung + genuegend_wertschoepfung + ausnahme > 0
