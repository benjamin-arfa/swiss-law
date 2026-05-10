"""SR 161.18 Art. 18

Generated from: ch/161/de/161.18.md

Rueckerstattung unrechtmaessig erhaltener Zuwendungen:
innert 30 Tagen, Meldung an EFK innert 5 Tagen danach.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_anonyme_zuwendung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine anonyme Zuwendung handelt"
    reference = "SR 161.18 Art. 18 Abs. 1"


class ist_zuwendung_aus_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Zuwendung aus dem Ausland handelt"
    reference = "SR 161.18 Art. 18 Abs. 1"


class zuwendung_rueckerstattungspflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zuwendung innert 30 Tagen rueckzuerstatten ist"
    reference = "SR 161.18 Art. 18 Abs. 1"

    def formula(person, period, parameters):
        anonym = person('ist_anonyme_zuwendung', period)
        ausland = person('ist_zuwendung_aus_ausland', period)
        return anonym + ausland > 0
