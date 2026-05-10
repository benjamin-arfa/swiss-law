"""SR 642.116 Art. 5

Generated from: ch/642/de/642.116.md

Art. 5: Lump-sum deduction (Pauschalabzug)

Instead of actual costs for maintenance, restoration, third-party
management, energy-saving investments, demolition costs, and insurance
premiums, a taxpayer may claim a lump-sum deduction:

a. Building <= 10 years old at start of tax period: 10% of gross rental
   income / imputed rental value
b. Building > 10 years old: 20% of gross rental income / imputed rental value

Excluded if the property is primarily used commercially by third parties (Abs. 3).
The taxpayer may choose between actual costs and lump-sum per property
per tax period (Abs. 4).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class liegenschaft_gebaeudealter_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter des Gebaeudes in Jahren zu Beginn der Steuerperiode"
    reference = "SR 642.116 Art. 5 Abs. 2"


class liegenschaft_bruttomietertrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Brutto-Mietertrag bzw. Brutto-Eigenmietwert der Liegenschaft (CHF)"
    reference = "SR 642.116 Art. 5 Abs. 2"


class liegenschaft_vorwiegend_geschaeftlich_dritte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Liegenschaft wird von Dritten vorwiegend geschaeftlich genutzt"
    reference = "SR 642.116 Art. 5 Abs. 3"
    default_value = False


class liegenschaft_pauschalabzug_gewaehlt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerpflichtige Person waehlt den Pauschalabzug statt tatsaechliche Kosten"
    reference = "SR 642.116 Art. 5 Abs. 4"


class liegenschaft_pauschalabzug_satz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschalabzugsatz (0.10 oder 0.20)"
    reference = "SR 642.116 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        alter = person('liegenschaft_gebaeudealter_jahre', period)
        p = parameters(period).sr_642_116

        return where(
            alter <= 10,
            p.pauschalabzug_satz_bis_10_jahre,
            p.pauschalabzug_satz_ueber_10_jahre
        )


class liegenschaft_pauschalabzug(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschalabzug fuer Liegenschaftskosten (CHF)"
    reference = "SR 642.116 Art. 5"

    def formula(person, period, parameters):
        bruttomietertrag = person('liegenschaft_bruttomietertrag', period)
        pauschal_gewaehlt = person('liegenschaft_pauschalabzug_gewaehlt', period)
        geschaeftlich = person('liegenschaft_vorwiegend_geschaeftlich_dritte', period)
        satz = person('liegenschaft_pauschalabzug_satz', period)

        # Art. 5 Abs. 3: excluded if primarily commercial use by third parties
        # Art. 5 Abs. 4: only if taxpayer chooses lump-sum
        abzug = bruttomietertrag * satz
        return abzug * pauschal_gewaehlt * (1 - geschaeftlich)
