"""SR 312.2 Art. 7

Generated from: ch/312/fr/312.2.md

Examination of request: Service examines danger level, compliance ability,
prior convictions, sufficiency of cantonal/CPP measures (Art. 149-151),
and public interest in prosecution.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ltem_danger_considerable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne est exposee a un danger considerable"
    reference = "SR 312.2 Art. 7 al. 1 let. a"


class ltem_peut_satisfaire_conditions_programme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne peut satisfaire aux conditions du programme de protection"
    reference = "SR 312.2 Art. 7 al. 1 let. b"


class ltem_condamnations_anterieures(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne a des condamnations anterieures ou circonstances presentant un risque"
    reference = "SR 312.2 Art. 7 al. 1 let. c"


class ltem_mesures_cantonales_suffisantes(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Les mesures cantonales ou procedurales (art. 149-151 CPP) sont suffisantes"
    reference = "SR 312.2 Art. 7 al. 1 let. d"


class ltem_interet_public_preponderant(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Interet public preponderant a poursuivre penalement l'auteur"
    reference = "SR 312.2 Art. 7 al. 1 let. e"


class ltem_programme_protection_justifie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le programme de protection des temoins est justifie selon l'examen"
    reference = "SR 312.2 Art. 7 al. 1"

    def formula(person, period, parameters):
        danger = person('ltem_danger_considerable', period)
        conditions = person('ltem_peut_satisfaire_conditions_programme', period)
        mesures_insuff = not_(person('ltem_mesures_cantonales_suffisantes', period))
        interet = person('ltem_interet_public_preponderant', period)
        return danger * conditions * mesures_insuff * interet
