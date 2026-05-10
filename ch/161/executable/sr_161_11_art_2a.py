"""SR 161.11 Art. 2a

Generated from: ch/161/fr/161.11.md

Federal voting dates: 4 reserved Sundays per year:
a) 4th Sunday before Easter, b) Sunday after Pentecost,
c) Sunday after Jeune federal, d) last Sunday of November.
No federal vote on dates c/d during National Council renewal year.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class odp_annee_renouvellement_conseil_national(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'annee en cours est une annee de renouvellement integral du Conseil national"
    reference = "SR 161.11 Art. 2a al. 3"


class odp_nombre_dates_votation_reservees(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de dimanches reserves pour les votations populaires federales"
    reference = "SR 161.11 Art. 2a al. 1"

    def formula(person, period, parameters):
        annee_renouvellement = person('odp_annee_renouvellement_conseil_national', period)
        return where(annee_renouvellement, 2, 4)


class odp_pas_de_votation_automne_renouvellement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Pas de votation aux dates c et d l'annee du renouvellement du CN"
    reference = "SR 161.11 Art. 2a al. 3"

    def formula(person, period, parameters):
        return person('odp_annee_renouvellement_conseil_national', period)
