"""SR 523.51 Art. 8

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class einzelleistung_versaeumt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Einzelleistung wurde versaeumt"
    reference = "SR 523.51 Art. 8"


class versaeumnis_begruendet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Versaeumnis ist begruendet (Krankheit, Unfall, Todesfall in der Familie etc.)"
    reference = "SR 523.51 Art. 8 Abs. 3"


class note_versaeumte_einzelleistung(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Note fuer versaeumte Einzelleistung"
    reference = "SR 523.51 Art. 8 Abs. 1-2"

    def formula(person, period, parameters):
        versaeumt = person('einzelleistung_versaeumt', period)
        begruendet = person('versaeumnis_begruendet', period)
        # Unbegründet versäumt -> Note 1
        # Begründet versäumt -> Lehrkraft entscheidet (modeled as 0 = entfällt)
        return where(versaeumt * not_(begruendet), 1.0, 0.0)
