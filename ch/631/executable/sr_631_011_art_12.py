"""SR 631.011 Art. 12

Generated from: ch/631/de/631.011.md

Milch und Milchprodukte: Zollfreiheit fuer Milch und Milchprodukte
von Nutztieren im Grenzweidegang.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tier_im_tierverzeichnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Nutztier im Tierverzeichnis nach Art. 9 Abs. 2 aufgefuehrt ist"
    reference = "SR 631.011 Art. 12 Abs. 1"


class ist_inlaendisches_tier(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Tier ein inlaendisches Tier ist"
    reference = "SR 631.011 Art. 12 Abs. 2"


class milchprodukte_wiedereinfuhr_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Tage seit Wiedereinfuhr der Tiere ins Zollgebiet"
    reference = "SR 631.011 Art. 12 Abs. 2"


class milchprodukte_grenzweidegang_zollfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Milch/Milchprodukte aus dem Grenzweidegang zollfrei sind"
    reference = "SR 631.011 Art. 12"

    def formula(person, period, parameters):
        im_verzeichnis = person('tier_im_tierverzeichnis', period)
        inlaendisch = person('ist_inlaendisches_tier', period)
        tage_seit_einfuhr = person('milchprodukte_wiedereinfuhr_tage', period)
        frist = parameters(period).sr_631_011.milchprodukte_wiedereinfuhr_frist_tage

        # Abs. 1: zollfrei wenn im Tierverzeichnis
        # Abs. 2: Milchprodukte inlaendischer Tiere innerhalb Frist
        return im_verzeichnis * (
            (1 - inlaendisch)  # auslaendische Tiere: immer zollfrei
            + inlaendisch * (tage_seit_einfuhr <= frist)
        )
