"""SR 0.101.094 Art. 21

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY

class MaxTermJudge(Variable):
        def __init__(self, society):
            super(MaxTermJudge, self).__init__(
                name = "max_term_judge",
                label = "Maximum term of office for a judge",
                entity = society,
                definition = self.definition,
                default_table = [
                    ("person", "period"),
                    (0, ETERNITY, 0)
                ]
            )

        definition = Definition()
        definition.add_formula(
            "base",
            """
                E(period - E(period) >= E(period - start_period(initial_term)) <= E(period)) * 9
                + (E(period - start_period(initial_term)) > E(period))
                  * min(9, start_term(initial_term) + 2)
            """,
            period = "year",
            start = "first_of"
        )
