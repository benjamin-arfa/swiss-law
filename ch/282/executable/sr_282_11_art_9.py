"""SR 282.11 Art. 9 - Verwaltungsvermoegen

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class vermoegenswert_dient_unmittelbar_oeffentlichen_aufgaben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vermoegenswert dient unmittelbar der Erfuellung oeffentlicher Aufgaben"
    reference = "SR 282.11 Art. 9 Abs. 1"


class vermoegenswert_ist_steuerforderung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vermoegenswert ist eine Steuerforderung"
    reference = "SR 282.11 Art. 9 Abs. 2"


# Computed variables

class verwaltungsvermoegen_unpfaendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vermoegenswert ist unpfaendbar (Verwaltungsvermoegen oder Steuerforderung)"
    reference = "SR 282.11 Art. 9"

    def formula(self, period, parameters):
        oeffentlich = self('vermoegenswert_dient_unmittelbar_oeffentlichen_aufgaben', period)
        steuer = self('vermoegenswert_ist_steuerforderung', period)
        return oeffentlich + steuer > 0
