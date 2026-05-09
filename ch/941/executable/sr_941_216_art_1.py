"""SR 941.216 Art. 1 — Gegenstand

Audiometrieverordnung — Verordnung über audiometrische Messmittel.
Generated from: ch/de/941/941.216.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_audiometrisches_messmittel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein audiometrisches Messmittel im Sinne von SR 941.216"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_1"


class unterliegt_audiometrieverordnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterliegt der Audiometrieverordnung SR 941.216 (Art. 1 und 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_1"

    def formula(person, period, parameters):
        # Art. 1 und 2: Regelt Anforderungen, Inverkehrbringen und
        # Messbeständigkeit von audiometrischen Messmitteln für
        # gesundheitsrelevante Zwecke.
        return person('ist_audiometrisches_messmittel', period)
