"""SR 611.010 Art. 1

Generated from: ch/611/de/611.010.md

Bundesgesetz über Massnahmen zur Verbesserung des Bundeshaushaltes.
Art. 1: Grundsatz - Bundesausgaben sind auf das unbedingt Notwendige zu
beschränken und auf die finanziellen Möglichkeiten des Bundes auszurichten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bundesausgaben_auf_notwendiges_beschraenkt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Bundesausgaben sind auf das unbedingt Notwendige beschränkt und auf "
        "die finanziellen Möglichkeiten des Bundes ausgerichtet (Art. 1 Abs. 1)"
    )
    reference = "SR 611.010 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 1: Zur Verbesserung des Bundeshaushaltes sind die
        # Bundesausgaben auf das unbedingt Notwendige zu beschränken und auf
        # die finanziellen Möglichkeiten des Bundes auszurichten.
        # This is a declaratory principle; modeled as input variable.
        return person('ist_ausgabe_unbedingt_notwendig', period)


class ist_ausgabe_unbedingt_notwendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausgabe ist unbedingt notwendig im Sinne von SR 611.010 Art. 1 Abs. 1"
    reference = "SR 611.010 Art. 1 Abs. 1"
