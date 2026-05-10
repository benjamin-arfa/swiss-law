"""SR 831.20 Art. 38

Generated from: ch/831/de/831.20.md

Art. 38: Hoehe der Kinderrenten - Amount of child pensions:
- Abs. 1: The child pension is 40% of the disability pension corresponding
  to the relevant average annual income. If both parents are entitled, the
  sum of both child pensions is capped at 60% of the maximum disability
  pension (reduction per Art. 35 AHVG).
- Abs. 2: The same calculation rules as for the respective disability pension apply.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_rente_massgebendes_einkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Massgebendes durchschnittliches Jahreseinkommen fuer die IV-Rente"
    reference = "SR 831.20 Art. 38 Abs. 1"


class iv_maximale_invalidenrente(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Invalidenrente (CHF/Monat)"
    reference = "SR 831.20 Art. 38 Abs. 1"


class iv_anzahl_kinder_rente(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Kinder mit Anspruch auf Kinderrente"
    reference = "SR 831.20 Art. 38"


class iv_beide_eltern_kinderrente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beide Elternteile haben Anspruch auf Kinderrente"
    reference = "SR 831.20 Art. 38 Abs. 1"


class iv_kinderrente_pro_kind(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "IV-Kinderrente pro Kind (Art. 38 IVG, CHF/Monat)"
    reference = "SR 831.20 Art. 38 Abs. 1"

    def formula(person, period, parameters):
        iv_rente = person('iv_rente_betrag', period)
        # 40% of the disability pension
        return iv_rente * 0.40


class iv_kinderrenten_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Total Kinderrenten mit Plafonierung (Art. 38 IVG, CHF/Monat)"
    reference = "SR 831.20 Art. 38 Abs. 1"

    def formula(person, period, parameters):
        pro_kind = person('iv_kinderrente_pro_kind', period)
        anzahl = person('iv_anzahl_kinder_rente', period)
        beide_eltern = person('iv_beide_eltern_kinderrente', period)
        max_rente = person('iv_maximale_invalidenrente', period)

        total = pro_kind * anzahl

        # If both parents entitled: cap at 60% of max disability pension
        plafond = max_rente * 0.60
        total = where(beide_eltern, min_(total, plafond), total)
        return total
