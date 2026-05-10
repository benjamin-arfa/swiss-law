"""SR 418.0 Art. 6

Generated from: ch/418/de/418.0.md

Voraussetzungen fuer die Anerkennung von Filialschulen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class filialschule_organisatorisch_paedagogisch_bestandteil(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Filialschule bildet organisatorisch und paedagogisch Bestandteil der Schule"
    reference = "SR 418.0 Art. 6 Bst. a"


class filialschule_wirtschaftlich_paedagogisch_vorteilhaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Filialschule ist wirtschaftlich und paedagogisch vorteilhaft"
    reference = "SR 418.0 Art. 6 Bst. b"


class filialschule_beitragsberechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Filialschule als beitragsberechtigt anerkannt"
    reference = "SR 418.0 Art. 6"

    def formula(person, period, parameters):
        return (
            person('filialschule_organisatorisch_paedagogisch_bestandteil', period) *
            person('filialschule_wirtschaftlich_paedagogisch_vorteilhaft', period)
        )
