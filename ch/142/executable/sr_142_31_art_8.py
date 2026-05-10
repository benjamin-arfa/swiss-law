"""SR 142.31 Art. 8 - Obligation de collaborer (Duty to Cooperate)

Generated from: ch/142/fr/142.31.md

Asylum seeker's duty to cooperate:
- Must declare identity, submit travel/identity documents, explain reasons
- Must provide evidence without delay
- Must submit to biometric data collection and medical examinations
- Must hand over electronic data carriers if identity cannot be established otherwise

Consequences of non-cooperation (Art. 8 al. 3bis):
- Absent > 20 days without valid reason: deemed abandonment, case closed
- Absent from federal centre > 5 days without valid reason: deemed abandonment
- New application only possible after 3 years (refugee convention reserved)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lasi_jours_absence_sans_motif(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Nombre de jours d'absence sans motif valable"
    reference = "SR 142.31 Art. 8 al. 3bis"


class lasi_sejourne_dans_centre_federal(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le requerant sejourne dans un centre de la Confederation"
    reference = "SR 142.31 Art. 8 al. 3bis"


class lasi_renonce_poursuite_procedure(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le requerant est repute avoir renonce a la poursuite de la procedure"
    reference = "SR 142.31 Art. 8 al. 3bis"

    def formula(person, period, parameters):
        jours = person('lasi_jours_absence_sans_motif', period)
        en_centre = person('lasi_sejourne_dans_centre_federal', period)

        # > 20 jours hors centre, ou > 5 jours en centre
        abandon_general = jours > 20
        abandon_centre = en_centre * (jours > 5)

        return (abandon_general + abandon_centre) > 0


class lasi_delai_nouvelle_demande_annees(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai minimum avant de pouvoir deposer une nouvelle demande d'asile (3 ans)"
    reference = "SR 142.31 Art. 8 al. 3bis"

    def formula(person, period, parameters):
        # Si classement sans decision, nouvelle demande seulement apres 3 ans
        return where(person('lasi_renonce_poursuite_procedure', period.first_month), 3, 0)
