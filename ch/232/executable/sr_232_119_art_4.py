"""SR 232.119 Art. 4

Generated from: ch/232/de/232.119.md

Art. 4 defines when a watch case qualifies as Swiss.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gehaeuse_wesentlicher_fabrikationsvorgang_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestens ein wesentlicher Fabrikationsvorgang (Ausstanzen, Bearbeiten, Polieren) des Gehaeuses in der Schweiz"
    reference = "SR 232.119 Art. 4 Abs. 1 lit. a"


class gehaeuse_in_schweiz_zusammengesetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Uhrengehaeuse wurde in der Schweiz zusammengesetzt"
    reference = "SR 232.119 Art. 4 Abs. 1 lit. b"


class gehaeuse_in_schweiz_kontrolliert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Uhrengehaeuse wird durch den Hersteller in der Schweiz kontrolliert"
    reference = "SR 232.119 Art. 4 Abs. 1 lit. c"


class herstellungskosten_anteil_schweiz_gehaeuse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Herstellungskosten des Gehaeuses, die in der Schweiz anfallen (0-1)"
    reference = "SR 232.119 Art. 4 Abs. 1 lit. d"


class ist_schweizerisches_uhrengehaeuse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Das Uhrengehaeuse gilt als schweizerisch im Sinne von SR 232.119 Art. 4"
    reference = "SR 232.119 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        # All four conditions must be met cumulatively
        fabrikation = person('gehaeuse_wesentlicher_fabrikationsvorgang_in_schweiz', period)
        zusammengesetzt = person('gehaeuse_in_schweiz_zusammengesetzt', period)
        kontrolliert = person('gehaeuse_in_schweiz_kontrolliert', period)
        kosten_anteil = person('herstellungskosten_anteil_schweiz_gehaeuse', period)

        # Art. 4 Abs. 1 lit. d: mindestens 60% Herstellungskosten in CH
        kosten_ok = kosten_anteil >= 0.60

        return fabrikation * zusammengesetzt * kontrolliert * kosten_ok
