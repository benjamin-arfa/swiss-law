"""SR 0.142.116.907 Art. 8

Generated from: ch/0/de/0.142.116.907.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class swiss_slovak_agreement_authorities(Variable):
    value_type = bool
    entity = None  # Agreement-specific entity: not relevant to individual-level data
    definition_period = YEAR
    label = "Switzerland-Slovakia agreement on social security authorities"

    def formula(effects, period, parameters):
        is_swiss = effects["countries"] == "CH"
        is_slovak = effects["countries"] == "SK"
        swiss_authority = ["Eidgenössisches Justiz- und Polizeidepartement", "Bundesamt für Industrie, Gewerbe und Arbeit", "Staatssekretariat für Migration (SEM)"]
        slovak_authority = ["Ministerium für Arbeit, Soziales und Familie der Slowakischen Republik", "Verwaltung des Beschäftigungsdienstes in Bratislava"]
        return (is_swiss & set(effects["responsibility_swiss"]) == set(swiss_authority)) | (is_slovak & set(effects["responsibility_slovak"]) == set(slovak_authority))
