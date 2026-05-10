"""SR 832.112.31 Art. 8

Generated from: ch/832/de/832.112.31.md

Art. 8: Aerztlicher Auftrag oder aerztliche Anordnung (Pflege)
- Abs. 2a: Leistungen nach Art. 7 Abs. 2 Bst. b: maximal 9 Monate
- Abs. 2b: Leistungen der Akut-/Uebergangspflege: maximal 2 Wochen
- Abs. 3: Bei Hilflosenentschaedigung wegen mittlerer/schwerer Hilflosigkeit:
  Anordnung gilt unbefristet.
- Abs. 4: Anordnungen nach Abs. 2a koennen verlaengert werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class klv_pflege_ist_akut_uebergangspflege(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Leistung ist Akut- und Uebergangspflege nach Art. 25a Abs. 2 KVG"
    reference = "SR 832.112.31 Art. 8 Abs. 2 Bst. b"


class klv_pflege_hilflosenentschaedigung_mittel_schwer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hilflosenentschaedigung wegen mittlerer oder schwerer Hilflosigkeit"
    reference = "SR 832.112.31 Art. 8 Abs. 3"


class klv_pflege_anordnung_max_dauer_monate(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Dauer der aerztlichen Anordnung fuer Pflegeleistungen (Monate)"
    reference = "SR 832.112.31 Art. 8 Abs. 2-3"

    def formula(person, period, parameters):
        ist_akut = person('klv_pflege_ist_akut_uebergangspflege', period)
        hilflos = person('klv_pflege_hilflosenentschaedigung_mittel_schwer', period)

        # Abs. 3: Unbefristet bei mittlerer/schwerer Hilflosigkeit
        # (Wir kodieren 'unbefristet' als 9999 Monate)
        # Abs. 2b: Akut-/Uebergangspflege: max 2 Wochen = 0.5 Monate
        # Abs. 2a: Sonstige Behandlung: max 9 Monate
        return select(
            [hilflos, ist_akut],
            [9999.0, 0.5],
            default=9.0,
        )


class klv_pflege_anordnung_unbefristet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Aerztliche Anordnung fuer Pflegeleistungen gilt unbefristet"
    reference = "SR 832.112.31 Art. 8 Abs. 3"

    def formula(person, period, parameters):
        return person('klv_pflege_hilflosenentschaedigung_mittel_schwer', period)
