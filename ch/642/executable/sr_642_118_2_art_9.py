"""SR 642.118.2 Art. 9

Generated from: ch/642/de/642.118.2.md

Art. 9: Obligatorische nachtraegliche ordentliche Veranlagung -
Mandatory subsequent ordinary assessment when gross income from employment
reaches at least CHF 120,000 per year.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class quellensteuer_bruttoeinkommen_unselbstaendig(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bruttoeinkommen aus unselbstaendiger Erwerbstaetigkeit (CHF/Jahr)"
    reference = "SR 642.118.2 Art. 9 Abs. 2"


class quellensteuer_ehepartner_bruttoeinkommen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bruttoeinkommen des Ehepartners aus unselbstaendiger Erwerbstaetigkeit (CHF/Jahr)"
    reference = "SR 642.118.2 Art. 9 Abs. 3"


class quellensteuer_obligatorische_ordentliche_veranlagung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Obligatorische nachtraegliche ordentliche Veranlagung "
        "(Bruttoeinkommen >= 120'000 CHF)"
    )
    reference = "SR 642.118.2 Art. 9"

    def formula(person, period, parameters):
        bruttoeinkommen = person('quellensteuer_bruttoeinkommen_unselbstaendig', period)
        ehepartner_einkommen = person('quellensteuer_ehepartner_bruttoeinkommen', period)
        verheiratet = person('quellensteuer_zivilstand', period) == 2

        mindestbetrag = 120000  # CHF

        # Abs. 1: Person selbst >= 120'000
        eigenes_ueber_schwelle = bruttoeinkommen >= mindestbetrag

        # Abs. 3: Bei Zweiverdienern genuegt, wenn einer der Eheleute >= 120'000
        ehepartner_ueber_schwelle = verheiratet * (ehepartner_einkommen >= mindestbetrag)

        return eigenes_ueber_schwelle + ehepartner_ueber_schwelle
