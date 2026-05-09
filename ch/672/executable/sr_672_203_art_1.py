"""SR 672.203 Art. 1 — Gegenstand und Geltungsbereich

Verordnung über die Steuerentlastung schweizerischer Dividenden aus wesentlichen Beteiligungen
ausländischer Gesellschaften.
Generated from: ch/de/672/672.203.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_schweizerische_gesellschaft_vstg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine schweizerische Gesellschaft, die nach dem Verrechnungssteuergesetz Steuern auf Dividenden zu erheben hat"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_1"


class hat_auslaendische_wesentliche_beteiligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine ausländische Gesellschaft ist wesentlich an der schweizerischen Gesellschaft beteiligt"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_1"


class auslaendische_gesellschaft_in_dba_staat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die ausländische Gesellschaft ist in einem Staat ansässig, mit dem die Schweiz ein DBA abgeschlossen hat"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_1"


class unterliegt_meldeverfahren_dividenden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterliegt dem Meldeverfahren für Steuerentlastung von Dividenden (SR 672.203 Art. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 2: Gilt für schweizerische Gesellschaften mit
        # wesentlicher ausländischer Beteiligung aus DBA-Staat.
        ist_ch_gesellschaft = person('ist_schweizerische_gesellschaft_vstg', period)
        wesentliche_beteiligung = person('hat_auslaendische_wesentliche_beteiligung', period)
        dba_staat = person('auslaendische_gesellschaft_in_dba_staat', period)
        return ist_ch_gesellschaft * wesentliche_beteiligung * dba_staat
