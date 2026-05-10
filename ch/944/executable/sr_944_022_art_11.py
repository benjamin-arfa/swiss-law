"""SR 944.022 Art. 11

Generated from: ch/944/de/944.022.md

Gebuehren: Control fees for fur declaration violations. Hourly rate CHF 200.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pelz_deklarationspflicht_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Pelzdeklarationspflicht verletzt wurde"
    reference = "SR 944.022 Art. 11 Abs. 1"


class pelz_kontrollaufwand_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zeitaufwand der Kontrolle in Stunden"
    reference = "SR 944.022 Art. 11 Abs. 2"
    default_value = 0.0


class pelz_kontrollgebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebuehr fuer Kontrolle bei Pelzdeklarationsverletzung (CHF)"
    reference = "SR 944.022 Art. 11"

    def formula(person, period, parameters):
        import numpy as np
        verletzt = person('pelz_deklarationspflicht_verletzt', period)
        stunden = person('pelz_kontrollaufwand_stunden', period)
        stundenansatz = parameters(period).sr_944_022.kontroll_stundenansatz

        return np.where(verletzt, stunden * stundenansatz, 0)
