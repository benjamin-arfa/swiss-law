"""SR 922.0 Art. 16 & 17

Generated from: ch/922/de/922.0.md

Art. 16: Versicherung - Insurance for hunters:
- All hunting-authorized persons must take out liability insurance
- Federal Council sets the minimum coverage sum
- Injured party has direct claim against insurer up to contractual sum

Art. 17: Vergehen - Criminal offenses:
- Imprisonment up to 1 year or monetary penalty for intentional unauthorized hunting/killing
  of protected or huntable species, etc.
- Negligent acts: fine

Art. 18: Übertretungen - Misdemeanors:
- Fine up to CHF 20,000 for various violations
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jsg_haftpflichtversicherung_abgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Jagdberechtigte Person hat Haftpflichtversicherung abgeschlossen"
    reference = "SR 922.0 Art. 16 Abs. 1"


class jsg_versicherungspflicht_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherungspflicht für jagdberechtigte Person ist erfüllt"
    reference = "SR 922.0 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        jagdberechtigt = person('jsg_jagdberechtigung', period)
        versichert = person('jsg_haftpflichtversicherung_abgeschlossen', period)
        # Only applicable if person is hunting-authorized
        return jagdberechtigt * versichert + (1 - jagdberechtigt)


class jsg_vergehen_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vorsätzliches Jagdvergehen nach Art. 17 begangen"
    reference = "SR 922.0 Art. 17 Abs. 1"


class jsg_max_freiheitsstrafe_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Freiheitsstrafe in Monaten bei Vergehen nach Art. 17"
    reference = "SR 922.0 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        vorsaetzlich = person('jsg_vergehen_vorsaetzlich', period)
        # Up to 1 year (12 months) for intentional offenses
        return vorsaetzlich * 12


class jsg_uebertretung_max_busse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse bei Übertretung nach Art. 18 (CHF)"
    reference = "SR 922.0 Art. 18 Abs. 1"

    def formula(person, period, parameters):
        return person('jsg_vergehen_vorsaetzlich', period) * 0 + 20000.0
