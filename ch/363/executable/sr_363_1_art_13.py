"""SR 363.1 Art. 13

Generated from: ch/363/de/363.1.md

Bearbeitung der Loeschmeldungen. Ohne Meldung: Loeschung nach 30 Jahren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dna_profil_loeschmeldung_erhalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fedpol hat eine Loeschmeldung fuer den DNA-Datensatz erhalten"
    reference = "SR 363.1 Art. 13 Abs. 1"


class jahre_seit_erkennungsdienstlicher_erfassung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit der erkennungsdienstlichen Erfassung der betroffenen Person"
    reference = "SR 363.1 Art. 13 Abs. 2"


class dna_personenprofil_zu_loeschen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "DNA-Personenprofil ist zu loeschen (auf Meldung oder nach 30 Jahren)"
    reference = "SR 363.1 Art. 13"

    def formula(person, period, parameters):
        meldung = person('dna_profil_loeschmeldung_erhalten', period)
        jahre = person('jahre_seit_erkennungsdienstlicher_erfassung', period)
        return meldung + (jahre >= 30)
