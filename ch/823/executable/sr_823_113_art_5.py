"""SR 823.113 Art. 5

Generated from: ch/823/de/823.113.md

Vermittlungsprovision zulasten von Fotomodellen und Mannequins:
- Einsätze < 6 Arbeitstage: max. 12%
- Einsätze >= 6 Arbeitstage: max. 10%
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class einsatzdauer_modell_arbeitstage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Einsatzdauer in Arbeitstagen für Fotomodelle/Mannequins"
    reference = "SR 823.113 Art. 5"


class einsatz_gage_modell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Brutto-Gage des Einsatzes für Fotomodelle/Mannequins"
    reference = "SR 823.113 Art. 5"


class vermittlungsprovision_modell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Vermittlungsprovision für Fotomodelle und Mannequins"
    reference = "SR 823.113 Art. 5"

    def formula(person, period, parameters):
        import numpy as np
        tage = person('einsatzdauer_modell_arbeitstage', period)
        gage = person('einsatz_gage_modell', period)
        params = parameters(period).sr_823_113

        satz = np.where(
            tage < params.modell_kurzeinsatz_schwelle,
            params.provision_modell_kurz,
            params.provision_modell_lang
        )
        return gage * satz
