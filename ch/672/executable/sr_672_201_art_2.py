"""SR 672.201 Art. 2 — Anspruch auf Anrechnung ausländischer Quellensteuern

Art. 2: In der Schweiz ansässige natürliche und juristische Personen können
für die in Übereinstimmung mit einem DBA erhobene begrenzte Steuer eine
Anrechnung beantragen. Bei Kollektiv-/Kommanditgesellschaften steht der
Anspruch der Gesellschaft zu. Alternativ: Abzug vom Bruttobetrag möglich.

Generated from: ch/672/de/672.201.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_in_schweiz_ansaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist in der Schweiz ansässig (SR 672.201 Art. 2 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_2"


class beantragt_anrechnung_auslaendischer_quellensteuern(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person beantragt Anrechnung ausländischer Quellensteuern (SR 672.201 Art. 2 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_2"
    default_value = False


class anspruch_anrechnung_auslaendischer_quellensteuern(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat Anspruch auf Anrechnung ausländischer Quellensteuern (SR 672.201 Art. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_2"

    def formula(person, period, parameters):
        # Art. 2 Abs. 1: In der Schweiz ansässige Personen können für
        # DBA-konforme begrenzte Steuer eine Anrechnung beantragen.
        ansaessig = person('ist_in_schweiz_ansaessig', period)
        beantragt = person('beantragt_anrechnung_auslaendischer_quellensteuern', period)
        hat_ertraege = person('ertrag_unterliegt_begrenzter_steuer_vertragsstaat', period)
        return ansaessig * beantragt * hat_ertraege


class abzug_auslaendische_steuer_statt_anrechnung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Abzug der ausländischen Steuer vom Bruttobetrag statt Anrechnung (SR 672.201 Art. 2 Abs. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_2"

    def formula(person, period, parameters):
        # Art. 2 Abs. 3: Wer die Anrechnung nicht beantragt, kann verlangen,
        # dass die im Vertragsstaat erhobenen Steuern vom Bruttobetrag abgezogen werden.
        ansaessig = person('ist_in_schweiz_ansaessig', period)
        beantragt_anrechnung = person('beantragt_anrechnung_auslaendischer_quellensteuern', period)
        ertrag = person('ertrag_aus_vertragsstaat', period)
        # Only available if anrechnung not claimed
        return ansaessig * (1 - beantragt_anrechnung) * ertrag * 0  # Placeholder: actual foreign tax amount needed
