"""SR 152.31 Art. 7

Generated from: ch/152/de/152.31.md

Content of access request: informal, no justification needed,
must contain enough information to identify the document.
10-day deadline to provide additional information.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zugangsgesuch_begruendung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Zugangsgesuch begruendet werden muss"
    reference = "SR 152.31 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return False


class zugangsgesuch_genuegend_angaben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Gesuch genuegend Angaben zur Identifizierung des Dokuments enthaelt"
    reference = "SR 152.31 Art. 7 Abs. 2"


class frist_praezisierung_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist in Tagen fuer Praezisierung des Gesuchs"
    reference = "SR 152.31 Art. 7 Abs. 4"

    def formula(person, period, parameters):
        return 10


class gesuch_gilt_als_zurueckgezogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Gesuch als zurueckgezogen gilt (keine Praezisierung innert 10 Tagen)"
    reference = "SR 152.31 Art. 7 Abs. 4"
