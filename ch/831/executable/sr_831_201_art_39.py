"""SR 831.201 Art. 39

Generated from: ch/831/de/831.201.md

Intensivpflegezuschlag (Intensive care supplement for minors):
- Abs. 1: Intensive care = minor needs >= 4 additional hours of care per day
  due to health impairment
- Abs. 2: Only the additional care need vs. non-disabled minors of same age counts.
  Time for physician-ordered medical measures by medical staff and
  pedagogical-therapeutic measures is excluded.
- Abs. 3: Permanent supervision due to health impairment can count as
  2 hours of care; especially intensive supervision counts as 4 hours.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_minderjaehrig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die versicherte Person minderjaehrig ist"
    reference = "SR 831.201 Art. 39 Abs. 1"


class iv_zusaetzlicher_betreuungsbedarf_stunden_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Zusaetzlicher Betreuungsbedarf pro Tag in Stunden (Mehrbedarf vs. nicht behinderte Minderjaehrige)"
    reference = "SR 831.201 Art. 39 Abs. 1-2"


class iv_benoetigt_dauernde_ueberwachung_minderjaehrig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die minderjaehrige Person infolge Gesundheit dauernder Ueberwachung bedarf"
    reference = "SR 831.201 Art. 39 Abs. 3"


class iv_besonders_intensive_ueberwachung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine besonders intensive behinderungsbedingte Ueberwachung erforderlich ist"
    reference = "SR 831.201 Art. 39 Abs. 3"


class iv_anrechenbare_betreuung_stunden_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anrechenbare Betreuungsstunden pro Tag (inkl. Ueberwachungszuschlag)"
    reference = "SR 831.201 Art. 39"

    def formula(person, period, parameters):
        import numpy as np
        betreuung = person('iv_zusaetzlicher_betreuungsbedarf_stunden_tag', period)
        ueberwachung = person('iv_benoetigt_dauernde_ueberwachung_minderjaehrig', period)
        intensiv = person('iv_besonders_intensive_ueberwachung', period)

        # Abs. 3: supervision counts as 2h; especially intensive = 4h
        ueberwachung_stunden = np.where(
            intensiv, 4.0,
            np.where(ueberwachung, 2.0, 0.0)
        )

        return betreuung + ueberwachung_stunden


class iv_anspruch_intensivpflegezuschlag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Intensivpflegezuschlag (>= 4h zusaetzliche Betreuung/Tag)"
    reference = "SR 831.201 Art. 39 Abs. 1"

    def formula(person, period, parameters):
        minderjaehrig = person('iv_minderjaehrig', period)
        stunden = person('iv_anrechenbare_betreuung_stunden_tag', period)
        return minderjaehrig & (stunden >= 4)
