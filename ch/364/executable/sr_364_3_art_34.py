"""SR 364.3 Art. 34

Generated from: ch/364/de/364.3.md

Foerderung der Ausbildung: Pauschalbetrag von 180 CHF pro Kursteilnehmer und Tag.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_kursteilnehmer(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Kursteilnehmerinnen und -teilnehmer"
    reference = "SR 364.3 Art. 34"


class anzahl_ausbildungstage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Ausbildungstage"
    reference = "SR 364.3 Art. 34"


class ausbildungsverguetung_bund(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verguetung des Bundes an Kantone fuer Ausbildung im Bereich Rueckfuehrungen (CHF)"
    reference = "SR 364.3 Art. 34"

    def formula(person, period, parameters):
        teilnehmer = person('anzahl_kursteilnehmer', period)
        tage = person('anzahl_ausbildungstage', period)
        return teilnehmer * tage * 180.0
