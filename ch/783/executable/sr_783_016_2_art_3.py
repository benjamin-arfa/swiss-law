"""SR 783.016.2 Art. 3

Generated from: ch/783/de/783.016.2.md

Auskunft ueber die Einhaltung der Mindeststandards: Anbieterinnen mit
ordentlicher Meldepflicht muessen jaehrlich den Nachweis erbringen.
PostCom kann von allen Anbieterinnen Auskunft verlangen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_ordentlich_meldepflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anbieterin der ordentlichen Meldepflicht unterliegt"
    reference = "SR 783.016.2 Art. 3 Abs. 1"


class pflicht_jaehrlicher_nachweis_mindeststandards(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anbieterin jaehrlich den Nachweis der Einhaltung der Mindeststandards erbringen muss"
    reference = "SR 783.016.2 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_ordentlich_meldepflichtig', period)
