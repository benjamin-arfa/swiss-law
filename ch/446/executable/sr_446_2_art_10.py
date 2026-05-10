"""SR 446.2 Art. 10

Generated from: ch/446/de/446.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class branchenorg_zweck_jugendschutz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Branchenorganisation hat Jugendschutz als Zweck"
    reference = "SR 446.2 Art. 10 Abs. 1 Bst. a"


class branchenorg_offen_fuer_alle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Branchenorganisation steht allen Akteurinnen offen"
    reference = "SR 446.2 Art. 10 Abs. 1 Bst. b"


class branchenorg_repraesentativ(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Branchenorganisation ist repraesentativ zusammengesetzt"
    reference = "SR 446.2 Art. 10 Abs. 1 Bst. c"


class branchenorg_gesamtschweizerisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Branchenorganisation ist gesamtschweizerisch taetig"
    reference = "SR 446.2 Art. 10 Abs. 1 Bst. d"


class branchenorg_hat_anlaufstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Branchenorganisation hat eine Anlaufstelle eingesetzt"
    reference = "SR 446.2 Art. 10 Abs. 1 Bst. e"


class branchenorg_experten_beigezogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Branchenorganisation hat Experten fuer Erarbeitung der Jugendschutzregelung beigezogen"
    reference = "SR 446.2 Art. 10 Abs. 1 Bst. f"


class branchenorg_erfuellt_anforderungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Branchenorganisation erfuellt alle Anforderungen fuer Verbindlicherklaerung"
    reference = "SR 446.2 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        zweck = person('branchenorg_zweck_jugendschutz', period)
        offen = person('branchenorg_offen_fuer_alle', period)
        repraesentativ = person('branchenorg_repraesentativ', period)
        gesamt_ch = person('branchenorg_gesamtschweizerisch', period)
        anlaufstelle = person('branchenorg_hat_anlaufstelle', period)
        experten = person('branchenorg_experten_beigezogen', period)
        return zweck * offen * repraesentativ * gesamt_ch * anlaufstelle * experten
