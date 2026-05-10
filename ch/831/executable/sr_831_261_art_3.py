"""SR 831.261 Art. 3

Generated from: ch/831/de/831.261.md

Applications: Organizations meeting the requirements of Art. 9 IFEG
can be added to the list of complaint-authorized organizations.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class organisation_erfuellt_art9_ifeg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation die Voraussetzungen nach Art. 9 IFEG erfuellt"
    reference = "SR 831.261 Art. 3"


class organisation_aufnahme_verzeichnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufnahme der Organisation in das Verzeichnis der beschwerdeberechtigten Organisationen"
    reference = "SR 831.261 Art. 3"

    def formula(person, period, parameters):
        return person('organisation_erfuellt_art9_ifeg', period)
