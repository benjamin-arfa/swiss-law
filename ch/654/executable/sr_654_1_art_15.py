"""SR 654.1 Art. 15 - Declarations pays par pays recues des Etats partenaires

Generated from: ch/654/de/654.1.md

The ESTV forwards CbC reports received from partner states to the
competent cantonal tax authorities, with use restrictions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class declaration_recue_etat_partenaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC a recu une declaration pays par pays d'un Etat partenaire"
    reference = "SR 654.1 Art. 15 al. 1"


class declaration_etrangere_transmise_cantons(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC a transmis la declaration recue aux autorites cantonales competentes"
    reference = "SR 654.1 Art. 15 al. 1"
