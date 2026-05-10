"""SR 152.31 Art. 2

Generated from: ch/152/de/152.31.md

Principle of equal access: if one person has access to an official document,
every other applicant has access to the same extent.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_zugang_zu_dokument(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Person Zugang zu einem amtlichen Dokument hat"
    reference = "SR 152.31 Art. 2"


class gleicher_zugang_fuer_alle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob jeder weiteren gesuchstellenden Person der gleiche Zugang zusteht"
    reference = "SR 152.31 Art. 2"

    def formula(person, period, parameters):
        return person('hat_zugang_zu_dokument', period)
