"""SR 443.1 Art. 21

Generated from: ch/443/de/443.1.md

Abgabe zur Foerderung der Angebotsvielfalt: Max 2 CHF pro Eintritt.
Verleih- und Vorfuehrunternehmen tragen die Abgabe je zur Haelfte.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_eintritte_kinoregion(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Eintritte in der Kinoregion"
    reference = "SR 443.1 Art. 21 Abs. 2"


class abgabesatz_pro_eintritt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abgabesatz pro Eintritt (max 2 CHF)"
    reference = "SR 443.1 Art. 21 Abs. 2"


class abgabe_angebotsvielfalt_gesamt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte Abgabe zur Foerderung der Angebotsvielfalt (CHF)"
    reference = "SR 443.1 Art. 21 Abs. 2"

    def formula(person, period, parameters):
        eintritte = person('anzahl_eintritte_kinoregion', period)
        satz = person('abgabesatz_pro_eintritt', period)
        import numpy as np
        satz_begrenzt = np.minimum(satz, 2.0)
        return eintritte * satz_begrenzt


class abgabe_anteil_verleih(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil Verleihunternehmen an der Abgabe (50%)"
    reference = "SR 443.1 Art. 21 Abs. 2"

    def formula(person, period, parameters):
        gesamt = person('abgabe_angebotsvielfalt_gesamt', period)
        return gesamt * 0.50
