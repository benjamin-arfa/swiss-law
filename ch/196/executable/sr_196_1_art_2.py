"""SR 196.1 Art. 2

Generated from: ch/196/de/196.1.md

Begriffe: Definitionen von auslaendischen politisch exponierten Personen,
nahestehenden Personen und Vermoegenswerten.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_auslaendische_politisch_exponierte_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person mit fuehrenden oeffentlichen Funktionen im Ausland betraut ist oder war"
    reference = "SR 196.1 Art. 2 lit. a"


class ist_nahestehende_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person einer auslaendischen PEP aus familiaeren, persoenlichen oder geschaeftlichen Gruenden erkennbar nahesteht"
    reference = "SR 196.1 Art. 2 lit. b"
