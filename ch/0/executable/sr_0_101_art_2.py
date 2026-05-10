"""SR 0.101 Art. 2

Generated from: ch/0/de/0.101.md

Right to life: Everyone's right to life shall be protected by law.
No one shall be deprived of his life intentionally. Exceptions for
lawful defence, arrest, and suppression of insurrection.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_recht_auf_leben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf Leben gesetzlich geschuetzt ist"
    reference = "SR 0.101 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_toetung_verteidigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Toetung zur Verteidigung gegen rechtswidrige Gewalt erfolgte"
    reference = "SR 0.101 Art. 2 Abs. 2 Bst. a"


class emrk_toetung_festnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Toetung bei rechtmaessiger Festnahme oder zur Fluchtverhinderung erfolgte"
    reference = "SR 0.101 Art. 2 Abs. 2 Bst. b"


class emrk_toetung_aufruhr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Toetung zur rechtmaessigen Niederschlagung eines Aufruhrs erfolgte"
    reference = "SR 0.101 Art. 2 Abs. 2 Bst. c"


class emrk_toetung_nicht_verletzung_art2(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Toetung nicht als Verletzung von Art. 2 EMRK gilt"
    reference = "SR 0.101 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        verteidigung = person('emrk_toetung_verteidigung', period)
        festnahme = person('emrk_toetung_festnahme', period)
        aufruhr = person('emrk_toetung_aufruhr', period)
        return verteidigung + festnahme + aufruhr
