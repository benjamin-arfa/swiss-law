"""SR 142.201.1 Art. 5

Generated from: ch/142/de/142.201.1.md

Abweichungen von den Zulassungsvoraussetzungen: Bewilligungen, die
dem SEM zur Zustimmung zu unterbreiten sind (Haertefaelle, Opfer
Menschenhandel, Wiederzulassung, etc.).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 5 lists various special-case permit categories requiring SEM
# approval (children of Swiss citizens, former Swiss citizens, hardship cases,
# human trafficking victims, witness protection, readmission, etc.).
# These are categorical eligibility checks without computable formulas -
# each is a boolean fact that must be provided externally.
# The rule is: if any of these categories applies, SEM approval is required.


class ist_auslaendisches_kind_schweizer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob auslaendisches Kind von Schweizer/in (Art. 29 VZAE)"
    reference = "SR 142.201.1 Art. 5 Bst. a"


class ist_ehemalige_schweizerin(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ehemalige/r Schweizer/in (Art. 30 VZAE)"
    reference = "SR 142.201.1 Art. 5 Bst. b"


class ist_schwerwiegender_haertefall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob schwerwiegender persoenlicher Haertefall (Art. 31 VZAE)"
    reference = "SR 142.201.1 Art. 5 Bst. d"


class ist_opfer_menschenhandel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Opfer oder Zeuge von Menschenhandel (Art. 36 VZAE)"
    reference = "SR 142.201.1 Art. 5 Bst. g"


class zustimmung_sem_abweichung_zulassung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Zustimmung des SEM fuer Abweichungen von Zulassungsvoraussetzungen erforderlich"
    reference = "SR 142.201.1 Art. 5"

    def formula(person, period, parameters):
        return (
            person('ist_auslaendisches_kind_schweizer', period)
            + person('ist_ehemalige_schweizerin', period)
            + person('ist_schwerwiegender_haertefall', period)
            + person('ist_opfer_menschenhandel', period)
        ) > 0
