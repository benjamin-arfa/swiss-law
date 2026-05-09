"""SR 654.1 Art. 4 - Langue de la declaration pays par pays

Generated from: ch/654/de/654.1.md

The country-by-country report must be prepared in one of the official
federal languages or in English.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class langue_declaration_pays(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Langue dans laquelle la declaration pays par pays est redigee"
    reference = "SR 654.1 Art. 4"


class langue_declaration_pays_valide(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La declaration est redigee dans une langue officielle de la Confederation ou en anglais"
    reference = "SR 654.1 Art. 4"
