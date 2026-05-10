"""SR 501.31 Art. 7 - Beteiligte Institutionen

Generated from: ch/501/de/501.31.md

Das BABS wird auf Stufe Bund durch folgende Institutionen unterstuetzt:
a. Leitungskonferenz KSD
b. SANKO
c. Fachgruppen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_leitungskonferenz_ksd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Institution die Leitungskonferenz KSD ist"
    reference = "SR 501.31 Art. 7 lit. a"


class ist_sanko(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Institution das sanitaetsdienstliche Koordinationsgremium (SANKO) ist"
    reference = "SR 501.31 Art. 7 lit. b"


class ist_fachgruppe_ksd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Institution eine Fachgruppe des KSD ist"
    reference = "SR 501.31 Art. 7 lit. c"


class unterstuetzt_babs_auf_stufe_bund(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Institution das BABS auf Stufe Bund unterstuetzt"
    reference = "SR 501.31 Art. 7"

    def formula(person, period, parameters):
        return (
            person('ist_leitungskonferenz_ksd', period)
            + person('ist_sanko', period)
            + person('ist_fachgruppe_ksd', period)
        ) > 0
