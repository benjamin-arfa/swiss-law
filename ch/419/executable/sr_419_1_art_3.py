"""SR 419.1 Art. 3

Generated from: ch/419/de/419.1.md

Begriffe - Definitionen von Weiterbildung, formaler Bildung, strukturierter Bildung, informeller Bildung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bildungsangebot_ist_staatlich_geregelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bildungsangebot ist staatlich geregelt"
    reference = "SR 419.1 Art. 3 Bst. b"


class bildungsangebot_fuehrt_zu_abschluss_sek_ii_oder_hoeher(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fuehrt zu Abschluss Sekundarstufe II, hoehere Berufsbildung oder akademischem Grad"
    reference = "SR 419.1 Art. 3 Bst. b Ziff. 2"


class bildungsangebot_obligatorische_schule(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Findet in der obligatorischen Schule statt"
    reference = "SR 419.1 Art. 3 Bst. b Ziff. 1"


class bildungsangebot_ist_strukturiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bildung ist strukturiert (organisierte Kurse, Lernprogramme, Lehr-Lern-Beziehung)"
    reference = "SR 419.1 Art. 3 Bst. c"


# --- Computed variables ---

class ist_formale_bildung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angebot ist formale Bildung"
    reference = "SR 419.1 Art. 3 Bst. b"

    def formula(person, period, parameters):
        staatlich = person('bildungsangebot_ist_staatlich_geregelt', period)
        obligatorisch = person('bildungsangebot_obligatorische_schule', period)
        abschluss = person('bildungsangebot_fuehrt_zu_abschluss_sek_ii_oder_hoeher', period)
        return staatlich * (obligatorisch + abschluss)


class ist_weiterbildung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angebot ist Weiterbildung (nichtformale Bildung)"
    reference = "SR 419.1 Art. 3 Bst. a"

    def formula(person, period, parameters):
        strukturiert = person('bildungsangebot_ist_strukturiert', period)
        formal = person('ist_formale_bildung', period)
        return strukturiert * not_(formal)
