"""SR 282.11 Art. 7 - Pfaendbares Vermoegen

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class vermoegenswert_ist_finanzvermoegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vermoegenswert gehoert zum Finanzvermoegen des Gemeinwesens"
    reference = "SR 282.11 Art. 7 Abs. 1"


class vermoegenswert_ist_verwaltungsvermoegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vermoegenswert ist Verwaltungsvermoegen (dient unmittelbar oeffentlichen Aufgaben)"
    reference = "SR 282.11 Art. 7 Abs. 2"


class dingliches_recht_dritter_besteht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es besteht ein dingliches Recht eines Dritten am Vermoegenswert"
    reference = "SR 282.11 Art. 7 Abs. 1"


# Computed variables

class vermoegenswert_ist_pfaendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vermoegenswert ist pfaendbar"
    reference = "SR 282.11 Art. 7"

    def formula(self, period, parameters):
        finanzvermoegen = self('vermoegenswert_ist_finanzvermoegen', period)
        # Pfaendbar: alles Finanzvermoegen, unter Vorbehalt dinglicher Rechte
        return finanzvermoegen
