"""SR 272.1 Art. 11

Generated from: ch/272/de/272.1.md

Zeitpunkt der Zustellung: Die Zustellung gilt im Zeitpunkt des
Herunterladens als erfolgt. Bei elektronischem Postfach gelten
die Bestimmungen ueber eingeschriebene Sendungen sinngemäss.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dokument_heruntergeladen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Dokument von der Zustellplattform heruntergeladen wurde"
    reference = "SR 272.1 Art. 11 Abs. 1"


class hat_elektronisches_postfach(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein elektronisches Postfach auf einer anerkannten Zustellplattform besteht"
    reference = "SR 272.1 Art. 11 Abs. 2"


class zustellung_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die elektronische Zustellung als erfolgt gilt"
    reference = "SR 272.1 Art. 11"

    def formula(person, period, parameters):
        return person('dokument_heruntergeladen', period)
