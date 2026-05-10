"""SR 837.21 Art. 21 - Ermittlung des Reinvermoegens (Determining net assets)

Net assets = gross assets minus proven debts.
- Mortgage debts max deductible up to property value
- For owner-occupied property, deduct in order:
  a. tax-free amount per Art. 10(1)(c) UeLG
  b. mortgage debts up to remaining property value after deduction a
- BVG pension assets of entitled person are NOT included in net assets

Generated from: ch/837/de/837.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class uelv_bruttovermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bruttovermoegen in CHF (Art. 21 Abs. 1 UeLV)"
    reference = "SR 837.21 Art. 21 Abs. 1"


class uelv_schulden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Nachgewiesene Schulden in CHF (Art. 21 Abs. 1 UeLV)"
    reference = "SR 837.21 Art. 21 Abs. 1"


class uelv_liegenschaftswert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wert der selbstbewohnten Liegenschaft in CHF (Art. 21 Abs. 3 UeLV)"
    reference = "SR 837.21 Art. 21 Abs. 3"


class uelv_hypothekarschulden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hypothekarschulden in CHF (Art. 21 Abs. 2 UeLV)"
    reference = "SR 837.21 Art. 21 Abs. 2"


class uelv_freibetrag_liegenschaft(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Freibetrag nach Art. 10 Abs. 1 Bst. c UeLG in CHF (Art. 21 Abs. 3 Bst. a UeLV)"
    reference = "SR 837.21 Art. 21 Abs. 3 Bst. a"


class uelv_reinvermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Reinvermoegen fuer Ueberbrueckungsleistungen in CHF (Art. 21 UeLV)"
    reference = "SR 837.21 Art. 21"

    def formula(person, period, parameters):
        brutto = person('uelv_bruttovermoegen', period)
        schulden = person('uelv_schulden', period)
        liegenschaft = person('uelv_liegenschaftswert', period)
        hypothek = person('uelv_hypothekarschulden', period)
        freibetrag = person('uelv_freibetrag_liegenschaft', period)
        eigene = person('uelv_bewohnt_eigene_liegenschaft', period)
        bvg = person('uelv_vorsorgeguthaben_bvg', period)

        # Abs. 2: Mortgage debts max up to property value
        hypothek_anrechenbar = min_(hypothek, liegenschaft)

        # Abs. 3: For owner-occupied property, deduct freibetrag then remaining mortgage
        liegenschaft_nach_freibetrag = max_(liegenschaft - freibetrag, 0)
        hypothek_nach_freibetrag = min_(hypothek_anrechenbar, liegenschaft_nach_freibetrag)

        # Abzug auf Liegenschaft: Freibetrag + anrechenbare Hypothek
        liegenschaft_abzug = eigene * (freibetrag + hypothek_nach_freibetrag)

        # Nicht-Hypothekarschulden
        andere_schulden = max_(schulden - hypothek, 0)

        # Abs. 4: BVG pension assets excluded
        reinvermoegen = brutto - bvg - andere_schulden - liegenschaft_abzug

        return max_(reinvermoegen, 0)
