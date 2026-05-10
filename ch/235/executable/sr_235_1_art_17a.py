"""SR 235.1 Art. 17a

Generated from: ch/235/de/235.1.md

Automatisierte Datenbearbeitung im Rahmen von Pilotversuchen.
Enthaelt konkrete Fristen (2 Jahre Evaluationsbericht, 5 Jahre Hoechstdauer).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_pilotsystem_in_betrieb_seit_jahren(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Jahre seit Inbetriebnahme des Pilotsystems"
    reference = "SR 235.1 Art. 17a Abs. 4-5"


class dsg_gesetz_formell_in_kraft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesetz im formellen Sinn mit erforderlicher Rechtsgrundlage ist in Kraft getreten"
    reference = "SR 235.1 Art. 17a Abs. 5"


class dsg_evaluationsbericht_frist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer Evaluationsbericht an Bundesrat in Jahren"
    reference = "SR 235.1 Art. 17a Abs. 4"

    def formula(person, period, parameters):
        return person('dsg_pilotsystem_in_betrieb_seit_jahren', period) * 0 + 2


class dsg_pilotsystem_hoechstdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstdauer eines Pilotsystems ohne formelle Rechtsgrundlage in Jahren"
    reference = "SR 235.1 Art. 17a Abs. 5"

    def formula(person, period, parameters):
        return person('dsg_pilotsystem_in_betrieb_seit_jahren', period) * 0 + 5


class dsg_pilotsystem_muss_abgebrochen_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Automatisierte Datenbearbeitung im Pilotversuch muss abgebrochen werden"
    reference = "SR 235.1 Art. 17a Abs. 5"

    def formula(person, period, parameters):
        jahre = person('dsg_pilotsystem_in_betrieb_seit_jahren', period)
        gesetz_in_kraft = person('dsg_gesetz_formell_in_kraft', period)
        return (jahre >= 5) * not_(gesetz_in_kraft)
