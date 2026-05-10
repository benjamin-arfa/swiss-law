"""SR 861.1 Art. 11

Generated from: ch/861/de/861.1.md

Art. 11: Bemessung und Dauer der Finanzhilfen an Tagesfamilien-Koordination
- Training: up to CHF 150 per employed day-care family, max 1/3 of costs, max 3 years
- Projects: 1/3 of eligible costs
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kbfhv_tagesfamilien_anzahl(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl beschäftigter Tagesfamilien"
    reference = "SR 861.1 Art. 11 Abs. 1"


class kbfhv_tagesfamilien_ausbildungskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Effektive jährliche Aus- und Weiterbildungskosten (CHF)"
    reference = "SR 861.1 Art. 11 Abs. 1"


class kbfhv_tagesfamilien_beitragsjahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Laufendes Beitragsjahr für Tagesfamilien-Ausbildung (1-3)"
    reference = "SR 861.1 Art. 11 Abs. 1"


class kbfhv_tagesfamilien_finanzhilfe_ausbildung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzhilfe an Aus- und Weiterbildung der Tagesfamilien (CHF)"
    reference = "SR 861.1 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        anzahl = person('kbfhv_tagesfamilien_anzahl', period)
        kosten = person('kbfhv_tagesfamilien_ausbildungskosten', period)
        beitragsjahr = person('kbfhv_tagesfamilien_beitragsjahr', period)

        p = parameters(period).sr_861_1
        max_pro_familie = p.tagesfamilien_max_pro_familie

        # Up to CHF 150 per family, max 1/3 of costs
        betrag_pro_familie = anzahl * max_pro_familie
        drittel_kosten = kosten / 3.0
        beitrag = min_(betrag_pro_familie, drittel_kosten)

        # Max 3 years
        return where(beitragsjahr <= 3, beitrag, 0)


class kbfhv_tagesfamilien_projektkosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Projektkosten für Tagesfamilien-Koordination (CHF)"
    reference = "SR 861.1 Art. 11 Abs. 2"


class kbfhv_tagesfamilien_finanzhilfe_projekt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzhilfe an Projekte zur Verbesserung der Tagesfamilien-Koordination (CHF)"
    reference = "SR 861.1 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        kosten = person('kbfhv_tagesfamilien_projektkosten', period)
        # 1/3 of eligible costs
        return kosten / 3.0
