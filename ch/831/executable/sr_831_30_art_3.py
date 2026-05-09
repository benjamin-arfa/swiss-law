"""SR 831.30 Art. 3

Generated from: ch/831/de/831.30.md

Art. 3: Bestandteile der Ergaenzungsleistungen - Supplementary benefits
consist of:
a. the annual supplementary benefit (cash benefit, Art. 15 ATSG)
b. reimbursement of illness and disability costs (in-kind benefit, Art. 14 ATSG)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_jaehrliche_ergaenzungsleistung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche Ergaenzungsleistung (Art. 3 Abs. 1 Bst. a ELG)"
    reference = "SR 831.30 Art. 3 Abs. 1 Bst. a"


class el_vergütung_krankheitskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verguetung von Krankheits- und Behinderungskosten (Art. 3 Abs. 1 Bst. b ELG)"
    reference = "SR 831.30 Art. 3 Abs. 1 Bst. b"
