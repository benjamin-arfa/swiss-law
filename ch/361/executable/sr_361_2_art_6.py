"""SR 361.2 Art. 6

Generated from: ch/361/de/361.2.md

Zugriffberechtigte Stellen: Online-Abfrageberechtigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ipas_mitarbeitende_fedpol(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Mitarbeitende/r von fedpol"
    reference = "SR 361.2 Art. 6 Abs. 1"


class ipas_daten_fuer_gesetzliche_aufgabe_benoetigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten werden zur Erfuellung gesetzlicher Aufgaben benoetigt"
    reference = "SR 361.2 Art. 6 Abs. 1"


class ipas_online_abfrage_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist zur Online-Abfrage von IPAS berechtigt"
    reference = "SR 361.2 Art. 6"

    def formula(person, period, parameters):
        fedpol = person('ipas_mitarbeitende_fedpol', period)
        benoetigt = person('ipas_daten_fuer_gesetzliche_aufgabe_benoetigt', period)
        return fedpol * benoetigt
