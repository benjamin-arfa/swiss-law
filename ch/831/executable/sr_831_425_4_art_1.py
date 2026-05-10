"""SR 831.425.4 Art. 1

Generated from: ch/831/de/831.425.4.md

Calculation of exit benefit at time of marriage per Art. 22b FZG:
- Table in annex gives percentage of computed amount per Art. 22b(2) FZG
  that counts as exit benefit at time of marriage
- Determining factors: contribution period between entry payment and exit
  benefit, and marriage duration within that period
- Durations rounded to full years; if both < 3.05 years, round to 0.1 years
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
import numpy as np


class fzg_beitragsdauer_gesamt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beitragsdauer zwischen Eintrittsleistung und Austrittsleistung in Jahren"
    reference = "SR 831.425.4 Art. 1 Abs. 3 Bst. a"


class fzg_ehedauer_in_beitragsdauer(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ehedauer innerhalb der Beitragsdauer in Jahren"
    reference = "SR 831.425.4 Art. 1 Abs. 3 Bst. b"


class fzg_errechneter_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Errechneter Betrag nach Art. 22b Abs. 2 FZG in CHF"
    reference = "SR 831.425.4 Art. 1 Abs. 2"


class fzg_beitragsdauer_gerundet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gerundete Beitragsdauer in Jahren (ganze Jahre oder 0.1 wenn beide < 3.05)"
    reference = "SR 831.425.4 Art. 1 Abs. 4"

    def formula(person, period, parameters):
        gesamt = person('fzg_beitragsdauer_gesamt', period)
        ehe = person('fzg_ehedauer_in_beitragsdauer', period)

        # If both < 3.05: round to 0.1 years
        beide_klein = (gesamt < 3.05) * (ehe < 3.05)
        gerundet_fein = np.round(gesamt * 10) / 10
        gerundet_grob = np.round(gesamt)

        return where(beide_klein, gerundet_fein, gerundet_grob)


class fzg_ehedauer_gerundet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gerundete Ehedauer in Jahren (ganze Jahre oder 0.1 wenn beide < 3.05)"
    reference = "SR 831.425.4 Art. 1 Abs. 4"

    def formula(person, period, parameters):
        gesamt = person('fzg_beitragsdauer_gesamt', period)
        ehe = person('fzg_ehedauer_in_beitragsdauer', period)

        beide_klein = (gesamt < 3.05) * (ehe < 3.05)
        gerundet_fein = np.round(ehe * 10) / 10
        gerundet_grob = np.round(ehe)

        return where(beide_klein, gerundet_fein, gerundet_grob)


class fzg_austrittsleistung_anteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prozentualer Anteil des errechneten Betrags, der als Austrittsleistung im Zeitpunkt der Eheschliessung gilt"
    reference = "SR 831.425.4 Art. 1 Abs. 2"


class fzg_austrittsleistung_bei_eheschliessung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Austrittsleistung im Zeitpunkt der Eheschliessung in CHF"
    reference = "SR 831.425.4 Art. 1"

    def formula(person, period, parameters):
        betrag = person('fzg_errechneter_betrag', period)
        anteil = person('fzg_austrittsleistung_anteil', period)
        return betrag * anteil / 100
