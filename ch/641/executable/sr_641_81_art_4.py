"""SR 641.81 Art. 4 - Ausnahmen und Befreiungen (Exemptions)

Heavy Vehicle Tax Act (SVAG) - Exemptions and flat-rate for passenger transport.
Art. 4 Abs. 2: Flat-rate tax for passenger transport max 5000 CHF/year.

Generated from: ch/641/de/641.81.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class svag_fahrzeug_personentransport(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle is used for passenger transport (SR 641.81 Art. 4 Abs. 2)"
    reference = "SR 641.81 Art. 4"
    default_value = False


class svag_fahrzeug_befreit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vehicle is fully or partially exempt from heavy vehicle tax (SR 641.81 Art. 4 Abs. 1)"
    reference = "SR 641.81 Art. 4"
    default_value = False


class svag_pauschale_personentransport(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Flat-rate heavy vehicle tax for passenger transport in CHF (SR 641.81 Art. 4 Abs. 2)"
    reference = "SR 641.81 Art. 4"

    def formula(person, period, parameters):
        ist_personentransport = person("svag_fahrzeug_personentransport", period)
        ist_befreit = person("svag_fahrzeug_befreit", period)
        max_pauschale = 5000.0
        return where(ist_befreit, 0.0, where(ist_personentransport, max_pauschale, 0.0))
