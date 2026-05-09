"""SR 654.1 Art. 13 - Transmission et utilisation des declarations pays par pays

Generated from: ch/654/de/654.1.md

The ESTV transmits the CbC reports to partner states and cantonal authorities,
subject to confidentiality and use restrictions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class declaration_transmise_etats_partenaires(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La declaration pays par pays a ete transmise aux autorites competentes des Etats partenaires"
    reference = "SR 654.1 Art. 13 al. 1"


class declaration_transmise_autorites_cantonales(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La declaration pays par pays a ete transmise aux autorites cantonales competentes"
    reference = "SR 654.1 Art. 13 al. 2"


class restrictions_utilisation_communiquees(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Les restrictions d'utilisation et obligations de confidentialite ont ete communiquees"
    reference = "SR 654.1 Art. 13 al. 3"
