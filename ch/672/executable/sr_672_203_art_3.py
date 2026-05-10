"""SR 672.203 Art. 3 — Bewilligung des Meldeverfahrens

Verordnung über die Steuerentlastung schweizerischer Dividenden aus wesentlichen Beteiligungen
ausländischer Gesellschaften.
Generated from: ch/de/672/672.203.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuch_meldeverfahren_eingereicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesuch für Meldeverfahren wurde mit amtlichem Formular vor Fälligkeit der Dividenden eingereicht"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_3"


class auslaendische_gesellschaft_hat_dba_anspruch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausländische Gesellschaft hat nach DBA Anspruch auf Entlastung"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_3"


class bewilligung_meldeverfahren_gueltigkeitsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gültigkeitsdauer der Bewilligung des Meldeverfahrens in Jahren (SR 672.203 Art. 3 Abs. 4)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 4: Die Bewilligung gilt fünf Jahre.
        return 5


class bewilligung_meldeverfahren_erteilt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "ESTV hat Bewilligung für Meldeverfahren erteilt (SR 672.203 Art. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_3"

    def formula(person, period, parameters):
        # Art. 3: ESTV erteilt auf Gesuch Bewilligung wenn:
        # - Gesuch vor Fälligkeit eingereicht (Abs. 2)
        # - Ausländische Gesellschaft hat DBA-Anspruch (Abs. 3)
        gesuch = person('gesuch_meldeverfahren_eingereicht', period)
        anspruch = person('auslaendische_gesellschaft_hat_dba_anspruch', period)
        return gesuch * anspruch
