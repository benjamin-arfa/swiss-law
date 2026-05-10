"""SR 161.18 Art. 17

Generated from: ch/161/de/161.18.md

Dauer der Veroeffentlichung und Aufbewahrung: 5 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahr_eingang_meldung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des Eingangs der Meldung bei der EFK"
    reference = "SR 161.18 Art. 17 Abs. 1"


class meldung_noch_veroeffentlicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Meldung noch veroeffentlicht ist (5 Jahre nach Eingang)"
    reference = "SR 161.18 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        eingang = person('jahr_eingang_meldung', period)
        aktuell = person('aktuelles_jahr', period)
        return (aktuell - eingang) <= 5
