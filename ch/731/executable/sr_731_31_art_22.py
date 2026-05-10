"""SR 731.31 Art. 22

Generated from: ch/731/de/731.31.md

Liability of the Confederation - limited liability, only for breach of
essential official duties and if damage not caused by the borrower.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_bund_haftung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Haftung des Bundes gegeben (Art. 22 Abs. 2)"
    reference = "SR 731.31 Art. 22 Abs. 2"

    def formula(person, period, parameters):
        """Art. 22 Abs. 2: Liability only if:
        a. essential official duties were breached; and
        b. damage is not attributable to the borrower's breach.
        """
        amtspflicht_verletzt = person('firevo_amtspflichtverletzung', period)
        schaden_darlehensnehmerin = person('firevo_schaden_durch_darlehensnehmerin', period)
        return amtspflicht_verletzt * not_(schaden_darlehensnehmerin)


class firevo_amtspflichtverletzung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wesentliche Amtspflichtverletzung liegt vor"
    reference = "SR 731.31 Art. 22 Abs. 2 lit. a"


class firevo_schaden_durch_darlehensnehmerin(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schaden ist auf Pflichtverletzung der Darlehensnehmerin zurueckzufuehren"
    reference = "SR 731.31 Art. 22 Abs. 2 lit. b"
