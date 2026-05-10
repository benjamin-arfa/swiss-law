"""SR 351.6 Art. 15

Generated from: ch/351/de/351.6.md
Compensation rules for proceedings requested by the ICC.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verfolgte_hat_haft_verursacht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfolgte Person hat die Untersuchung oder Haft schuldhaft verursacht"
    reference = "SR 351.6 Art. 15 Abs. 2"


class verfahren_mutwillig_erschwert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfolgte Person hat das Verfahren mutwillig erschwert oder verlaengert"
    reference = "SR 351.6 Art. 15 Abs. 2"


class icc_festnahmeersuchen_zurueckgezogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "ICC hat das Festnahmeersuchen zum Zweck der Ueberstellung zurueckgezogen"
    reference = "SR 351.6 Art. 15 Abs. 3 lit. a"


class icc_ersuchen_nicht_fristgerecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "ICC hat das Ueberstellungsersuchen nicht fristgerecht eingereicht"
    reference = "SR 351.6 Art. 15 Abs. 3 lit. b"


class icc_hat_entschaedigung_zugesprochen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "ICC hat nach Art. 85 Statut eine Entschaedigung zugesprochen oder abgelehnt"
    reference = "SR 351.6 Art. 15 Abs. 4"


class entschaedigung_herabsetzbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entschaedigung kann herabgesetzt oder verweigert werden"
    reference = "SR 351.6 Art. 15 Abs. 2-3"

    def formula(person, period):
        schuldhaft = person('verfolgte_hat_haft_verursacht', period)
        mutwillig = person('verfahren_mutwillig_erschwert', period)
        zurueckgezogen = person('icc_festnahmeersuchen_zurueckgezogen', period)
        nicht_fristgerecht = person('icc_ersuchen_nicht_fristgerecht', period)
        return schuldhaft + mutwillig + zurueckgezogen + nicht_fristgerecht


class entschaedigung_verweigert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entschaedigung wird verweigert"
    reference = "SR 351.6 Art. 15 Abs. 4"

    def formula(person, period):
        # Verweigert, soweit ICC nach Art. 85 Statut bereits entschieden hat
        return person('icc_hat_entschaedigung_zugesprochen', period)
