"""SR 955.01 Art. 19–21

Generated from: ch/955/de/955.01.md

Zusaetzliche Abklaerungen, Meldepflicht und Dokumentation:
- Art. 19: Hintergrundueberpruefung bei ungewoehnlichen Geschaeften
  oder Geldwaescherei-Anhaltspunkten (z.B. kleine Nennwerte,
  leichtverkaeufliche Gueter, falsche Angaben).
- Art. 20: Meldepflicht bei begruendetem Verdacht (konkreter Hinweis
  oder mehrere Anhaltspunkte).
- Art. 21: Dokumentation auf Formular; Aufbewahrung mind. 10 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gwv_haendler_geschaeft_ist_ungewoehnlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Geschaeft erscheint ungewoehnlich oder mit GW-Anhaltspunkten"
    reference = "SR 955.01 Art. 19 Abs. 1"


class gwv_haendler_abklaerungen_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Zusaetzliche Abklaerungen nach Art. 19 durchgefuehrt"
    reference = "SR 955.01 Art. 19"


class gwv_haendler_begruendeter_verdacht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Begruendeter Geldwaeschereiverdacht besteht"
    reference = "SR 955.01 Art. 20 Abs. 1"


class gwv_haendler_meldepflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Meldepflicht nach Art. 20 ist ausgeloest"
    reference = "SR 955.01 Art. 20"

    def formula(person, period, parameters):
        verdacht = person('gwv_haendler_begruendeter_verdacht', period)
        abklaerungen = person('gwv_haendler_abklaerungen_durchgefuehrt', period)

        # Meldepflicht wenn Verdacht sich trotz Abklaerungen nicht ausraeumen laesst
        return verdacht * abklaerungen


class gwv_dokumentation_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Dokumentation (Formular Anhang 1) korrekt erstellt"
    reference = "SR 955.01 Art. 21"


class gwv_aufbewahrungsfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Aufbewahrungsfrist fuer Dokumentation (Jahre)"
    reference = "SR 955.01 Art. 21 Abs. 4"

    def formula(person, period, parameters):
        import numpy as np

        p = parameters(period).sr955_01
        return np.full(person.count, p.dokumentation_aufbewahrungsfrist_jahre)
