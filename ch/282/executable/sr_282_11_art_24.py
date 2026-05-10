"""SR 282.11 Art. 24 - Einbeziehung anderer Glaeubiger

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class sanierung_ohne_einbeziehung_unmoeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Sanierung wuerde ohne Einbeziehung anderer Glaeubiger unbilligerweise verunmoeglicht"
    reference = "SR 282.11 Art. 24 Abs. 2"


class forderungen_anderer_glaeubiger_ueber_ein_drittel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Forderungen anderer Glaeubiger uebersteigen einen Drittel des Obligationenkapitals"
    reference = "SR 282.11 Art. 24 Abs. 3"


class einfache_mehrheit_anderer_glaeubiger_zugestimmt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die einfache Mehrheit der anderen Glaeubiger hat zugestimmt"
    reference = "SR 282.11 Art. 24 Abs. 3"


class forderungen_ueber_haelfte_gesamtbetrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die vertretenen Forderungen machen mehr als die Haelfte des Gesamtbetrags aus"
    reference = "SR 282.11 Art. 24 Abs. 3"


# Computed variables

class einbeziehung_anderer_glaeubiger_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Einbeziehung anderer Glaeubiger mit Opferauflage ist zulaessig"
    reference = "SR 282.11 Art. 24"

    def formula(self, period, parameters):
        sanierung = self('sanierung_ohne_einbeziehung_unmoeglich', period)
        ueber_drittel = self('forderungen_anderer_glaeubiger_ueber_ein_drittel', period)
        mehrheit = self('einfache_mehrheit_anderer_glaeubiger_zugestimmt', period)
        haelfte = self('forderungen_ueber_haelfte_gesamtbetrag', period)
        # Wenn unter Drittel: Billigkeit genuegt
        # Wenn ueber Drittel: braucht einfache Mehrheit und Haelfte der Forderungen
        unter_drittel_ok = sanierung * (1 - ueber_drittel)
        ueber_drittel_ok = sanierung * ueber_drittel * mehrheit * haelfte
        return unter_drittel_ok + ueber_drittel_ok > 0
