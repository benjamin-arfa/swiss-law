"""SR 441.11 Art. 16

Generated from: ch/441/de/441.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class taetig_in_min_3_sprachregionen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist in mindestens drei Sprachregionen tätig"
    reference = "SR 441.11, Art. 16 Abs. 2 lit. a"

    def formula(self, period, parameters):
        return self.person('taetig_in_sprachregionen_anzahl', period) >= 3


class ist_gemeinnuetzig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist gemeinnützig tätig"
    reference = "SR 441.11, Art. 16 Abs. 2 lit. c"


class ist_politisch_konfessionell_neutral(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist politisch und konfessionell neutral"
    reference = "SR 441.11, Art. 16 Abs. 2 lit. d"


class berechtigung_finanzhilfe_uebersetzungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigung auf Finanzhilfen für Übersetzungen (Art. 16 SpV)"
    reference = "SR 441.11, Art. 16 Abs. 2"

    def formula(self, period, parameters):
        in_3_regionen = self.person('taetig_in_min_3_sprachregionen', period)
        nicht_gewinn = self.person('ist_nicht_gewinnorientiert', period)
        gemeinnuetzig = self.person('ist_gemeinnuetzig', period)
        neutral = self.person('ist_politisch_konfessionell_neutral', period)
        # Must not already receive Art. 14 aid (Art. 16 Abs. 3)
        kein_art14 = not_(self.person('berechtigung_finanzhilfe_verstaendigung', period))
        return in_3_regionen * nicht_gewinn * gemeinnuetzig * neutral * kein_art14
