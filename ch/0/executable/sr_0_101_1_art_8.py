"""SR 0.101.1 Art. 8

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core.variables import Variable
from openfisca_core.formulas import any_of, as_year
from openfisca_core.periods import ETERNITY
from openfisca_core.reindex import reindex

class member_states(rating):
    definition = [
        'share',
        ((any_of(
            (signing_date == current_year)
            | (ratification_date == current_year),
            (signing_date == previous_year)
            | (ratification_date == previous_year)
        )),
        ETERNITY )
    ]
    label = "Member states that have signed and ratified the treaty"
    reference = "Art. 8 SR 0.101.1"

class treaty_in_force(rating):
    definition = [
        'share',
        (
            as_year(
                reindex(
                    (
                        (five_member_states
                        > 5)
                        | (
                            (
                                (signing_date == current_year)
                                | (signing_date == previous_year)
                            )
                            & ((5 <= member_states) | all_of((~ (5 <= member_states))))
                        )
                    ),
                    period,
                )
            ),
            period
        )
    ]
    label = "Treaty in force"
    reference = "Art. 8 SR 0.101.1"
    entity = 'country'
