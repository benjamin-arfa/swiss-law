"""SR 651.1 Art. 7 - Non-entree en matiere

Generated from: ch/651/fr/651.1.md

Grounds for refusing to process a request: fishing expeditions,
information not covered by the convention, bad faith.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class demande_recherche_preuves(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La demande est deposee a des fins de recherche de preuves (fishing expedition)"
    reference = "SR 651.1 Art. 7 let. a"


class renseignements_non_prevus_convention(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La demande porte sur des renseignements non prevus par la convention applicable"
    reference = "SR 651.1 Art. 7 let. b"


class demande_viole_bonne_foi(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La demande viole le principe de la bonne foi (renseignements obtenus par actes punissables)"
    reference = "SR 651.1 Art. 7 let. c"


class non_entree_en_matiere(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Il n'est pas entre en matiere sur la demande d'assistance administrative"
    reference = "SR 651.1 Art. 7"

    def formula(self, period, parameters):
        recherche = self('demande_recherche_preuves', period)
        non_prevus = self('renseignements_non_prevus_convention', period)
        mauvaise_foi = self('demande_viole_bonne_foi', period)
        return recherche + non_prevus + mauvaise_foi > 0
