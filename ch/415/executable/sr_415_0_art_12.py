"""SR 415.0 Art. 12

Generated from: ch/415/de/415.0.md

Foerderung von Sport- und Bewegungsmoeglichkeiten in der Schule.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class schulstufe(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Schulstufe (obligatorische_schule, sekundarstufe_ii, berufsfachschule)"
    reference = "SR 415.0 Art. 12"


# --- Computed variables ---

class sportunterricht_obligatorisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sportunterricht ist obligatorisch"
    reference = "SR 415.0 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        stufe = person('schulstufe', period)
        return (stufe == 'obligatorische_schule') + (stufe == 'sekundarstufe_ii')


class mindestlektionen_sportunterricht_pro_woche(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestlektionen Sportunterricht pro Woche"
    reference = "SR 415.0 Art. 12 Abs. 4"

    def formula(person, period, parameters):
        stufe = person('schulstufe', period)
        # In der obligatorischen Schule mindestens 3 Lektionen
        return where(stufe == 'obligatorische_schule', 3, 0)
