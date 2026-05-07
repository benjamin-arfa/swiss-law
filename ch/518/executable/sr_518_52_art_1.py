"""SR 518.52 Art. 1

Generated from: ch/518/fr/518.52.md

Approval of the Additional Protocols to the Geneva Conventions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class protocole_I_approuve(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le Protocole I relatif aux conflits armes internationaux est approuve"
    reference = "SR 518.52 Art. 1 al. 1 let. a"
    default_value = True


class protocole_II_approuve(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le Protocole II relatif aux conflits armes non internationaux est approuve"
    reference = "SR 518.52 Art. 1 al. 1 let. b"
    default_value = True


class reserve_art_57_commandants_bataillon(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Reserve: Art. 57 al. 2 ne cree des obligations que pour commandants au niveau du bataillon ou superieur"
    reference = "SR 518.52 Art. 1 al. 1 let. a ch. 1"
    default_value = True


class reserve_art_58_defense_territoire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Reserve: Art. 58 applique sous reserve des exigences de la defense du territoire national"
    reference = "SR 518.52 Art. 1 al. 1 let. a ch. 2"
    default_value = True
