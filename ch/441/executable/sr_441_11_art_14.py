"""SR 441.11 Art. 14

Generated from: ch/441/de/441.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_nicht_gewinnorientiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist nicht gewinnorientiert"
    reference = "SR 441.11, Art. 14 Abs. 2 lit. b"


class taetig_in_sprachregionen_anzahl(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Sprachregionen, in denen die Organisation tätig ist"
    reference = "SR 441.11, Art. 14 Abs. 2 lit. a"


class jahre_verstaendigungstaetigkeit(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre der Sensibilisierungs-/Vernetzungstätigkeit"
    reference = "SR 441.11, Art. 14 Abs. 2 lit. c"


class berechtigung_finanzhilfe_verstaendigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigung auf Finanzhilfen zur Förderung der Verständigung (Art. 14 SpV)"
    reference = "SR 441.11, Art. 14 Abs. 2"

    def formula(self, period, parameters):
        in_min_2_regionen = self.person('taetig_in_sprachregionen_anzahl', period) >= 2
        nicht_gewinnorientiert = self.person('ist_nicht_gewinnorientiert', period)
        min_3_jahre = self.person('jahre_verstaendigungstaetigkeit', period) >= 3
        return in_min_2_regionen * nicht_gewinnorientiert * min_3_jahre


class finanzhilfe_verstaendigung_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten der Sensibilisierungs-/Vernetzungstätigkeit"
    reference = "SR 441.11, Art. 14 Abs. 4"


class finanzhilfe_verstaendigung_max_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Betrag der Finanzhilfe (höchstens 50% der Kosten)"
    reference = "SR 441.11, Art. 14 Abs. 4"

    def formula(self, period, parameters):
        kosten = self.person('finanzhilfe_verstaendigung_kosten', period)
        return kosten * 0.50
