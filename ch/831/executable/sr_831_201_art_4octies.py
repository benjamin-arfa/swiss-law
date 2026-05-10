"""SR 831.201 Art. 4octies

Generated from: ch/831/de/831.201.md

Art. 4octies: Beitrag an den Arbeitgeber - Employer contribution for
integration measures, maximum CHF 100 per day.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_integrationsmassnahme_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Tage mit Integrationsmassnahmen im Monat"
    reference = "SR 831.201 Art. 4octies Abs. 1"


class iv_beitrag_arbeitgeber_integration(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Beitrag an Arbeitgeber fuer Integrationsmassnahmen (max. 100 CHF/Tag)"
    reference = "SR 831.201 Art. 4octies"

    def formula(person, period, parameters):
        tage = person('iv_integrationsmassnahme_tage', period)

        # Abs. 1: hoechstens 100 Franken pro Tag
        max_pro_tag = 100
        return tage * max_pro_tag
