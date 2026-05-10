"""SR 0.101 Art. 15

Generated from: ch/0/de/0.101.md

Derogation in time of emergency: In time of war or other public emergency
threatening the life of the nation, derogation from Convention obligations
is possible. No derogation from Art. 2 (except lawful acts of war),
Art. 3, Art. 4(1) and Art. 7.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_notstand_krieg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Leben der Nation durch Krieg oder oeffentlichen Notstand bedroht ist"
    reference = "SR 0.101 Art. 15 Abs. 1"


class emrk_abweichung_lage_erfordert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Lage eine Abweichung von Konventionsverpflichtungen unbedingt erfordert"
    reference = "SR 0.101 Art. 15 Abs. 1"


class emrk_abweichung_notstand_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Abweichung von EMRK-Verpflichtungen im Notstandsfall zulaessig ist"
    reference = "SR 0.101 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        notstand = person('emrk_notstand_krieg', period)
        erfordert = person('emrk_abweichung_lage_erfordert', period)
        return notstand * erfordert


class emrk_notstandsfeste_rechte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die notstandsfesten Rechte (Art. 2 bei Krieg, Art. 3, Art. 4 Abs. 1, Art. 7) gelten"
    reference = "SR 0.101 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)
