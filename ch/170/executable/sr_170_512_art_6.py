"""SR 170.512 Art. 6

Generated from: ch/170/de/170.512.md

Ausnahmen von der Publikationspflicht bei Geheimhaltung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erlass_muss_geheim_gehalten_werden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erlass muss zur Wahrung der Sicherheit oder aufgrund völkerrechtlicher Verpflichtungen geheim gehalten werden (Art. 6 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 6 Abs. 1"


class erlass_wird_in_as_veroeffentlicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Erlass wird in der AS veröffentlicht (Art. 6 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 6 Abs. 1"

    def formula(person, period, parameters):
        geheim = person('erlass_muss_geheim_gehalten_werden', period)
        return 1 - geheim


class geheime_pflichten_nur_bei_bekanntgabe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Individuelle Pflichten aus geheimen Erlassen gelten nur bei Bekanntgabe (Art. 6 Abs. 2 PublG)"
    reference = "SR 170.512, Art. 6 Abs. 2"

    def formula(person, period, parameters):
        return person('erlass_muss_geheim_gehalten_werden', period)
