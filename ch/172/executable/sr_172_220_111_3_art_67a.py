"""SR 172.220.111.3 Art. 67a - Reduction des vacances (Vacation Reduction)

Generated from: ch/172/fr/172.220.111.3.md

Vacation is reduced proportionally when absences exceed thresholds:
- Illness/accident/obligatory service: reduced if total > 66 working days per year
  (first 66 days are not counted toward reduction)
- Unpaid leave: reduced if total > 22 working days per year

For calculation: partial and full absence days are summed, divided by working
days in the year. Hourly employees get reduced vacation pay, not reduced days.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class opers_jours_absence_maladie_accident(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de jours ouvres d'absence pour maladie, accident ou service obligatoire"
    reference = "SR 172.220.111.3 Art. 67a al. 1 let. a"


class opers_jours_conge_non_paye(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de jours ouvres de conge non paye"
    reference = "SR 172.220.111.3 Art. 67a al. 1 let. b"


class opers_jours_ouvres_annee(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de jours ouvres dans l'annee (typiquement ~252)"
    reference = "SR 172.220.111.3 Art. 67a al. 3"
    default_value = 252


class opers_vacances_reduction_applicable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Une reduction des vacances est applicable"
    reference = "SR 172.220.111.3 Art. 67a al. 1"

    def formula(person, period, parameters):
        maladie = person('opers_jours_absence_maladie_accident', period)
        non_paye = person('opers_jours_conge_non_paye', period)

        depasse_maladie = maladie > 66
        depasse_non_paye = non_paye > 22

        return (depasse_maladie + depasse_non_paye) > 0


class opers_vacances_jours_apres_reduction(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de jours de vacances apres reduction eventuelle"
    reference = "SR 172.220.111.3 Art. 67a"

    def formula(person, period, parameters):
        vacances_base = person('opers_vacances_jours', period)
        maladie = person('opers_jours_absence_maladie_accident', period)
        non_paye = person('opers_jours_conge_non_paye', period)
        jours_ouvres = person('opers_jours_ouvres_annee', period)

        # Jours comptabilises pour la reduction (apres seuils)
        jours_maladie_comptables = max_(maladie - 66, 0)
        jours_non_paye_comptables = max_(non_paye - 22, 0)
        total_reduction_jours = jours_maladie_comptables + jours_non_paye_comptables

        # Proportion de reduction
        proportion = total_reduction_jours / jours_ouvres

        # Vacances reduites proportionnellement
        reduction = round_(vacances_base * proportion)
        vacances_apres = max_(vacances_base - reduction, 0)

        return vacances_apres
