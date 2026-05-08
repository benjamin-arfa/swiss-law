"""SR 731.31 Art. 7

Generated from: ch/731/de/731.31.md

Loan amount, interest rate, and risk surcharge.
- Market-rate interest plus risk surcharge
- Normal risk surcharge: 4-8% p.a. of drawn amount
- Violation risk surcharge: 5-10% p.a.
- Surcharge due upon expiry of the draw period
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_darlehensbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Bezogener Darlehensbetrag (CHF)"
    reference = "SR 731.31 Art. 7 Abs. 1"


class firevo_marktzins_satz(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Marktgerechter Zinssatz (Anteil, z.B. 0.02 fuer 2%)"
    reference = "SR 731.31 Art. 7 Abs. 2"


class firevo_pflicht_verstoss(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Verstoss gegen Pflichten/Auflagen/Bedingungen der Darlehensverfuegung"
    reference = "SR 731.31 Art. 7 Abs. 3"


class firevo_risikozuschlag_satz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Risikozuschlag-Satz (Anteil, z.B. 0.06 fuer 6%)"
    reference = "SR 731.31 Art. 7 Abs. 3"

    def formula(person, period, parameters):
        """Art. 7 Abs. 3:
        - Normal: 4-8% (use midpoint 6%)
        - With violation: 5-10% (use midpoint 7.5%)
        """
        verstoss = person('firevo_pflicht_verstoss', period.first_month)

        normal_satz = 0.06    # midpoint of 4-8%
        verstoss_satz = 0.075  # midpoint of 5-10%

        return where(verstoss, verstoss_satz, normal_satz)


class firevo_risikozuschlag_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Risikozuschlag-Betrag (CHF p.a.)"
    reference = "SR 731.31 Art. 7 Abs. 3-4"

    def formula(person, period, parameters):
        betrag = person('firevo_darlehensbetrag', period.first_month)
        satz = person('firevo_risikozuschlag_satz', period)
        return betrag * satz


class firevo_zinskosten_total(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Totale jaehrliche Zinskosten inkl. Risikozuschlag (CHF)"
    reference = "SR 731.31 Art. 7"

    def formula(person, period, parameters):
        betrag = person('firevo_darlehensbetrag', period.first_month)
        marktzins = person('firevo_marktzins_satz', period.first_month)
        risiko = person('firevo_risikozuschlag_betrag', period)
        return betrag * marktzins + risiko
