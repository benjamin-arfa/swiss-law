"""SR 152.21 Art. 8

Generated from: ch/152/de/152.21.md

Access during protection period: may be granted if affected persons consent,
if affected persons have been dead for at least 3 years, or if documents
were already publicly accessible.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class einwilligung_betroffener_personen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einwilligung der betroffenen Personen vorliegt"
    reference = "SR 152.21 Art. 8 Abs. 1 Bst. a"


class betroffene_personen_seit_3_jahren_tot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die betroffenen Personen seit mindestens drei Jahren tot sind"
    reference = "SR 152.21 Art. 8 Abs. 1 Bst. b"


class unterlagen_bereits_oeffentlich_zugaenglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Unterlagen der Oeffentlichkeit bereits zugaenglich waren"
    reference = "SR 152.21 Art. 8 Abs. 1 Bst. c"


class einsichtnahme_waehrend_schutzfrist_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Einsicht waehrend der Schutzfrist gewaehrt werden kann"
    reference = "SR 152.21 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        einwilligung = person('einwilligung_betroffener_personen', period)
        tot = person('betroffene_personen_seit_3_jahren_tot', period)
        oeffentlich = person('unterlagen_bereits_oeffentlich_zugaenglich', period)
        return (einwilligung + tot + oeffentlich) > 0
