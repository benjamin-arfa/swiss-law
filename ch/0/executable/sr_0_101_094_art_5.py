"""SR 0.101.094 Art. 5

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_countrymodules_ch.taxonomy import Taxonomy
from openfisca_core import periods, variables
from openfisca_core.indexed_enums import EnumBuilder
from openfisca_core.parsing import expression as exp

class anträge_nach_art_25(variables.Variable):
    label = 'Anträge nach Artikel 25'
    # Bereich
    entity = variables.ENTITIES
    definition_period = '1 Jahr'

    # Anzahl der Anträge auf Personengrundlage
    def formula_2024_01_01(art_25, this_period, this_households):
        einträge = this_households((art_25('plenum', this_period) > 0) ^ (art_25('plenum', this_period) == 1), this_period)
        return einträge
