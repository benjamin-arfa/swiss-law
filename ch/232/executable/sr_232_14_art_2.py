"""SR 232.14 Art. 2

Generated from: ch/232/de/232.14.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erfindung_verletzt_menschenwuerde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verwertung der Erfindung würde die Menschenwürde verletzen"
    reference = "SR 232.14 Art. 2 Abs. 1"


class erfindung_missachtet_wuerde_kreatur(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verwertung würde die Würde der Kreatur missachten"
    reference = "SR 232.14 Art. 2 Abs. 1"


class erfindung_gegen_oeffentliche_ordnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verwertung verstösst gegen die öffentliche Ordnung oder die guten Sitten"
    reference = "SR 232.14 Art. 2 Abs. 1"


class erfindung_ist_chirurgie_therapie_diagnostik(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung ist ein Verfahren der Chirurgie, Therapie oder Diagnostik am Körper"
    reference = "SR 232.14 Art. 2 Abs. 2 lit. a"


class erfindung_ist_pflanzensorte_tierrasse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung betrifft Pflanzensorten, Tierrassen oder im Wesentlichen biologische Verfahren"
    reference = "SR 232.14 Art. 2 Abs. 2 lit. b"


class erfindung_von_patentierung_ausgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung ist von der Patentierung ausgeschlossen"
    reference = "SR 232.14 Art. 2"

    def formula(person, period, parameters):
        menschenwuerde = person('erfindung_verletzt_menschenwuerde', period)
        kreatur = person('erfindung_missachtet_wuerde_kreatur', period)
        ordnung = person('erfindung_gegen_oeffentliche_ordnung', period)
        medizin = person('erfindung_ist_chirurgie_therapie_diagnostik', period)
        pflanze_tier = person('erfindung_ist_pflanzensorte_tierrasse', period)
        return menschenwuerde + kreatur + ordnung + medizin + pflanze_tier
