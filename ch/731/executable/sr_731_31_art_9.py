"""SR 731.31 Art. 9

Generated from: ch/731/de/731.31.md

Loan draw by the borrower - conditions for disbursement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_nicht_ueberschuldet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Unternehmen ist nicht ueberschuldet"
    reference = "SR 731.31 Art. 9 Abs. 3 lit. a Ziff. 1"


class firevo_auszahlung_berechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Voraussetzungen fuer Auszahlung des Darlehens erfuellt"
    reference = "SR 731.31 Art. 9 Abs. 3"

    def formula(person, period, parameters):
        """Art. 9 Abs. 3: UVEK authorises disbursement if:
        a. the company: 1. is not over-indebted, 2. has taken all
           reasonable self-help measures;
        b. unforeseen developments lead to a liquidity shortfall;
        c. illiquidity or over-indebtedness threatening electricity
           supply is imminent.
        """
        nicht_ueberschuldet = person('firevo_nicht_ueberschuldet', period)
        selbsthilfe = person('firevo_selbsthilfemassnahmen_getroffen', period)
        engpass = person('firevo_liquiditaetsengpass', period)

        return nicht_ueberschuldet * selbsthilfe * engpass
