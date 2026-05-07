"""SR 631.011 Art. 4

Generated from: ch/631/de/631.011.md

Grenzweidegang — Begriffe: Definitionen fuer Tiere, inlaendische/
auslaendische Tiere, Grenzweidegang und Herkunftsland.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class tier_gattung_ist_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Tier der Pferde-, Rinder-, Schaf-, Ziegen- oder Schweinegattung angehoert"
    reference = "SR 631.011 Art. 4 Bst. a"


class tier_standplatz_im_zollgebiet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Tier seinen ordentlichen Standplatz im Zollgebiet hat (inlaendisches Tier)"
    reference = "SR 631.011 Art. 4 Bst. b"


class grenzweidegang_dauer_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Dauer des Weideaufenthalts in Tagen"
    reference = "SR 631.011 Art. 4 Bst. d"


class ist_grenzweidegang(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Grenzweidegang vorliegt (Aufenthalt > 1 Tag)"
    reference = "SR 631.011 Art. 4 Bst. d"

    def formula(person, period, parameters):
        dauer = person('grenzweidegang_dauer_tage', period)
        return dauer > 1
