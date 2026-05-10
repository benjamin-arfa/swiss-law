"""SR 641.811.31 Art. 4

Generated from: ch/641/de/641.811.31.md

Domestic vehicles subject to performance-based levy: applications per vehicle
and levy period; refund amount offset against the levy where possible.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_inlaendisches_fahrzeug_leistungsabhaengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein inlaendisches Fahrzeug mit leistungsabhaengiger Abgabe handelt"
    reference = "SR 641.811.31 Art. 4 Abs. 1"


class rueckerstattung_verrechnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Rueckerstattungsbetrag mit der Schwerverkehrsabgabe verrechnet wird"
    reference = "SR 641.811.31 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_inlaendisches_fahrzeug_leistungsabhaengig', period)
