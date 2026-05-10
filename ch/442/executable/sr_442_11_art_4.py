"""SR 442.11 Art. 4

Generated from: ch/442/de/442.11.md

Nachwuchsfoerderung: Als Nachwuchs gelten Personen, die ihre kuenstlerische
Berufsausbildung nicht seit mehr als 5 Jahren abgeschlossen haben, oder deren
erste oeffentliche Praesentation nicht mehr als 5 Jahre zurueckliegt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_berufsausbildung_abschluss(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit Abschluss der kuenstlerischen Berufsausbildung in gleicher Sparte"
    reference = "SR 442.11 Art. 4 Bst. a"


class hat_berufsausbildung_gleiche_sparte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Berufsausbildung in der gleichen Kunstsparte absolviert wurde"
    reference = "SR 442.11 Art. 4 Bst. a"


class jahre_seit_erster_praesentation(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit erster oeffentlicher Praesentation eines Werks"
    reference = "SR 442.11 Art. 4 Bst. b"


class gilt_als_nachwuchs(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als kuenstlerischer Nachwuchs gilt"
    reference = "SR 442.11 Art. 4"

    def formula(person, period, parameters):
        hat_ausbildung = person('hat_berufsausbildung_gleiche_sparte', period)
        jahre_ausbildung = person('jahre_seit_berufsausbildung_abschluss', period)
        jahre_praesentation = person('jahre_seit_erster_praesentation', period)
        # a) Ausbildung in gleicher Sparte: max 5 Jahre seit Abschluss
        nachwuchs_a = hat_ausbildung * (jahre_ausbildung <= 5)
        # b) Keine Ausbildung oder andere Sparte: max 5 Jahre seit erster Praesentation
        nachwuchs_b = (1 - hat_ausbildung) * (jahre_praesentation <= 5)
        return nachwuchs_a + nachwuchs_b
