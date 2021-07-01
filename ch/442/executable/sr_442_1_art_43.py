"""SR 442.1 Art. 43

Generated from: ch/442/de/442.1.md

Steuern: Pro Helvetia ist von der Besteuerung durch Bund, Kantone und Gemeinden
befreit. Vorbehalten: MWST, Verrechnungssteuer, Stempelabgaben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class pro_helvetia_steuerbefreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Pro Helvetia von der Besteuerung befreit ist"
    reference = "SR 442.1 Art. 43 Abs. 1"
    default_value = True


class pro_helvetia_mwst_pflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Pro Helvetia der Mehrwertsteuer unterliegt (Vorbehalt)"
    reference = "SR 442.1 Art. 43 Abs. 2 Bst. a"
    default_value = True


class pro_helvetia_verrechnungssteuer_pflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Pro Helvetia der Verrechnungssteuer unterliegt (Vorbehalt)"
    reference = "SR 442.1 Art. 43 Abs. 2 Bst. b"
    default_value = True


class pro_helvetia_stempelabgaben_pflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Pro Helvetia Stempelabgaben unterliegt (Vorbehalt)"
    reference = "SR 442.1 Art. 43 Abs. 2 Bst. c"
    default_value = True
