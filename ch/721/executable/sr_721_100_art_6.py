"""SR 721.100 Art. 6

Generated from: ch/721/de/721.100.md

Art. 6 - Federal compensations for flood protection:
5. Contribution to eligible costs:
   - Data acquisition (Grundlagenbeschaffung): 50%
   - Measures: 35%
6. The contribution for measures may be increased:
   a. by up to 10% for extra performance (Mehrleistungen)
   b. by up to 20% if a canton is significantly burdened by extraordinary
      natural hazard protection measures (especially after storm damage)
4. Costs are eligible if actually incurred and directly necessary for
   appropriate task fulfillment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wbg_anrechenbare_kosten_grundlagen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eligible costs for data acquisition / Grundlagenbeschaffung (CHF)"
    reference = "SR 721.100 Art. 6 Abs. 3-4"


class wbg_anrechenbare_kosten_massnahmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eligible costs for flood protection measures (CHF)"
    reference = "SR 721.100 Art. 6 Abs. 3-4"


class wbg_mehrleistung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the project qualifies for extra performance surcharge"
    reference = "SR 721.100 Art. 6 Abs. 6 Bst. a"


class wbg_ausserordentlich_belastet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the canton is significantly burdened by extraordinary natural hazard measures"
    reference = "SR 721.100 Art. 6 Abs. 6 Bst. b"


class wbg_abgeltung_grundlagen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Federal compensation for data acquisition (CHF)"
    reference = "SR 721.100 Art. 6 Abs. 5"

    def formula(person, period, parameters):
        kosten = person('wbg_anrechenbare_kosten_grundlagen', period)
        satz = parameters(period).sr_721_100.abgeltung_grundlagen_satz

        return kosten * satz


class wbg_abgeltung_massnahmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Federal compensation for flood protection measures (CHF)"
    reference = "SR 721.100 Art. 6 Abs. 5-6"

    def formula(person, period, parameters):
        kosten = person('wbg_anrechenbare_kosten_massnahmen', period)
        mehrleistung = person('wbg_mehrleistung', period)
        ausserordentlich = person('wbg_ausserordentlich_belastet', period)
        p = parameters(period).sr_721_100

        basis_satz = p.abgeltung_massnahmen_satz
        zuschlag_mehr = p.abgeltung_mehrleistung_zuschlag
        zuschlag_ao = p.abgeltung_ausserordentlich_zuschlag

        effektiver_satz = basis_satz + mehrleistung * zuschlag_mehr + ausserordentlich * zuschlag_ao

        return kosten * effektiver_satz
