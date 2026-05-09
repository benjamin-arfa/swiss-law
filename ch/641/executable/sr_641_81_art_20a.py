"""SR 641.81 Art. 20a - Gefährdung der Abgabe (Procedural violation penalties)

Heavy Vehicle Tax Act (SVAG) - Penalties for endangering the tax through
violation of procedural duties.
Art. 20a:
  Abs. 1: Intentional violation: fine up to 20'000 CHF
  Abs. 2: Negligent violation: fine up to 10'000 CHF

Generated from: ch/641/de/641.81.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class svag_verfahrenspflicht_verletzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether procedural duties were violated (SR 641.81 Art. 20a)"
    reference = "SR 641.81 Art. 20a"
    default_value = False


class svag_verfahrenspflicht_vorsaetzlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the procedural violation was intentional (SR 641.81 Art. 20a Abs. 1)"
    reference = "SR 641.81 Art. 20a"
    default_value = False


class svag_busse_verfahrenspflicht(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximum fine for procedural violations in CHF (SR 641.81 Art. 20a)"
    reference = "SR 641.81 Art. 20a"

    def formula(person, period, parameters):
        verletzt = person("svag_verfahrenspflicht_verletzt", period)
        vorsaetzlich = person("svag_verfahrenspflicht_vorsaetzlich", period)

        # Intentional: max 20'000 CHF; negligent: max 10'000 CHF
        max_busse = where(vorsaetzlich, 20000.0, 10000.0)
        return where(verletzt, max_busse, 0.0)
