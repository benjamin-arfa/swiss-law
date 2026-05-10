"""SR 831.30 Art. 3

Generated from: ch/831/de/831.30.md

Art. 3: Bestandteile der Ergaenzungsleistungen - Components of
supplementary benefits.

Abs. 1: Supplementary benefits consist of:
a. the annual supplementary benefit (jaehrliche Ergaenzungsleistung)
   - this is a cash benefit (Geldleistung, Art. 15 ATSG)
b. reimbursement of health and disability costs
   (Vergütung von Krankheits- und Behinderungskosten)
   - this is a benefit in kind (Sachleistung, Art. 14 ATSG)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class el_jaehrliche_ergaenzungsleistung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche Ergaenzungsleistung als Geldleistung (Art. 3 Abs. 1 Bst. a ELG)"
    reference = "SR 831.30 Art. 3 Abs. 1 Bst. a"


class el_verguetung_krankheitskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verguetung von Krankheits- und Behinderungskosten (Art. 3 Abs. 1 Bst. b ELG)"
    reference = "SR 831.30 Art. 3 Abs. 1 Bst. b"


class el_leistungen_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtbetrag der Ergaenzungsleistungen (Art. 3 ELG)"
    reference = "SR 831.30 Art. 3"

    def formula(person, period, parameters):
        jaehrlich = person('el_jaehrliche_ergaenzungsleistung', period)
        krankheitskosten = person('el_verguetung_krankheitskosten', period)
        return jaehrlich + krankheitskosten
