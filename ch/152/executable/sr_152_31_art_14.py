"""SR 152.31 Art. 14

Generated from: ch/152/de/152.31.md

Fee principles: a fee may be charged if processing takes more than
8 hours. Only time exceeding 8 hours counts for fee calculation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arbeitsaufwand_zugangsgesuch_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitsaufwand fuer die Bearbeitung des Zugangsgesuchs in Stunden"
    reference = "SR 152.31 Art. 14 Abs. 1"


class gebuehr_zugangsgesuch_zulasssig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Gebuehr fuer das Zugangsgesuch erhoben werden darf"
    reference = "SR 152.31 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        return person('arbeitsaufwand_zugangsgesuch_stunden', period) > 8


class gebuehrenrelevanter_aufwand_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gebuehrenrelevanter Aufwand in Stunden (nur ueber 8 Stunden)"
    reference = "SR 152.31 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        aufwand = person('arbeitsaufwand_zugangsgesuch_stunden', period)
        return max_(aufwand - 8, 0)


class schwelle_gebuehrenpflicht_stunden(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Schwelle fuer Gebuehrenpflicht in Stunden"
    reference = "SR 152.31 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        return 8
