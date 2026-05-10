"""SR 642.11 Art. 25

Generated from: ch/642/de/642.11.md

Art. 25 Reineinkommen (Net income principle):
To determine the net income (Reineinkommen), the following are deducted
from total taxable income:
- Expenses and general deductions according to Art. 26-33a.

This is the central provision connecting gross income to net income
by allowing all deductions specified in Articles 26 through 33a.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gesamte_steuerbare_einkuenfte(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte steuerbare Einkuenfte vor Abzuegen (CHF)"
    reference = "SR 642.11 Art. 25"


class aufwendungen_art_26_bis_33a(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufwendungen und allgemeine Abzuege nach Art. 26-33a (CHF)"
    reference = "SR 642.11 Art. 25, Art. 26-33a"


class reineinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Reineinkommen (gesamte steuerbare Einkuenfte minus Aufwendungen, CHF)"
    reference = "SR 642.11 Art. 25"

    def formula(person, period, parameters):
        einkuenfte = person('gesamte_steuerbare_einkuenfte', period)
        abzuege = person('aufwendungen_art_26_bis_33a', period)
        return max_(einkuenfte - abzuege, 0)
