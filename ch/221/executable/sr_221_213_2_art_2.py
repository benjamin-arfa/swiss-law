"""SR 221.213.2 Art. 2

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_rebgrundstueck(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pachtgegenstand ist ein Rebgrundstück"
    reference = "SR 221.213.2 Art. 2 Abs. 1 lit. a"


class flaeche_aren(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Fläche des Grundstücks in Aren"
    reference = "SR 221.213.2 Art. 2 Abs. 1"


class grundstueck_hat_gebaeude(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Grundstück umfasst Gebäude"
    reference = "SR 221.213.2 Art. 2 Abs. 1 lit. b"


class ausnahme_kleine_grundstuecke(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausnahme für kleine Grundstücke - LPG gilt nicht"
    reference = "SR 221.213.2 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        ist_reb = person('ist_rebgrundstueck', period)
        flaeche = person('flaeche_aren', period)
        hat_gebaeude = person('grundstueck_hat_gebaeude', period)
        # Rebgrundstücke unter 15 Aren
        reb_ausnahme = ist_reb * (flaeche < 15)
        # Andere Grundstücke ohne Gebäude unter 25 Aren
        andere_ausnahme = not_(ist_reb) * not_(hat_gebaeude) * (flaeche < 25)
        return reb_ausnahme + andere_ausnahme
