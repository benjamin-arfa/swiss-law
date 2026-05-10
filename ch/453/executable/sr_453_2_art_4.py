"""SR 453.2 Art. 4

Generated from: ch/453/de/453.2.md
Einfuhrbedingungen Meeresfischerei - Grundsatz.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fischereierzeugnis_rechtmaessiger_herkunft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fischereierzeugnis ist rechtmaessiger Herkunft"
    reference = "SR 453.2 Art. 4 Abs. 1 Bst. a"


class begleitdokumente_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erforderliche Begleitdokumente liegen bei"
    reference = "SR 453.2 Art. 4 Abs. 1 Bst. b"


class flaggenstaat_in_anhang_2(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fischereierzeugnis stammt aus Flaggenstaat nach Anhang 2"
    reference = "SR 453.2 Art. 4 Abs. 2"


class hat_fangbescheinigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fangbescheinigung liegt vor"
    reference = "SR 453.2 Art. 4 Abs. 2"


class einfuhr_fischerei_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbsmaessige Einfuhr von Fischereierzeugnissen ist zulaessig"
    reference = "SR 453.2 Art. 4"

    def formula(person, period, parameters):
        rechtmaessig = person('fischereierzeugnis_rechtmaessiger_herkunft', period)
        dokumente = person('begleitdokumente_vorhanden', period)
        anhang2 = person('flaggenstaat_in_anhang_2', period)
        fangbescheinigung = person('hat_fangbescheinigung', period)

        # Abs. 1: rechtmaessig + Dokumente
        # Abs. 2: Nicht-Anhang-2-Staaten brauchen zusaetzlich Fangbescheinigung
        grundanforderung = rechtmaessig * dokumente
        zusatz_nicht_anhang2 = where(anhang2, True, fangbescheinigung)
        return grundanforderung * zusatz_nicht_anhang2
