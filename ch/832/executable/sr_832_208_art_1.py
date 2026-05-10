"""SR 832.208 Art. 1

Generated from: ch/832/de/832.208.md

Prämienzuschlag für Verhütung von Berufsunfällen und Berufskrankheiten.
Base rate: 6.5% of net premiums for occupational accident insurance.
Reduced rates for partially exempt businesses based on share of non-subject
payroll (table in Abs. 2).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class uv_praemienzuschlag_berufsunfall(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prämienzuschlag für Verhütung von Berufsunfällen und Berufskrankheiten (Anteil)"
    reference = "SR 832.208 Art. 1"

    def formula_1984(person, period, parameters):
        import numpy as np

        anteil_nicht_unterstellt = person(
            'uv_anteil_nicht_unterstellte_lohnsumme', period
        )
        teilweise_unterstellt = person(
            'uv_betrieb_teilweise_unterstellt', period
        )

        p = parameters(period).sr832_208

        # Full rate for fully subject businesses
        voller_satz = p.praemienzuschlag_berufsunfall_basis

        # Graduated rates for partially exempt businesses (Art. 1 Abs. 2)
        abgestufter_satz = np.select(
            [
                anteil_nicht_unterstellt < 0.10,
                (anteil_nicht_unterstellt >= 0.10) & (anteil_nicht_unterstellt < 0.26),
                (anteil_nicht_unterstellt >= 0.26) & (anteil_nicht_unterstellt < 0.42),
                (anteil_nicht_unterstellt >= 0.42) & (anteil_nicht_unterstellt < 0.58),
                (anteil_nicht_unterstellt >= 0.58) & (anteil_nicht_unterstellt < 0.74),
                (anteil_nicht_unterstellt >= 0.74) & (anteil_nicht_unterstellt < 0.90),
                anteil_nicht_unterstellt >= 0.90,
            ],
            [
                p.staffelung.stufe_unter_10,
                p.staffelung.stufe_ab_10,
                p.staffelung.stufe_ab_26,
                p.staffelung.stufe_ab_42,
                p.staffelung.stufe_ab_58,
                p.staffelung.stufe_ab_74,
                p.staffelung.stufe_ab_90,
            ],
            default=voller_satz
        )

        return np.where(teilweise_unterstellt, abgestufter_satz, voller_satz)


class uv_anteil_nicht_unterstellte_lohnsumme(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der prämienpflichtigen Lohnsumme der nicht unterstellten Arbeiten"
    reference = "SR 832.208 Art. 1 Abs. 2"


class uv_betrieb_teilweise_unterstellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrieb ist den Vorschriften über Arbeitssicherheit nur teilweise unterstellt"
    reference = "SR 832.208 Art. 1 Abs. 2, SR 832.30 Art. 2 Abs. 2-3"
