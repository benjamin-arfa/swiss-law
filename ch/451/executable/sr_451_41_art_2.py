"""SR 451.41 Art. 2

Generated from: ch/451/de/451.41.md
UNESCO-Uebereinkommen - Beitrag hoechstens 1% des UNESCO-Beitrags.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beitrag_unesco_haushalt_zweijahres(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zweijahres-Beitrag der Schweiz zum UNESCO-Haushalt in CHF"
    reference = "SR 451.41 Art. 2 Abs. 1"


class max_beitrag_fonds_kultur_naturgut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstbeitrag an Fonds fuer Kultur- und Naturgut (1% des UNESCO-Beitrags)"
    reference = "SR 451.41 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        unesco_beitrag = person('beitrag_unesco_haushalt_zweijahres', period)
        return unesco_beitrag * 0.01
