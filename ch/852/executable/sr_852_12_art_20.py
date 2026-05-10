"""SR 852.12 Art. 20

Generated from: ch/852/fr/852.12.md

Art. 20: Data destruction timelines for Travel Admin:
- al. 1: Travel data destroyed at most 90 days after expiry of indicated
  travel duration.
- al. 2: Other data destroyed 2 years after last login.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class travel_admin_est_donnee_voyage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether the data pertains to travel information"
    reference = "SR 852.12 Art. 20 al. 1"


class travel_admin_jours_depuis_fin_voyage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Days since the expiry of the indicated travel duration"
    reference = "SR 852.12 Art. 20 al. 1"


class travel_admin_annees_depuis_derniere_connexion(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Years since the last login"
    reference = "SR 852.12 Art. 20 al. 2"


class travel_admin_donnees_a_detruire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether the Travel Admin data must be destroyed"
    reference = "SR 852.12 Art. 20"

    def formula(person, period, parameters):
        p = parameters(period).sr_852_12
        est_voyage = person('travel_admin_est_donnee_voyage', period)
        jours_fin = person('travel_admin_jours_depuis_fin_voyage', period)
        ans_connexion = person('travel_admin_annees_depuis_derniere_connexion', period.this_year)

        # al. 1: travel data - 90 days after travel expiry
        destruction_voyage = est_voyage * (jours_fin >= p.delai_destruction_voyage_jours)

        # al. 2: other data - 2 years after last login
        destruction_autres = (1 - est_voyage) * (ans_connexion >= p.delai_destruction_autres_annees)

        return (destruction_voyage + destruction_autres) > 0
