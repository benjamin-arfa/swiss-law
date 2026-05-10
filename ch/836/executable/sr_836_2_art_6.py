"""SR 836.2 Art. 6

Generated from: ch/836/de/836.2.md

Art. 6: Verbot des Doppelbezugs - For the same child, only one allowance
of the same type may be paid. Differential payment per Art. 7 Abs. 2
is reserved.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_zulagen_gleicher_art_fuer_kind(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Zulagen derselben Art, die für dasselbe Kind ausgerichtet werden"
    reference = "SR 836.2 Art. 6"


class doppelbezug_unzulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Doppelbezug ist unzulässig: für dasselbe Kind wird mehr als eine Zulage gleicher Art beansprucht"
    reference = "SR 836.2 Art. 6"

    def formula(person, period, parameters):
        return person('anzahl_zulagen_gleicher_art_fuer_kind', period) > 1
