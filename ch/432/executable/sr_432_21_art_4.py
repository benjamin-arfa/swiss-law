"""SR 432.21 Art. 4

Generated from: ch/432/de/432.21.md

Umschreibung des Sammelauftrags - Bundesrat kann Druckwerke vom Sammelauftrag
ausschliessen unter bestimmten Bedingungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class werk_von_anderer_institution_gesammelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Druckwerk wird von einer anderen Institution gesammelt und oeffentlich zugaenglich gemacht"
    reference = "SR 432.21 Art. 4 Abs. 2 Bst. a"


class werk_geringe_bedeutung_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Druckwerk ist fuer die Schweiz von geringer Bedeutung"
    reference = "SR 432.21 Art. 4 Abs. 2 Bst. b"


class werk_beschraenkter_personenkreis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Druckwerk ist nur fuer beschraenkten Personenkreis oder vorwiegend private Zwecke bestimmt"
    reference = "SR 432.21 Art. 4 Abs. 2 Bst. c"


class werk_vom_sammelauftrag_ausgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Druckwerk kann vom Sammelauftrag der Nationalbibliothek ausgeschlossen werden"
    reference = "SR 432.21 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('werk_von_anderer_institution_gesammelt', period) +
            person('werk_geringe_bedeutung_schweiz', period) +
            person('werk_beschraenkter_personenkreis', period)
        ) > 0
