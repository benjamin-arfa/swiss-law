"""SR 112.1 Art. 2

Generated from: ch/112/de/112.1.md

Gegen Erfuellung der vertraglichen Leistungen wird die Gemeinde Bern der
Verpflichtungen fuer den Bundessitz fuer alle Zukunft enthoben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bern_vertragliche_leistungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die vertraglichen Leistungen der Gemeinde Bern erfuellt sind"
    reference = "SR 112.1 Art. 2"


class bern_bundessitz_verpflichtung_enthoben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gemeinde Bern der Verpflichtungen fuer den Bundessitz enthoben ist"
    reference = "SR 112.1 Art. 2"

    def formula(person, period, parameters):
        return person('bern_vertragliche_leistungen_erfuellt', period)
