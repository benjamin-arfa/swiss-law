"""SR 783.018 Art. 5

Generated from: ch/783/de/783.018.md

Gebuehrenpflichtige Leistungen der Schlichtungsstelle:
- Behandlungsgebuehr: CHF 20
- Verfahrensgebuehr: nach Zeitaufwand, CHF 250/Stunde
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

BEHANDLUNGSGEBUEHR_SCHLICHTUNG = 20.0
GEBUEHRENANSATZ_SCHLICHTUNG_PRO_STUNDE = 250.0


class schlichtungsstelle_arbeitsstunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Arbeitsstunden der Schlichtungsstelle fuer Verfahrensgebuehr"
    reference = "SR 783.018 Art. 5 Abs. 2"


class schlichtungsstelle_behandlungsgebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Behandlungsgebuehr der Schlichtungsstelle in CHF (pauschal CHF 20)"
    reference = "SR 783.018 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('schlichtungsstelle_behandlungsgebuehr', period) * 0 + BEHANDLUNGSGEBUEHR_SCHLICHTUNG


class schlichtungsstelle_verfahrensgebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Verfahrensgebuehr der Schlichtungsstelle in CHF (CHF 250/Stunde)"
    reference = "SR 783.018 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        stunden = person('schlichtungsstelle_arbeitsstunden', period)
        return stunden * GEBUEHRENANSATZ_SCHLICHTUNG_PRO_STUNDE
