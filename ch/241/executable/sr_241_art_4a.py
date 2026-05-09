"""SR 241 Art. 4a

Generated from: ch/de/241.md

Active and passive bribery in the private sector.
Contractually approved or minor socially customary advantages
do not count as undue advantages.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bestechung_privatsektor_aktiv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob aktive Bestechung im privaten Sektor vorliegt (Vorteil anbieten/versprechen/gewaehren)"
    reference = "SR 241 Art. 4a Abs. 1 Bst. a"


class bestechung_privatsektor_passiv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob passive Bestechung im privaten Sektor vorliegt (Vorteil fordern/annehmen)"
    reference = "SR 241 Art. 4a Abs. 1 Bst. b"


class vorteil_vertraglich_genehmigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Vorteil vertraglich vom Dritten genehmigt ist"
    reference = "SR 241 Art. 4a Abs. 2"


class vorteil_geringfuegig_sozial_ueblich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Vorteil geringfuegig und sozial ueblich ist"
    reference = "SR 241 Art. 4a Abs. 2"


class bestechung_privatsektor_unlauter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob unlautere Bestechung im Privatsektor nach Art. 4a vorliegt"
    reference = "SR 241 Art. 4a"

    def formula(person, period, parameters):
        bestechung = (
            person('bestechung_privatsektor_aktiv', period)
            + person('bestechung_privatsektor_passiv', period)
        ) > 0
        ausnahme = (
            person('vorteil_vertraglich_genehmigt', period)
            + person('vorteil_geringfuegig_sozial_ueblich', period)
        ) > 0
        return bestechung * (1 - ausnahme)
