"""SR 312.2 Art. 11

Generated from: ch/312/fr/312.2.md

End of witness protection program: when threat eliminated or obligations
not fulfilled. Before case closure, consultation with prosecution required.
Must end if protected person explicitly requests it.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ltem_menace_ecartee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Toute menace est ecartee"
    reference = "SR 312.2 Art. 11 al. 1 let. a"


class ltem_obligations_non_remplies(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Les obligations convenues ne sont pas remplies"
    reference = "SR 312.2 Art. 11 al. 1 let. b"


class ltem_procedure_penale_close(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La procedure penale est close par une decision entree en force"
    reference = "SR 312.2 Art. 11 al. 2"


class ltem_personne_demande_fin_programme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne a proteger demande expressement la fin du programme"
    reference = "SR 312.2 Art. 11 al. 3"


class ltem_programme_peut_etre_termine(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le programme de protection peut etre termine"
    reference = "SR 312.2 Art. 11 al. 1"

    def formula(person, period, parameters):
        menace_ecartee = person('ltem_menace_ecartee', period)
        obligations = person('ltem_obligations_non_remplies', period)
        demande = person('ltem_personne_demande_fin_programme', period)
        return (menace_ecartee + obligations + demande) > 0
