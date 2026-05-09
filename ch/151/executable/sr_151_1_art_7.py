"""SR 151.1 Art. 7 - Qualite pour agir des organisations (Standing of Organizations)

Generated from: ch/151/fr/151.1.md

Organizations can bring gender discrimination claims in their own name if:
1. They have existed for at least 2 years
2. Their statutes include promoting gender equality or defending workers' interests
3. The outcome would likely affect a considerable number of employment relationships
4. They give the employer a chance to take a position before initiating proceedings
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class leg_organisation_annees_existence(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre d'annees d'existence de l'organisation"
    reference = "SR 151.1 Art. 7 al. 1"


class leg_organisation_statuts_egalite(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les statuts prevoient la promotion de l'egalite ou la defense des travailleurs"
    reference = "SR 151.1 Art. 7 al. 1"


class leg_affecte_nombre_considerable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'issue du proces affecterait un nombre considerable de rapports de travail"
    reference = "SR 151.1 Art. 7 al. 1"


class leg_employeur_informe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'employeur a eu la possibilite de prendre position"
    reference = "SR 151.1 Art. 7 al. 1"


class leg_organisation_qualite_pour_agir(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'organisation a qualite pour agir selon Art. 7 LEg"
    reference = "SR 151.1 Art. 7"

    def formula(person, period, parameters):
        annees = person('leg_organisation_annees_existence', period)
        statuts = person('leg_organisation_statuts_egalite', period)
        nombre = person('leg_affecte_nombre_considerable', period)
        informe = person('leg_employeur_informe', period)

        # Conditions cumulatives
        duree_suffisante = annees >= 2
        return duree_suffisante * statuts * nombre * informe
