"""SR 861.1 Art. 4

Generated from: ch/861/de/861.1.md

Art. 4: Kindertagesstätten - Eligibility requirements for childcare
institutions to receive federal financial aid:
- At least 10 places
- Open at least 25 hours/week and 45 weeks/year
- Substantial increase = +1/3 of places (min 10) or +1/3 of hours (min 375h/year)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kbfhv_kita_anzahl_plaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Betreuungsplätze der Kindertagesstätte"
    reference = "SR 861.1 Art. 4 Abs. 2 Bst. a"


class kbfhv_kita_oeffnungsstunden_pro_woche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Öffnungsstunden pro Woche der Kindertagesstätte"
    reference = "SR 861.1 Art. 4 Abs. 2 Bst. b"


class kbfhv_kita_oeffnungswochen_pro_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Öffnungswochen pro Jahr der Kindertagesstätte"
    reference = "SR 861.1 Art. 4 Abs. 2 Bst. b"


class kbfhv_kita_beitragsberechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kindertagesstätte erfüllt die Voraussetzungen für Finanzhilfen (Art. 4 KBFHV)"
    reference = "SR 861.1 Art. 4"

    def formula(person, period, parameters):
        plaetze = person('kbfhv_kita_anzahl_plaetze', period)
        stunden = person('kbfhv_kita_oeffnungsstunden_pro_woche', period)
        wochen = person('kbfhv_kita_oeffnungswochen_pro_jahr', period)

        min_plaetze = parameters(period).sr_861_1.kita_mindest_plaetze
        min_stunden = parameters(period).sr_861_1.kita_mindest_stunden_pro_woche
        min_wochen = parameters(period).sr_861_1.kita_mindest_wochen_pro_jahr

        return (plaetze >= min_plaetze) * (stunden >= min_stunden) * (wochen >= min_wochen)


class kbfhv_kita_wesentliche_erhoehung_plaetze(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Wesentliche Erhöhung der Plätze (mind. 1/3 oder 10 Plätze)"
    reference = "SR 861.1 Art. 4 Abs. 3 Bst. a"

    def formula(person, period, parameters):
        plaetze = person('kbfhv_kita_anzahl_plaetze', period)
        neue_plaetze = person('kbfhv_kita_neue_plaetze', period)

        # Increase by 1/3, but at least 10
        drittel = plaetze / 3.0
        schwelle = max_(drittel, 10)
        return neue_plaetze >= schwelle


class kbfhv_kita_neue_plaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl neue Betreuungsplätze in der Kindertagesstätte"
    reference = "SR 861.1 Art. 4 Abs. 3"
