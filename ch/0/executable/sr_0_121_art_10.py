"""SR 0.121 Art. X

Generated from: ch/0/de/0.121.md

Each Contracting Party undertakes to exert appropriate efforts to
prevent any activity in Antarctica contrary to the principles or
purposes of the Treaty.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antarktis_verhinderung_vertragswidrige_taetigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vertragspartei Anstrengungen zur Verhinderung vertragswidriger Taetigkeiten unternimmt"
    reference = "SR 0.121 Art. X"
