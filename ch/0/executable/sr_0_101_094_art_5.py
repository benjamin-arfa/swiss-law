"""SR 0.101.094 Art. 5

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_countrymodules_ch.taxonomy import Taxonomy




class anträge_nach_art_25(variables.Variable):
    label = 'Anträge nach Artikel 25'
    # Bereich
    entity = variables.ENTITIES
    definition_period = '1 Jahr'

    # Anzahl der Anträge auf Personengrundlage
    def formula_2024_01_01(art_25, this_period, this_households):
        einträge = this_households((art_25('plenum', this_period) > 0) ^ (art_25('plenum', this_period) == 1), this_period)
        return einträge
