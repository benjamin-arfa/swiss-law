"""SR 282.11 Art. 6 - Vorlaeufige Einstellung der Betreibung

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class kantonsregierung_sorgt_fuer_keine_verschlechterung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Kantonsregierung sorgt dafuer, dass sich die Lage der Glaeubiger durch die Einstellung nicht verschlechtert"
    reference = "SR 282.11 Art. 6 Abs. 1"


class massnahmen_kantonsregierung_genuegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die von der Kantonsregierung getroffenen Massnahmen genuegen"
    reference = "SR 282.11 Art. 6 Abs. 2"


# Computed variables

class betreibung_kann_eingestellt_werden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Aufsichtsbehoerde kann die Betreibung voruebergehend einstellen"
    reference = "SR 282.11 Art. 6 Abs. 1"

    def formula(self, period, parameters):
        return self('kantonsregierung_sorgt_fuer_keine_verschlechterung', period)


class glaeubiger_kann_fortsetzung_verlangen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Glaeubiger kann die Fortsetzung der Betreibung verlangen"
    reference = "SR 282.11 Art. 6 Abs. 2"

    def formula(self, period, parameters):
        genuegen = self('massnahmen_kantonsregierung_genuegen', period)
        return 1 - genuegen
