"""SR 0.672.916.311 Art. 2 - Eligibility for tax relief

Art. 2: Beneficiary of dividends, interest, or royalties is entitled to
tax relief if at the time of payment they:
- Reside in the other contracting state
- Have beneficial ownership of the capital/rights
- Are not excluded under Art. 28 par. 6 and 7 of the convention

Generated from: ch/0/fr/0.672.916.311.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class reside_dans_autre_etat_contractant(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person resides in the other contracting state at time of income (Art. 2)"
    default_value = False


class droit_jouissance_placements(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person has beneficial ownership of the capital investments (Art. 2)"
    default_value = True


class exclu_degrevement_art28(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person excluded from relief per Art. 28 par. 6-7 of the convention (Art. 2)"
    default_value = False


class eligible_degrevement_ch_at(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person is eligible for CH-AT tax relief (Art. 2)"

    def formula(person, period, parameters):
        reside = person("reside_dans_autre_etat_contractant", period)
        jouissance = person("droit_jouissance_placements", period)
        exclu = person("exclu_degrevement_art28", period)
        return reside * jouissance * not_(exclu)
