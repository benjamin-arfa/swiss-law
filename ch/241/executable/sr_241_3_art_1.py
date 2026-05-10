"""SR 241.3 Art. 1 - Klagerecht des Bundes

Generated from: ch/241/de/241.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class verfahren_auf_grundlage_art_10_abs_3_uwg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es handelt sich um ein Zivil- oder Strafverfahren auf der Grundlage von Art. 10 Abs. 3 UWG"
    reference = "SR 241.3 Art. 1 Abs. 1"


class besonderer_fall_klagevertretung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegt ein besonderer Fall vor, der eine andere Vertretung rechtfertigt"
    reference = "SR 241.3 Art. 1 Abs. 2"


# Computed variables

class bund_vertreten_durch_seco_klagerecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund wird durch das SECO vertreten (Klagerecht)"
    reference = "SR 241.3 Art. 1 Abs. 1"

    def formula(self, period, parameters):
        uwg_verfahren = self('verfahren_auf_grundlage_art_10_abs_3_uwg', period)
        besonderer_fall = self('besonderer_fall_klagevertretung', period)
        # SECO vertritt den Bund, ausser in besonderen Faellen
        return uwg_verfahren * (1 - besonderer_fall)
