"""SR 922.0 Art. 12 & 13

Generated from: ch/922/de/922.0.md

Art. 12: Verhütung von Wildschaden und Gefährdung von Menschen:
- Cantons take measures to prevent wildlife damage
- Measures against individual animals causing significant damage or endangering humans
- Self-defense measures by affected parties
- Wolves of a pack may be regulated June-August if damaging cattle/horses

Art. 13: Entschädigung von Wildschaden - Compensation for wildlife damage:
- Damage by huntable animals to forest/agriculture/livestock is compensated appropriately
- Exception: damage by animals against which self-defense is allowed
- Not for trivial damage; reasonable prevention measures must have been taken
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jsg_wildschaden_an_wald(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wildschaden an Wald (CHF)"
    reference = "SR 922.0 Art. 13 Abs. 1"


class jsg_wildschaden_an_landwirtschaft(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wildschaden an landwirtschaftlichen Kulturen (CHF)"
    reference = "SR 922.0 Art. 13 Abs. 1"


class jsg_wildschaden_an_nutztieren(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wildschaden an Nutztieren (CHF)"
    reference = "SR 922.0 Art. 13 Abs. 1"


class jsg_schaden_durch_jagdbare_art(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Schaden wurde durch ein Tier einer jagdbaren Art verursacht"
    reference = "SR 922.0 Art. 13 Abs. 1"


class jsg_selbsthilfe_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Selbsthilfemassnahmen gegen diese Tierart sind zulässig (Art. 12 Abs. 3)"
    reference = "SR 922.0 Art. 12 Abs. 3"


class jsg_verhuetungsmassnahmen_getroffen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zumutbare Massnahmen zur Verhütung von Wildschaden wurden getroffen"
    reference = "SR 922.0 Art. 13 Abs. 2"


class jsg_ist_bagatellschaden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Wildschaden ist ein Bagatellschaden"
    reference = "SR 922.0 Art. 13 Abs. 2"


class jsg_wildschaden_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamter Wildschaden (CHF)"
    reference = "SR 922.0 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        wald = person('jsg_wildschaden_an_wald', period)
        landwirtschaft = person('jsg_wildschaden_an_landwirtschaft', period)
        nutztiere = person('jsg_wildschaden_an_nutztieren', period)
        return wald + landwirtschaft + nutztiere


class jsg_wildschaden_entschaedigungsberechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Wildschaden ist entschädigungsberechtigt nach Art. 13"
    reference = "SR 922.0 Art. 13 Abs. 1-2"

    def formula(person, period, parameters):
        jagdbar = person('jsg_schaden_durch_jagdbare_art', period)
        selbsthilfe = person('jsg_selbsthilfe_zulaessig', period)
        verhuetung = person('jsg_verhuetungsmassnahmen_getroffen', period)
        bagatell = person('jsg_ist_bagatellschaden', period)
        total = person('jsg_wildschaden_total', period)

        # Compensable if: caused by huntable animal, no self-defense allowed,
        # not trivial, prevention measures taken, and actual damage > 0
        return jagdbar * (1 - selbsthilfe) * verhuetung * (1 - bagatell) * (total > 0)


class jsg_wolf_regulierung_sommer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Wolfsregulierung im Sommer zulässig (Art. 12 Abs. 4bis: Juni-August)"
    reference = "SR 922.0 Art. 12 Abs. 4bis"

    def formula(person, period, parameters):
        ist_wolf = person('jsg_ist_wolf', period)
        monat = period.start.month
        # June 1 to August 31
        im_zeitraum = (monat >= 6) * (monat <= 8)
        return ist_wolf * im_zeitraum
