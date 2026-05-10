"""SR 844 Art. 5

Generated from: ch/fr/844.md

Art. 5: Aide financiere pour l'amelioration du logement en regions de montagne.

Abs. 1: L'aide financiere est de 10 a 30 % des frais pouvant etre pris
en consideration, selon la capacite financiere du canton.
Dans des cas particuliers, ces pourcentages peuvent etre reduits.

Abs. 2: Sont pris en consideration les frais globaux de construction y compris
les taxes. Exclus: interets, frais d'acquisition du terrain, indemnites a des tiers.

Abs. 3: L'octroi peut etre subordonne a la preuve du financement des frais
non couverts.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lalm_capacite_financiere_canton(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Capacite financiere du canton (indice, 0 a 1)"
    reference = "SR 844 Art. 5 al. 1"


class lalm_frais_construction_globaux(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Frais globaux de construction y compris taxes (CHF)"
    reference = "SR 844 Art. 5 al. 2"


class lalm_frais_exclus(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Frais exclus: interets, acquisition terrain, indemnites tiers (CHF)"
    reference = "SR 844 Art. 5 al. 2"


class lalm_frais_pris_en_consideration(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Frais pouvant etre pris en consideration (CHF)"
    reference = "SR 844 Art. 5 al. 2"

    def formula(person, period, parameters):
        frais_globaux = person('lalm_frais_construction_globaux', period)
        frais_exclus = person('lalm_frais_exclus', period)
        return max_(frais_globaux - frais_exclus, 0)


class lalm_cas_particulier_reduction(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Cas particulier justifiant une reduction du taux d'aide"
    reference = "SR 844 Art. 5 al. 1"


class lalm_taux_aide_financiere(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taux d'aide financiere (entre 0.10 et 0.30 selon capacite du canton)"
    reference = "SR 844 Art. 5 al. 1"

    def formula(person, period, parameters):
        p = parameters(period)
        capacite = person('lalm_capacite_financiere_canton', period)
        taux_min = p.sr_844.art_5.taux_aide_min
        taux_max = p.sr_844.art_5.taux_aide_max
        # Plus la capacite financiere du canton est faible, plus le taux est eleve
        taux = taux_max - capacite * (taux_max - taux_min)
        return taux


class lalm_aide_financiere_art5(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant de l'aide financiere federale (Art. 5 LALM, CHF)"
    reference = "SR 844 Art. 5"

    def formula(person, period, parameters):
        frais = person('lalm_frais_pris_en_consideration', period)
        taux = person('lalm_taux_aide_financiere', period)
        return frais * taux
