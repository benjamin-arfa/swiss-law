"""SR 455.102.4 Art. 6

Generated from: ch/455/de/455.102.4.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables
class belastungskategorie_tier(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Belastungskategorie des Tieres (0-3)"
    reference = "SR 455.102.4 Art. 6"


class zuchtziel_reduziert_belastung_nachkommen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuchtziel beinhaltet, dass Belastung der Nachkommen unter Belastung der Elterntiere liegt (Art. 6 Abs. 2 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 6 Abs. 2"


class zuchteinsatz_erlaubt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuchteinsatz des Tieres ist erlaubt nach Art. 6 SR 455.102.4"
    reference = "SR 455.102.4 Art. 6"

    def formula(person, period, parameters):
        kategorie = person('belastungskategorie_tier', period)
        reduziert_belastung = person('zuchtziel_reduziert_belastung_nachkommen', period)
        # Abs. 1: Kategorie 0 oder 1 darf gezuechtet werden
        erlaubt_kat_0_1 = (kategorie <= 1)
        # Abs. 2: Kategorie 2 darf gezuechtet werden wenn Zuchtziel Belastung reduziert
        erlaubt_kat_2 = (kategorie == 2) * reduziert_belastung
        # Kategorie 3 ist verboten (Art. 9)
        return erlaubt_kat_0_1 + erlaubt_kat_2
