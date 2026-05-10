"""SR 112 Art. 1

Generated from: ch/de/112.md

Property transfers from Bern to the Confederation: Bundesrathaus,
courtyard, and a parcel of the Vannazhalde.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bundesrathaus_abgetreten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Bundesrathausgebaeude an die Eidgenossenschaft abgetreten wurde"
    reference = "SR 112 Art. 1 Bst. a"


class innerer_hof_abgetreten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der innere Hof des Bundesrathauses abgetreten wurde"
    reference = "SR 112 Art. 1 Bst. b"


class vannazhalde_parzelle_abgetreten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Parzelle der Vannazhalde abgetreten wurde"
    reference = "SR 112 Art. 1 Bst. c"


class brunnen_verbleibt_gemeinde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Brunnen im Hof bei der Einwohnergemeinde verbleibt"
    reference = "SR 112 Art. 1 Bst. b"

    def formula(person, period, parameters):
        return person('innerer_hof_abgetreten', period)


class brunnen_oeffentlich_zugaenglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Brunnen dem Publikum zum Hausgebrauch offensteht"
    reference = "SR 112 Art. 1 Bst. b"

    def formula(person, period, parameters):
        return person('brunnen_verbleibt_gemeinde', period)
