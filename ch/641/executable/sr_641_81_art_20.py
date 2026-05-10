"""SR 641.81 Art. 20 - Hinterziehung der Abgabe (Tax evasion penalties)

Heavy Vehicle Tax Act (SVAG) - Penalties for tax evasion.
Art. 20:
  Abs. 1: Intentional evasion: fine up to 5x the evaded tax
  Abs. 2: Negligent evasion: fine up to 3x the evaded tax
  Abs. 3: Attempt is punishable

Generated from: ch/641/de/641.81.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class svag_hinterzogene_abgabe(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amount of evaded heavy vehicle tax in CHF (SR 641.81 Art. 20)"
    reference = "SR 641.81 Art. 20"
    default_value = 0.0


class svag_hinterziehung_vorsaetzlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the tax evasion was intentional (SR 641.81 Art. 20 Abs. 1)"
    reference = "SR 641.81 Art. 20"
    default_value = False


class svag_busse_hinterziehung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximum fine for tax evasion in CHF (SR 641.81 Art. 20)"
    reference = "SR 641.81 Art. 20"

    def formula(person, period, parameters):
        hinterzogen = person("svag_hinterzogene_abgabe", period)
        vorsaetzlich = person("svag_hinterziehung_vorsaetzlich", period)

        # Intentional: up to 5x; negligent: up to 3x
        multiplikator = where(vorsaetzlich, 5.0, 3.0)
        return hinterzogen * multiplikator
