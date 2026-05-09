"""SR 654.1 Art. 18 - Systeme d'information

Generated from: ch/654/de/654.1.md

The ESTV operates an information system for processing CbC report data.
Art. 18 defines its purposes and access rules.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class systeme_information_afc_operationnel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le systeme d'information de l'AFC pour les declarations pays par pays est operationnel"
    reference = "SR 654.1 Art. 18 al. 1"


class acces_consultation_cantons_accorde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC a accorde aux autorites cantonales un acces en ligne aux donnees du systeme d'information"
    reference = "SR 654.1 Art. 18 al. 5"
