"""SR 241.3 Art. 2 - Information der Oeffentlichkeit

Generated from: ch/241/de/241.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class fall_nach_art_10_abs_4_uwg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es handelt sich um einen Fall nach Art. 10 Abs. 4 UWG (Information der Oeffentlichkeit)"
    reference = "SR 241.3 Art. 2 Abs. 1"


class besonderer_fall_information(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegt ein besonderer Fall vor, der eine andere Vertretung rechtfertigt"
    reference = "SR 241.3 Art. 2 Abs. 2"


# Computed variables

class bund_vertreten_durch_seco_information(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund wird durch das SECO vertreten (Information der Oeffentlichkeit)"
    reference = "SR 241.3 Art. 2 Abs. 1"

    def formula(self, period, parameters):
        uwg_fall = self('fall_nach_art_10_abs_4_uwg', period)
        besonderer_fall = self('besonderer_fall_information', period)
        return uwg_fall * (1 - besonderer_fall)
