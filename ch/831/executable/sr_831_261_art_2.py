"""SR 831.261 Art. 2

Generated from: ch/831/de/831.261.md

Control: authorized organizations must notify EDI of changes to
their statutory purpose, legal form, or name. EDI checks ongoing
compliance with requirements.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class organisation_zweck_geaendert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation ihren statutarischen Zweck geaendert hat"
    reference = "SR 831.261 Art. 2 Abs. 1"


class organisation_rechtsform_geaendert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation ihre Rechtsform geaendert hat"
    reference = "SR 831.261 Art. 2 Abs. 1"


class organisation_bezeichnung_geaendert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation ihre Bezeichnung geaendert hat"
    reference = "SR 831.261 Art. 2 Abs. 1"


class organisation_meldepflicht_edi(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Meldepflicht der Organisation gegenueber dem EDI"
    reference = "SR 831.261 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        zweck = person('organisation_zweck_geaendert', period)
        rechtsform = person('organisation_rechtsform_geaendert', period)
        bezeichnung = person('organisation_bezeichnung_geaendert', period)
        return zweck + rechtsform + bezeichnung > 0
