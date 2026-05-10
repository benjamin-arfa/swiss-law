"""SR 142.209 Art. 3

Generated from: ch/142/de/142.209.md

Gebuehrenpflicht: Wer eine Verfuegung oder Dienstleistung veranlasst,
muss die Gebuehr bezahlen. Solidarhaftung fuer Personen, die fuer
Auslaender ein Gesuch eingereicht haben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_verfuegung_veranlasst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine auslaenderrechtliche Verfuegung oder Dienstleistung veranlasst hat"
    reference = "SR 142.209 Art. 3 Abs. 1"


class hat_gesuch_fuer_auslaender_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person fuer eine/n Auslaender/in ein Gesuch eingereicht hat"
    reference = "SR 142.209 Art. 3 Abs. 2"


class ist_gebuehrenpflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person gebuehrenpflichtig ist"
    reference = "SR 142.209 Art. 3"

    def formula(person, period, parameters):
        return (
            person('hat_verfuegung_veranlasst', period)
            + person('hat_gesuch_fuer_auslaender_eingereicht', period)
        ) > 0
