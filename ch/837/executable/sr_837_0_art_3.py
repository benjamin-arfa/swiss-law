"""SR 837.0 Art. 3

Generated from: ch/837/de/837.0.md

Art. 3: Beitragsbemessung und Beitragssatz
- Abs. 1: Contributions are calculated per employment relationship based on
  the relevant salary under AHV legislation.
- Abs. 2: The contribution rate is 2.2% up to the maximum insured income
  of the mandatory accident insurance.
- Abs. 3: Employer and employee each pay half. Employees of non-contributing
  employers pay the full contribution.
- Abs. 4: For employment of less than one year, the annual maximum insured
  income is prorated.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alv_massgebender_lohn(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Massgebender Lohn im Sinne der AHV-Gesetzgebung (monatlich)"
    reference = "SR 837.0 Art. 3 Abs. 1"


class alv_beitrag_arbeitnehmer(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "ALV-Beitragsanteil des Arbeitnehmers"
    reference = "SR 837.0 Art. 3 Abs. 2-3"

    def formula(person, period, parameters):
        lohn = person('alv_massgebender_lohn', period)
        satz = parameters(period).alv.beitragssatz_arbeitnehmer
        return lohn * satz


class alv_beitrag_arbeitgeber(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "ALV-Beitragsanteil des Arbeitgebers"
    reference = "SR 837.0 Art. 3 Abs. 2-3"

    def formula(person, period, parameters):
        lohn = person('alv_massgebender_lohn', period)
        satz = parameters(period).alv.beitragssatz_arbeitgeber
        return lohn * satz


class alv_beitrag_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamter ALV-Beitrag (Arbeitnehmer + Arbeitgeber)"
    reference = "SR 837.0 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('alv_beitrag_arbeitnehmer', period)
            + person('alv_beitrag_arbeitgeber', period)
        )
