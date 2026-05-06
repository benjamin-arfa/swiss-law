"""SR 313.32 Art. 7

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class abgekuerztes_verfahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wurde das abgekuerzte Verfahren (Art. 65 VStrR) angewendet"
    reference = "SR 313.32 Art. 7 Abs. 1"


class anzahl_betroffene_personen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Personen, die vom Bescheid oder der Verfuegung betroffen sind"
    reference = "SR 313.32 Art. 7 Abs. 3"
    default_value = 1


class spruchgebuehr_strafbescheid_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Spruchgebuehr fuer Strafbescheide (50 CHF)"
    reference = "SR 313.32 Art. 7 Abs. 2 lit. a"
    default_value = 50.0


class spruchgebuehr_strafbescheid_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Spruchgebuehr fuer Strafbescheide (5000 CHF)"
    reference = "SR 313.32 Art. 7 Abs. 2 lit. a"
    default_value = 5000.0


class spruchgebuehr_einstellungsverfuegung_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Spruchgebuehr fuer Einstellungs-/Einziehungsverfuegung (50 CHF)"
    reference = "SR 313.32 Art. 7 Abs. 2 lit. b"
    default_value = 50.0


class spruchgebuehr_einstellungsverfuegung_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Spruchgebuehr fuer Einstellungs-/Einziehungsverfuegung (5000 CHF)"
    reference = "SR 313.32 Art. 7 Abs. 2 lit. b"
    default_value = 5000.0


class spruchgebuehr_einspracheverfahren_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Spruchgebuehr im Einspracheverfahren (100 CHF)"
    reference = "SR 313.32 Art. 7 Abs. 2 lit. c"
    default_value = 100.0


class spruchgebuehr_einspracheverfahren_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Spruchgebuehr im Einspracheverfahren (10000 CHF)"
    reference = "SR 313.32 Art. 7 Abs. 2 lit. c"
    default_value = 10000.0
