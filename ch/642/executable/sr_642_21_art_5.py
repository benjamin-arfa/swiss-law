"""SR 642.21 Art. 5 - Ausnahmen von der Steuer (Tax Exemptions for Capital Income)

Generated from: ch/642/de/642.21.md

Art. 5 Abs. 1 Bst. c: Interest on customer deposits is exempt if
the interest amount does not exceed CHF 200 per calendar year.
Art. 5 Abs. 1bis: Return of reserves from capital contributions
(Kapitaleinlageprinzip) is treated like return of share capital
if reported on a separate account.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vstg_zinsen_kundenguthaben(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zinsen auf Kundenguthaben bei inlaendischen Banken/Sparkassen (CHF)"
    reference = "SR 642.21 Art. 5 Abs. 1 Bst. c"
    default_value = 0.0


class vstg_zinsen_steuerfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zinsen auf Kundenguthaben von der Verrechnungssteuer befreit sind (unter CHF 200)"
    reference = "SR 642.21 Art. 5 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        zinsen = person('vstg_zinsen_kundenguthaben', period)
        schwelle = parameters(period).sr_642_21.zinsen_freigrenze
        return zinsen <= schwelle


class vstg_reserven_kapitaleinlagen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Rueckzahlung von Reserven aus Kapitaleinlagen (CHF)"
    reference = "SR 642.21 Art. 5 Abs. 1bis"
    default_value = 0.0


class vstg_kapitaleinlagen_auf_separatem_konto(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Reserven aus Kapitaleinlagen auf gesondertem Konto in Handelsbilanz ausgewiesen sind"
    reference = "SR 642.21 Art. 5 Abs. 1bis"


class vstg_kapitaleinlagen_steuerfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Rueckzahlung von Kapitaleinlagen der Rueckzahlung von Grund-/Stammkapital gleichgestellt wird"
    reference = "SR 642.21 Art. 5 Abs. 1bis"

    def formula(person, period, parameters):
        auf_konto = person('vstg_kapitaleinlagen_auf_separatem_konto', period)
        # Tax-free if reported on a separate account and changes reported to ESTV
        return auf_konto
