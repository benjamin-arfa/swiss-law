"""SR 672.203 Art. 5 — Meldung an die ESTV

Verordnung über die Steuerentlastung schweizerischer Dividenden aus wesentlichen Beteiligungen
ausländischer Gesellschaften.
Generated from: ch/de/672/672.203.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_bewilligung_meldeverfahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfügt über eine Bewilligung für das Meldeverfahren"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_5"


class dividende_ausgerichtet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eine Dividende wurde an die ausländische Gesellschaft ausgerichtet"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_5"


class meldung_frist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist für Meldung der Dividendenausrichtung an ESTV in Tagen (SR 672.203 Art. 5 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_5"

    def formula(person, period, parameters):
        # Art. 5 Abs. 1: Meldung innert 30 Tagen mit Formular 108.
        return 30


class meldepflicht_dividende_estv(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Pflicht zur unaufgeforderten Meldung der Dividendenausrichtung an ESTV innert 30 Tagen (SR 672.203 Art. 5 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_5"

    def formula(person, period, parameters):
        # Art. 5 Abs. 1: Wer über Bewilligung verfügt, meldet unaufgefordert
        # innert 30 Tagen mit Formular 108.
        bewilligung = person('hat_bewilligung_meldeverfahren', period.this_year)
        dividende = person('dividende_ausgerichtet', period)
        return bewilligung * dividende
