"""SR 857.51 Art. 3

Generated from: ch/857/de/857.51.md

Information der Bundesbehoerden: Kantone bringen dem Bundesamt zur Kenntnis:
- ihre Bestimmungen ueber Beratungsstellen
- jede Verweigerung einer Anerkennung
- Organisation, Zusammensetzung und Taetigkeitsbericht jeder Beratungsstelle
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kanton_bestimmungen_beratungsstellen_mitgeteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hat der Kanton dem Bundesamt seine Bestimmungen ueber Beratungsstellen mitgeteilt?"
    reference = "SR 857.51 Art. 3 lit. a"


class kanton_anerkennungsverweigerung_mitgeteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hat der Kanton jede Verweigerung einer Anerkennung dem Bundesamt mitgeteilt?"
    reference = "SR 857.51 Art. 3 lit. b"


class kanton_organisation_taetigkeitsbericht_mitgeteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hat der Kanton Organisation, personelle Zusammensetzung und Taetigkeitsbericht dem Bundesamt mitgeteilt?"
    reference = "SR 857.51 Art. 3 lit. c"


class kanton_informationspflicht_bundesbehoerden_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hat der Kanton alle Informationspflichten gegenueber den Bundesbehoerden erfuellt?"
    reference = "SR 857.51 Art. 3"

    def formula(person, period, parameters):
        bestimmungen = person('kanton_bestimmungen_beratungsstellen_mitgeteilt', period)
        verweigerung = person('kanton_anerkennungsverweigerung_mitgeteilt', period)
        organisation = person('kanton_organisation_taetigkeitsbericht_mitgeteilt', period)
        return bestimmungen * verweigerung * organisation
