"""SR 824.02 Art. 4

Generated from: ch/824/de/824.02.md

Anerkennung als Einsatzbetrieb und besonderes Interesse: Conditions for
recognition of profit-oriented institutions and the 30% ambulatory
service threshold.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zdpv_ist_gewinnorientiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Institution gewinnorientiert ist"
    reference = "SR 824.02 Art. 4 Abs. 1"
    default_value = False


class zdpv_dienstleistung_oeffentliches_interesse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die erbrachten Dienstleistungen im oeffentlichen Interesse liegen"
    reference = "SR 824.02 Art. 4 Abs. 1"
    default_value = False


class zdpv_anteil_ambulant_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil ambulanter Dienstleistungen in Prozent"
    reference = "SR 824.02 Art. 4 Abs. 2"
    default_value = 0.0


class zdpv_anerkennung_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anerkennung als Einsatzbetrieb fuer Pilotversuche moeglich ist"
    reference = "SR 824.02 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        gewinnorientiert = person('zdpv_ist_gewinnorientiert', period)
        oeffentlich = person('zdpv_dienstleistung_oeffentliches_interesse', period)
        # Gewinnorientierte Institutionen nur wenn Dienstleistungen im oeff. Interesse
        return np.where(gewinnorientiert, oeffentlich, True)


class zdpv_besonderes_interesse_mitwirkung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein besonderes Interesse an der Mitwirkung vorliegt (mind. 30% ambulant)"
    reference = "SR 824.02 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        anteil = person('zdpv_anteil_ambulant_prozent', period)
        return anteil >= 30
