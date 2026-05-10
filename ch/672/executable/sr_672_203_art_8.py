"""SR 672.203 Art. 8 — Reziprozität

Verordnung über die Steuerentlastung schweizerischer Dividenden aus wesentlichen Beteiligungen
ausländischer Gesellschaften.
Generated from: ch/de/672/672.203.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class staat_gewaehrt_gegenseitigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der betreffende Staat gewährt Gegenseitigkeit beim Meldeverfahren"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_8"


class staat_auf_ausschlussliste_meldeverfahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Staat ist im Anhang der Verordnung als ausgeschlossen aufgeführt (SR 672.203 Art. 8 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_8"


class meldeverfahren_anwendbar_auf_staat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Meldeverfahren ist auf den betreffenden Staat anwendbar (SR 672.203 Art. 8)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_8"

    def formula(person, period, parameters):
        # Art. 8: ESTV entscheidet, ob Meldeverfahren nur auf Staaten
        # angewendet wird, die Gegenseitigkeit gewähren.
        # Ausgeschlossene Staaten im Anhang aufgeführt.
        gegenseitigkeit = person('staat_gewaehrt_gegenseitigkeit', period)
        nicht_ausgeschlossen = person('staat_auf_ausschlussliste_meldeverfahren', period) == False
        return gegenseitigkeit * nicht_ausgeschlossen
