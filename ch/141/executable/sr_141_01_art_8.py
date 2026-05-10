"""SR 141.01 Art. 8

Generated from: ch/141/de/141.01.md

Foerderung der Integration der Familienmitglieder: Unterstuetzung beim
Spracherwerb, Wirtschaftsteilnahme, sozialer/kultureller Teilnahme
oder anderen Integrationsaktivitaeten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class foerdert_spracherwerb_familie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Familienmitglieder beim Erwerb von Sprachkompetenzen in einer Landessprache unterstuetzt werden"
    reference = "SR 141.01 Art. 8 Bst. a"


class foerdert_wirtschaft_bildung_familie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Familienmitglieder bei der Teilnahme am Wirtschaftsleben oder Erwerb von Bildung unterstuetzt werden"
    reference = "SR 141.01 Art. 8 Bst. b"


class foerdert_integration_familie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Integration der Familienmitglieder nach Art. 12 Bst. e BueG gefoerdert wird"
    reference = "SR 141.01 Art. 8"

    def formula(person, period, parameters):
        sprache = person('foerdert_spracherwerb_familie', period)
        wirtschaft = person('foerdert_wirtschaft_bildung_familie', period)
        return (sprache + wirtschaft) > 0
