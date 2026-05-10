"""SR 235.1 Art. 22

Generated from: ch/235/de/235.1.md

Bearbeiten fuer Forschung, Planung und Statistik durch Bundesorgane.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_zweck_forschung_planung_statistik(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten werden fuer nicht personenbezogene Zwecke (Forschung, Planung, Statistik) bearbeitet"
    reference = "SR 235.1 Art. 22 Abs. 1"


class dsg_daten_anonymisiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten werden anonymisiert sobald der Zweck es erlaubt"
    reference = "SR 235.1 Art. 22 Abs. 1 lit. a"


class dsg_empfaenger_nur_mit_zustimmung_weitergibt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Empfaenger gibt Daten nur mit Zustimmung des Bundesorgans weiter"
    reference = "SR 235.1 Art. 22 Abs. 1 lit. b"


class dsg_ergebnisse_nicht_bestimmbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ergebnisse werden so veroeffentlicht, dass betroffene Personen nicht bestimmbar sind"
    reference = "SR 235.1 Art. 22 Abs. 1 lit. c"


class dsg_forschung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bearbeitung fuer Forschung/Planung/Statistik ist zulaessig"
    reference = "SR 235.1 Art. 22"

    def formula(person, period, parameters):
        zweck = person('dsg_zweck_forschung_planung_statistik', period)
        anon = person('dsg_daten_anonymisiert', period)
        zustimmung = person('dsg_empfaenger_nur_mit_zustimmung_weitergibt', period)
        nicht_bestimmbar = person('dsg_ergebnisse_nicht_bestimmbar', period)
        return zweck * anon * zustimmung * nicht_bestimmbar
