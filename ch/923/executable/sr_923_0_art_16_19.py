"""SR 923.0 Art. 16-19

Generated from: ch/923/de/923.0.md

Art. 16: Vergehen - Criminal offenses:
- Monetary penalty for intentionally harming fish/crayfish stocks through:
  a. unauthorized technical interventions; b. violating permit conditions;
  c. importing/introducing non-native species without permit; d. using non-native bait
- Negligent acts: fine up to CHF 20,000

Art. 17: Übertretungen - Misdemeanors:
- Fine up to CHF 20,000 for: a. violating conservation rules;
  b. receiving illegally obtained fish; c. other violations

Art. 19: Verbot der Fischereiausübung - Fishing ban:
- Court may ban fishing for up to 5 years upon offense conviction
  (if risk of repetition)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
import numpy as np


class bgf_vergehen_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vorsätzliches Fischereivergehen nach Art. 16 begangen"
    reference = "SR 923.0 Art. 16 Abs. 1"


class bgf_vergehen_fahrlaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrlässiges Fischereivergehen nach Art. 16 begangen"
    reference = "SR 923.0 Art. 16 Abs. 2"


class bgf_uebertretung_begangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Übertretung nach Art. 17 begangen"
    reference = "SR 923.0 Art. 17 Abs. 1"


class bgf_max_busse_fahrlaessig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse bei fahrlässigem Vergehen (CHF)"
    reference = "SR 923.0 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        fahrlaessig = person('bgf_vergehen_fahrlaessig', period)
        return fahrlaessig * 20000.0


class bgf_max_busse_uebertretung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse bei Übertretung (CHF)"
    reference = "SR 923.0 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        uebertretung = person('bgf_uebertretung_begangen', period)
        return uebertretung * 20000.0


class bgf_wiederholungsgefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gefahr weiterer Straftaten besteht"
    reference = "SR 923.0 Art. 19 Abs. 1"


class bgf_fischereiverbot_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gerichtliches Verbot der Fischereiausübung möglich (bis 5 Jahre)"
    reference = "SR 923.0 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        vergehen = person('bgf_vergehen_vorsaetzlich', period)
        uebertretung = person('bgf_uebertretung_begangen', period)
        wiederholung = person('bgf_wiederholungsgefahr', period)
        # Possible for offenses or serious/repeated misdemeanors, if risk of repetition
        return (vergehen + uebertretung) * wiederholung > 0


class bgf_fischereiverbot_max_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Dauer des Fischereiverbots (Jahre)"
    reference = "SR 923.0 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        moeglich = person('bgf_fischereiverbot_moeglich', period)
        return moeglich * 5
