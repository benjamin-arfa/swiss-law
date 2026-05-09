"""SR 642.117.1 Art. 3

Generated from: ch/642/de/642.117.1.md

Art. 3: Measurement of income from self-employment
(Bemessung des Einkommens aus selbststaendiger Erwerbstaetigkeit)

Abs. 1: Self-employment income is based on each fiscal year completed
within the tax period (Art. 41 DBG).

Abs. 2: The fiscal year result is used at actual amount regardless
of calendar year.

Abs. 3: For rate determination:
- Full-year liability: no annualization
- Partial-year liability with partial fiscal year: annualize based on
  tax liability duration or fiscal year duration (whichever is longer)

Abs. 4: Partial-year liability with fiscal year >= 12 months:
ordinary profits are not annualized.

Abs. 5: Extraordinary items (capital gains, book value gains) are
never annualized for rate determination.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ifd_se_geschaeftsjahr_dauer_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer des Geschaeftsjahres in Monaten"
    reference = "SR 642.117.1 Art. 3 Abs. 1"
    default_value = 12


class ifd_se_ordentlicher_gewinn(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ordentlicher Gewinn aus selbststaendiger Erwerbstaetigkeit (CHF)"
    reference = "SR 642.117.1 Art. 3 Abs. 3"


class ifd_se_ausserordentliche_faktoren(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ausserordentliche Faktoren (Kapitalgewinne, Wertvermehrungen) (CHF)"
    reference = "SR 642.117.1 Art. 3 Abs. 5"
    default_value = 0


class ifd_se_satzbestimmendes_einkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Satzbestimmendes Einkommen aus selbststaendiger Erwerbstaetigkeit (CHF)"
    reference = "SR 642.117.1 Art. 3"

    def formula(person, period, parameters):
        dauer_steuerpflicht = person('ifd_dauer_steuerpflicht_monate', period)
        dauer_gj = person('ifd_se_geschaeftsjahr_dauer_monate', period)
        ordentlich = person('ifd_se_ordentlicher_gewinn', period)
        ausserordentlich = person('ifd_se_ausserordentliche_faktoren', period)

        # Abs. 3: Full year -> no annualization
        # Abs. 4: Partial year but GJ >= 12 months -> no annualization
        # Otherwise: annualize by longer of tax liability or fiscal year
        annualisierungs_basis = max_(dauer_steuerpflicht, dauer_gj)

        annualisiert = where(
            (dauer_steuerpflicht >= 12) + (dauer_gj >= 12),
            ordentlich,  # no annualization
            ordentlich * 12 / max_(annualisierungs_basis, 1)
        )

        # Abs. 5: extraordinary items are never annualized
        return annualisiert + ausserordentlich
