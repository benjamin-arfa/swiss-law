"""SR 196.1 Art. 26

Generated from: ch/196/de/196.1.md

Verletzung der Melde- und Auskunftspflicht: Strafbestimmung fuer Verletzung
der Pflichten nach Art. 7.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_meldepflicht_vorsaetzlich_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person vorsaetzlich die Melde- und Auskunftspflicht nach Art. 7 verletzt hat"
    reference = "SR 196.1 Art. 26 Abs. 1"


class hat_meldepflicht_fahrlaessig_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person fahrlaessig die Melde- und Auskunftspflicht verletzt hat"
    reference = "SR 196.1 Art. 26 Abs. 2"


class maximale_busse_meldepflichtverletzung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse in CHF bei Verletzung der Meldepflicht"
    reference = "SR 196.1 Art. 26"

    def formula(person, period, parameters):
        vorsatz = person('hat_meldepflicht_vorsaetzlich_verletzt', period)
        fahrlaessig = person('hat_meldepflicht_fahrlaessig_verletzt', period)
        # Vorsaetzlich: max 250'000; fahrlaessig: max 100'000
        return vorsatz * 250000 + fahrlaessig * (1 - vorsatz) * 100000
