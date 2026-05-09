"""SR 654.1 Art. 17 - Traitement des donnees

Generated from: ch/654/de/654.1.md

The ESTV may process personal data, including data on administrative
and criminal proceedings, and may systematically use the UID.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class afc_traite_donnees_personnelles(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC traite des donnees personnelles pour l'execution de l'accord et de la loi"
    reference = "SR 654.1 Art. 17 al. 1"


class afc_utilise_uid_systematiquement(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC utilise systematiquement le numero d'identification des entreprises (IDE)"
    reference = "SR 654.1 Art. 17 al. 2"
