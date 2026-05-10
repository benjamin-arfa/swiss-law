"""SR 415.0 Art. 10

Generated from: ch/415/de/415.0.md

Ausserordentliche Leumundspruefung fuer J+S-Kader.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class strafverfahren_haengig_unvereinbar_mit_js_kader(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Haengiges Strafverfahren wegen Straftat unvereinbar mit J+S-Kader-Stellung"
    reference = "SR 415.0 Art. 10 Abs. 2"


class rechtskraeftig_verurteilt_unvereinbar_mit_js_kader(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rechtskraeftige Verurteilung wegen Straftat unvereinbar mit J+S-Kader-Stellung"
    reference = "SR 415.0 Art. 10 Abs. 3"


# --- Computed variables ---

class js_kader_anerkennung_verweigert_oder_sistiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "J+S-Kader-Anerkennung wird verweigert oder sistiert"
    reference = "SR 415.0 Art. 10 Abs. 2-3"

    def formula(person, period, parameters):
        verfahren = person('strafverfahren_haengig_unvereinbar_mit_js_kader', period)
        verurteilt = person('rechtskraeftig_verurteilt_unvereinbar_mit_js_kader', period)
        return verfahren + verurteilt
