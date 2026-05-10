"""SR 981.1 Art. 20 - Abstimmungen

Generated from: ch/981/de/981.1.md

Beschluesse mit einfacher Mehrheit. Bei Stimmengleichheit
Stichentscheid des Vorsitzenden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class stimmen_dafuer(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Stimmen dafuer"
    reference = "SR 981.1 Art. 20 Abs. 2"


class stimmen_dagegen(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Stimmen dagegen"
    reference = "SR 981.1 Art. 20 Abs. 2"


class vorsitzender_stimmt_dafuer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Der Vorsitzende stimmt dafuer (Stichentscheid)"
    reference = "SR 981.1 Art. 20 Abs. 2"


class beschluss_angenommen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Der Beschluss ist mit einfacher Mehrheit angenommen"
    reference = "SR 981.1 Art. 20 Abs. 2"

    def formula(self, period, parameters):
        dafuer = self('stimmen_dafuer', period)
        dagegen = self('stimmen_dagegen', period)
        stichentscheid = self('vorsitzender_stimmt_dafuer', period)
        # Einfache Mehrheit; bei Stimmengleichheit Stichentscheid
        return (dafuer > dagegen) + ((dafuer == dagegen) * stichentscheid)
