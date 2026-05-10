"""SR 742.101 Art. 8a

Generated from: ch/742/de/742.101.md

Erteilung und Erneuerung der Sicherheitsgenehmigung:
- Abs. 1: BAV erteilt Sicherheitsgenehmigung, wenn Infrastrukturbetreiberin
  ueber ein Sicherheitsmanagementsystem verfuegt.
- Abs. 2: Sicherheitsgenehmigung wird fuer hoechstens 5 Jahre erteilt,
  kann erneuert werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_sicherheitsmanagementsystem(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Infrastrukturbetreiberin ueber ein Sicherheitsmanagementsystem verfuegt"
    reference = "SR 742.101 Art. 8a Abs. 1"


class sicherheitsgenehmigung_erteilbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Sicherheitsgenehmigung erteilt werden kann"
    reference = "SR 742.101 Art. 8a Abs. 1"

    def formula(person, period, parameters):
        return person('hat_sicherheitsmanagementsystem', period)


class sicherheitsgenehmigung_max_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Dauer der Sicherheitsgenehmigung (Jahre)"
    reference = "SR 742.101 Art. 8a Abs. 2"

    def formula(person, period, parameters):
        return parameters(period).sr_742_101.sicherheitsgenehmigung_max_dauer_jahre
