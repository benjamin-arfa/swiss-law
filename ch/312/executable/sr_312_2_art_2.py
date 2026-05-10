"""SR 312.2 Art. 2

Generated from: ch/312/fr/312.2.md

Scope of witness protection: applies to persons whose life or physical
integrity is endangered due to cooperation in criminal proceedings,
and whose cooperation is disproportionately important to prosecution.
Also applies to close relatives (Art. 168 al. 1-3 CPP).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ltem_personne_collabore_procedure_penale(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne collabore ou veut collaborer dans une procedure penale"
    reference = "SR 312.2 Art. 2 al. 1 let. a"


class ltem_danger_vie_integrite_corporelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Danger mettant en peril la vie ou l'integrite corporelle"
    reference = "SR 312.2 Art. 2 al. 1 let. a"


class ltem_poursuite_entravee_sans_collaboration(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La poursuite penale serait entravee de maniere disproportionnee sans collaboration"
    reference = "SR 312.2 Art. 2 al. 1 let. b"


class ltem_est_proche_temoin_art168(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Personne ayant une relation au sens de l'art. 168 al. 1-3 CPP avec le temoin"
    reference = "SR 312.2 Art. 2 al. 2"


class ltem_dans_champ_application(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne entre dans le champ d'application de la loi sur la protection des temoins"
    reference = "SR 312.2 Art. 2"

    def formula(person, period, parameters):
        collabore = person('ltem_personne_collabore_procedure_penale', period)
        danger = person('ltem_danger_vie_integrite_corporelle', period)
        entravee = person('ltem_poursuite_entravee_sans_collaboration', period)
        proche = person('ltem_est_proche_temoin_art168', period)
        temoin_direct = collabore * danger * entravee
        return (temoin_direct + proche) > 0
