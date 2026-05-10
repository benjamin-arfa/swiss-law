"""SR 642.11 Art. 36

Generated from: ch/642/fr/642.11.md

Art. 36 Barèmes (Tax rate schedules) for federal direct tax on income:
- Abs. 1: Schedule for single taxpayers (Grundtarif)
- Abs. 2: Schedule for married couples (Verheiratetentarif)
- Abs. 2bis: Family tariff applies the married schedule with a CHF 263
  reduction per child/dependent
- Abs. 3: Tax amounts below CHF 25 are not collected

Tax brackets (2026, adjusted for cold progression per O DFF 10.09.2025):

Single (Art. 36 Abs. 1):
  up to   15,200 →     0.00  then 0.77% per 100
  at      33,200 →   138.60  then 0.88% per 100
  at      43,500 →   229.20  then 2.64% per 100
  at      58,000 →   612.00  then 2.97% per 100
  at      76,200 → 1,152.50  then 5.94% per 100
  at      82,100 → 1,502.95  then 6.60% per 100
  at     108,900 → 3,271.75  then 8.80% per 100
  at     141,500 → 6,140.55  then 11.00% per 100
  at     185,100 →10,936.55  then 13.20% per 100
  at     793,900 →91,298.15  (anchor)
  at     794,000 →91,310.00  then 11.50% per 100

Married (Art. 36 Abs. 2):
  up to   29,700 →     0.00  then 1.00% per 100
  at      53,400 →   237.00  then 2.00% per 100
  at      61,300 →   395.00  then 3.00% per 100
  at      79,100 →   929.00  then 4.00% per 100
  at      94,900 → 1,561.00  then 5.00% per 100
  at     108,700 → 2,251.00  then 6.00% per 100
  at     120,600 → 2,965.00  then 7.00% per 100
  at     130,500 → 3,658.00  then 8.00% per 100
  at     138,400 → 4,290.00  then 9.00% per 100
  at     144,300 → 4,821.00  then 10.00% per 100
  at     148,300 → 5,221.00  then 11.00% per 100
  at     150,400 → 5,452.00  then 12.00% per 100
  at     152,400 → 5,692.00  then 13.00% per 100
  at     941,300 →108,249.00 (anchor)
  at     941,400 →108,261.00 then 11.50% per 100
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Tax bracket computation helpers ---

# Single tariff brackets (2026): (threshold, base_tax, marginal_rate_per_100_CHF)
BRACKETS_SINGLE_2026 = [
    (0,       0.00,     0.0000),
    (15200,   0.00,     0.0077),
    (33200,   138.60,   0.0088),
    (43500,   229.20,   0.0264),
    (58000,   612.00,   0.0297),
    (76200,   1152.50,  0.0594),
    (82100,   1502.95,  0.0660),
    (108900,  3271.75,  0.0880),
    (141500,  6140.55,  0.1100),
    (185100,  10936.55, 0.1320),
    (794000,  91310.00, 0.1150),
]

# Married tariff brackets (2026): (threshold, base_tax, marginal_rate_per_100_CHF)
BRACKETS_MARRIED_2026 = [
    (0,       0.00,     0.0000),
    (29700,   0.00,     0.0100),
    (53400,   237.00,   0.0200),
    (61300,   395.00,   0.0300),
    (79100,   929.00,   0.0400),
    (94900,   1561.00,  0.0500),
    (108700,  2251.00,  0.0600),
    (120600,  2965.00,  0.0700),
    (130500,  3658.00,  0.0800),
    (138400,  4290.00,  0.0900),
    (144300,  4821.00,  0.1000),
    (148300,  5221.00,  0.1100),
    (150400,  5452.00,  0.1200),
    (152400,  5692.00,  0.1300),
    (941400,  108261.00, 0.1150),
]


def _compute_tax_from_brackets(revenu, brackets):
    """Compute tax using progressive bracket schedule.

    Args:
        revenu: numpy array of taxable incomes
        brackets: list of (threshold, base_tax, marginal_rate) tuples

    Returns:
        numpy array of computed tax amounts
    """
    tax = np.zeros_like(revenu, dtype=float)

    for i in range(len(brackets) - 1, -1, -1):
        threshold, base_tax, rate = brackets[i]
        mask = revenu >= threshold
        if i == len(brackets) - 1:
            # Top bracket
            tax = np.where(
                mask,
                base_tax + (revenu - threshold) * rate,
                tax
            )
        else:
            next_threshold = brackets[i + 1][0]
            mask_this = mask & (revenu < next_threshold)
            tax = np.where(
                mask_this,
                base_tax + (revenu - threshold) * rate,
                tax
            )

    return tax


class ifd_revenu_imposable(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taxable income for federal direct tax after all deductions (CHF)"
    reference = "SR 642.11 Art. 25, 35, 36"


class ifd_tarif_famille(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the family tariff applies (widowed/separated/divorced/single with children)"
    reference = "SR 642.11 Art. 36 Abs. 2bis"


class ifd_impot_revenu_brut(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gross federal income tax before minimum threshold (CHF)"
    reference = "SR 642.11 Art. 36"

    def formula(person, period, parameters):
        revenu = person('ifd_revenu_imposable', period)
        marie = person('ifd_marie_menage_commun', period)
        tarif_famille = person('ifd_tarif_famille', period)
        nb_enfants = person('ifd_nombre_enfants', period)
        nb_pers = person('ifd_nombre_personnes_a_charge', period)

        p = parameters(period).sr_642_11

        # Use married schedule for married couples and family tariff
        use_married = marie + tarif_famille

        tax_single = _compute_tax_from_brackets(revenu, BRACKETS_SINGLE_2026)
        tax_married = _compute_tax_from_brackets(revenu, BRACKETS_MARRIED_2026)

        tax = where(use_married, tax_married, tax_single)

        # Art. 36(2bis): reduction per child/dependent for family tariff
        reduction = where(tarif_famille,
                          (nb_enfants + nb_pers) * p.reduction_per_child,
                          0)
        tax = max_(tax - reduction, 0)

        return tax


class ifd_impot_revenu(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Federal income tax due (CHF), after minimum threshold"
    reference = "SR 642.11 Art. 36"

    def formula(person, period, parameters):
        impot_brut = person('ifd_impot_revenu_brut', period)
        seuil = parameters(period).sr_642_11.minimum_tax

        # Art. 36(3): amounts below CHF 25 are not collected
        return where(impot_brut < seuil, 0, impot_brut)
