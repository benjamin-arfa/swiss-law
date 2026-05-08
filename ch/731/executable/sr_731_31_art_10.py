"""SR 731.31 Art. 10

Generated from: ch/731/de/731.31.md

Obligations of the borrower during loan utilisation.
Prohibitions: no dividends, no capital repayments, no loans to owners.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_darlehen_in_anspruch(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Unternehmen nimmt Darlehen nach FiREVO in Anspruch"
    reference = "SR 731.31 Art. 10 Abs. 1"


class firevo_dividendenverbot(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dividenden- und Tantiemenverbot waehrend Darlehensinanspruchnahme"
    reference = "SR 731.31 Art. 10 Abs. 1 lit. a"

    def formula(person, period, parameters):
        """Art. 10 Abs. 1 lit. a: No dividends/bonuses to persons
        outside the borrower's group during loan utilisation."""
        return person('firevo_darlehen_in_anspruch', period)


class firevo_kapitaleinlagen_verbot(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Verbot der Kapitaleinlagenrueckerstattung waehrend Darlehensinanspruchnahme"
    reference = "SR 731.31 Art. 10 Abs. 1 lit. b"

    def formula(person, period, parameters):
        """Art. 10 Abs. 1 lit. b: No repayment of capital contributions
        from the top group company."""
        return person('firevo_darlehen_in_anspruch', period)


class firevo_veraeusserung_schwelle(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Schwelle fuer meldepflichtige Veraeusserungen (CHF)"
    reference = "SR 731.31 Art. 10 Abs. 3"
    default_value = 50000000.0  # CHF 50 million
