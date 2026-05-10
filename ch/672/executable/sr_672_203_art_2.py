"""SR 672.203 Art. 2 — Wesentliche Beteiligung

Verordnung über die Steuerentlastung schweizerischer Dividenden aus wesentlichen Beteiligungen
ausländischer Gesellschaften.
Generated from: ch/de/672/672.203.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beteiligung_prozent_auslaendische_gesellschaft(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der ausländischen Gesellschaft am Kapital der schweizerischen Gesellschaft in Prozent"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_2"


class dba_schwelle_wesentliche_beteiligung_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schwelle für wesentliche Beteiligung gemäss massgebendem DBA in Prozent"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_2"


class dba_hat_bestimmung_wesentliche_beteiligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das massgebende DBA enthält eine Bestimmung über wesentliche Beteiligungen"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_2"


class ist_wesentliche_beteiligung_672_203(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die ausländische Gesellschaft ist wesentlich beteiligt im Sinne von SR 672.203 Art. 2"
    reference = "https://www.fedlex.admin.ch/eli/cc/2005/26/de#art_2"

    def formula(person, period, parameters):
        # Art. 2 Abs. 1: Wesentlich beteiligt wenn Beteiligung gemäss DBA
        # zur zusätzlichen/vollständigen Entlastung berechtigt.
        # Art. 2 Abs. 2: Fehlt DBA-Bestimmung, mindestens 10% des Kapitals.
        beteiligung = person('beteiligung_prozent_auslaendische_gesellschaft', period)
        hat_dba_bestimmung = person('dba_hat_bestimmung_wesentliche_beteiligung', period)
        dba_schwelle = person('dba_schwelle_wesentliche_beteiligung_prozent', period)

        # Wenn DBA eine Bestimmung hat: Beteiligung >= DBA-Schwelle
        nach_dba = hat_dba_bestimmung * (beteiligung >= dba_schwelle)
        # Wenn DBA keine Bestimmung hat: mindestens 10%
        ohne_dba = (hat_dba_bestimmung == False) * (beteiligung >= 10.0)

        return nach_dba + ohne_dba > 0
