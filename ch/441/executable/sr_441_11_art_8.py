"""SR 441.11 Art. 8

Generated from: ch/441/de/441.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kaderstufe(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Kaderstufe (keine, mittel, mittel_fuehrung, hoeher)"
    reference = "SR 441.11, Art. 8"


class erforderliche_sprachkenntnisse_zweite_amtssprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfügt über erforderliche Kenntnisse einer zweiten Amtssprache"
    reference = "SR 441.11, Art. 8 Abs. 1 lit. a"


class gute_aktive_kenntnisse_zweite_amtssprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfügt über gute aktive Kenntnisse mindestens einer zweiten Amtssprache"
    reference = "SR 441.11, Art. 8 Abs. 1 lit. b"


class passive_kenntnisse_dritte_amtssprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfügt über passive Kenntnisse einer dritten Amtssprache"
    reference = "SR 441.11, Art. 8 Abs. 1 lit. c"


class erfuellt_sprachanforderungen_kader(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfüllt Sprachanforderungen gemäss Kaderstufe"
    reference = "SR 441.11, Art. 8 Abs. 1"

    def formula(self, period, parameters):
        stufe = self.person('kaderstufe', period)
        zweite = self.person('erforderliche_sprachkenntnisse_zweite_amtssprache', period)
        aktiv_zweite = self.person('gute_aktive_kenntnisse_zweite_amtssprache', period)
        passiv_dritte = self.person('passive_kenntnisse_dritte_amtssprache', period)

        # All employees: at least functional knowledge of a second official language
        basis = (stufe == 'keine') * zweite

        # Middle management: good active knowledge of 2nd, if possible passive of 3rd
        mittel = (stufe == 'mittel') * aktiv_zweite

        # Senior management or middle management with leadership: 2nd active + 3rd passive
        hoeher = ((stufe == 'hoeher') + (stufe == 'mittel_fuehrung')) * aktiv_zweite * passiv_dritte

        return basis + mittel + hoeher


class frist_sprachverbesserung_kader_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist für Verbesserung der Sprachkenntnisse bei Kaderanstellung (12 Monate)"
    reference = "SR 441.11, Art. 8 Abs. 3"

    def formula(self, period, parameters):
        return 12
