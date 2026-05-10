"""SR 120.52 Art. 5

Generated from: ch/120/de/120.52.md

Nachweis gewalttaetigen Verhaltens: Evidence of violent behavior.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nachweis_gerichtsurteil_oder_anzeige(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Nachweis durch Gerichtsurteil oder polizeiliche Anzeige"
    reference = "SR 120.52 Art. 5 Abs. 1 lit. a"


class nachweis_aussagen_oder_bildaufnahmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Nachweis durch glaubwuerdige Aussagen oder Bildaufnahmen"
    reference = "SR 120.52 Art. 5 Abs. 1 lit. b"


class nachweis_stadionverbot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Nachweis durch Stadionverbot der Sportverbaende"
    reference = "SR 120.52 Art. 5 Abs. 1 lit. c"


class nachweis_auslaendische_behoerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Nachweis durch Meldung einer zustaendigen auslaendischen Behoerde"
    reference = "SR 120.52 Art. 5 Abs. 1 lit. d"


class nachweis_gewalttaetiges_verhalten_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Nachweis gewalttaetigen Verhaltens vorliegt"
    reference = "SR 120.52 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('nachweis_gerichtsurteil_oder_anzeige', period) +
            person('nachweis_aussagen_oder_bildaufnahmen', period) +
            person('nachweis_stadionverbot', period) +
            person('nachweis_auslaendische_behoerde', period)
        ) > 0
