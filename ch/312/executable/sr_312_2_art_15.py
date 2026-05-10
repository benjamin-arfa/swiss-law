"""SR 312.2 Art. 15

Generated from: ch/312/fr/312.2.md

Financial support for protected witnesses: subsistence costs covered as long as
protection requires. Amount based on prior lawful income, assets, family situation,
support obligations, security needs. Lower limit based on social assistance
provisions at place of stay. Reimbursement if obtained through false information.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ltem_revenu_licite_anterieur_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Revenu licite percu avant le programme de protection en CHF"
    reference = "SR 312.2 Art. 15 al. 2"


class ltem_patrimoine_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Patrimoine de la personne a proteger en CHF"
    reference = "SR 312.2 Art. 15 al. 2"


class ltem_obligations_entretien(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne a des obligations d'entretien ou d'assistance"
    reference = "SR 312.2 Art. 15 al. 2"


class ltem_limite_inferieure_aide_sociale_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Limite inferieure de la prestation (aide sociale du lieu de sejour) en CHF"
    reference = "SR 312.2 Art. 15 al. 2"


class ltem_prestation_financiere_mensuelle_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Prestation financiere mensuelle du Service de protection des temoins en CHF"
    reference = "SR 312.2 Art. 15 al. 1-2"


class ltem_renseignements_inexacts_fournis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "L'interesse a fourni sciemment des renseignements inexacts"
    reference = "SR 312.2 Art. 15 al. 3"


class ltem_remboursement_prestations_exigible(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le remboursement des prestations financieres peut etre exige"
    reference = "SR 312.2 Art. 15 al. 3"

    def formula(person, period, parameters):
        return person('ltem_renseignements_inexacts_fournis', period)
