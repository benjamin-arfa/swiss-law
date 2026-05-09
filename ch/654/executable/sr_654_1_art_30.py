"""SR 654.1 Art. 30 - Transmission de declarations portant sur des periodes anterieures

Generated from: ch/654/de/654.1.md

Transitional provision: the ESTV transmits voluntarily submitted CbC
reports for tax periods preceding the entry into force of the law.
Registration and filing deadlines apply mutatis mutandis.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class declaration_volontaire_periode_anterieure(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite a volontairement depose une declaration pour une periode anterieure a l'entree en vigueur de la loi"
    reference = "SR 654.1 Art. 30 al. 1"


class inscription_au_moment_depot_volontaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'inscription a ete effectuee au plus tard au moment du depot volontaire de la declaration"
    reference = "SR 654.1 Art. 30 al. 3"
