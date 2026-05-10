"""SR 711 Art. 19

Generated from: ch/fr/711.md

Fixation de l'indemnite (Indemnity determination) for expropriation.
Components: (a) full market value of expropriated right, (abis) for agricultural land
under LDFR: 3x max price per Art. 66(1) LDFR, (b) depreciation of remaining part
in partial expropriation, (c) all other foreseeable damages.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

MULTIPLICATEUR_TERRAIN_AGRICOLE = 3  # 3x le prix maximal LDFR


class valeur_venale_droit_exproprie_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Valeur venale du droit exproprie (CHF)"
    reference = "SR 711 Art. 19 let. a"


class est_terrain_cultivable_ldfr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le terrain est un terrain cultivable au sens de la LDFR"
    reference = "SR 711 Art. 19 let. abis"


class prix_maximal_ldfr_art66_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Prix maximal determine selon Art. 66 al. 1 LDFR (CHF)"
    reference = "SR 711 Art. 19 let. abis"


class indemnite_terrain_agricole_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Indemnite pour terrain cultivable LDFR = 3x prix maximal (CHF)"
    reference = "SR 711 Art. 19 let. abis"

    def formula(person, period):
        est_agricole = person('est_terrain_cultivable_ldfr', period)
        prix_max = person('prix_maximal_ldfr_art66_chf', period)
        return est_agricole * prix_max * MULTIPLICATEUR_TERRAIN_AGRICOLE


class depreciation_partie_restante_art19_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Reduction de la valeur venale de la partie restante (CHF)"
    reference = "SR 711 Art. 19 let. b"


class autres_prejudices_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Montant de tous autres prejudices previsibles (CHF)"
    reference = "SR 711 Art. 19 let. c"


class indemnite_totale_expropriation_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Indemnite totale d'expropriation (CHF)"
    reference = "SR 711 Art. 19"

    def formula(person, period):
        import numpy as np
        est_agricole = person('est_terrain_cultivable_ldfr', period)
        valeur_venale = person('valeur_venale_droit_exproprie_chf', period)
        terrain_agricole = person('indemnite_terrain_agricole_chf', period)
        depreciation = person('depreciation_partie_restante_art19_chf', period)
        autres = person('autres_prejudices_chf', period)

        # let. a/abis: valeur venale OU 3x prix agricole (si terrain cultivable LDFR)
        composante_a = np.where(est_agricole, terrain_agricole, valeur_venale)

        return composante_a + depreciation + autres
