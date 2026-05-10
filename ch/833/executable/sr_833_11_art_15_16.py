"""SR 833.11 Art. 15 & 16

Generated from: ch/833/de/833.11.md

Art. 15: Höchstbetrag des versicherten Jahresverdienstes:
- Maximum insured annual earnings for daily allowance and disability pension:
  CHF 163,722 (as of 2025)
- Earnings exceeding this amount are not considered

Art. 16: Versicherter Verdienst beim Taggeld - Insured earnings for daily allowance:
1. Insured earnings = sum of main and secondary income, annualized and divided by 365
2. Employees: salary before employee social insurance deductions (no employer contributions)
3. Self-employed: net business income
4. Regular supplementary income (overtime, Sunday/night/shift work, danger pay) included
5. Homemakers: imputed salary for equivalent outside help
6. Independent farmers: determined by experience values based on usable area, altitude, livestock
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mvv_jahresverdienst_brutto(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Brutto-Jahresverdienst aus Haupt- und Nebenerwerb (CHF)"
    reference = "SR 833.11 Art. 16 Abs. 1"


class mvv_ist_selbstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist selbständig erwerbend"
    reference = "SR 833.11 Art. 16 Abs. 3"


class mvv_ist_hausfrau_hausmann(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Hausfrau/Hausmann oder arbeitet ohne Normallohn im Familienbetrieb"
    reference = "SR 833.11 Art. 16 Abs. 5"


class mvv_ist_selbstaendiger_landwirt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist selbständiger Landwirt"
    reference = "SR 833.11 Art. 16 Abs. 6"


class mvv_versicherter_jahresverdienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherter Jahresverdienst (CHF, gedeckelt auf Höchstbetrag)"
    reference = "SR 833.11 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        brutto = person('mvv_jahresverdienst_brutto', period)
        hoechstbetrag = parameters(period).mvv.hoechstbetrag_jahresverdienst
        return np.minimum(brutto, hoechstbetrag)


class mvv_taggeld_versicherter_verdienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherter Tagesverdienst für Taggeldberechnung (CHF/Tag)"
    reference = "SR 833.11 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        jahresverdienst = person('mvv_versicherter_jahresverdienst', period)
        return jahresverdienst / 365
