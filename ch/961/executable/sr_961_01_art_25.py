"""SR 961.01 Art. 25-26 — Rapports / Berichterstattung

Generated from: ch/961/fr/961.01.md

LSA — Reporting obligations:
- Art. 25: Annual management report (incl. annual accounts, annual report, group accounts)
  as of Dec 31 each year; due to FINMA by April 30 of following year
- Art. 25 al. 4: Foreign insurers must present separate Swiss reports
- Art. 26: Legal reserve from profits — FINMA sets minimum amount
- Art. 26 al. 2: Foundation/capital increase costs charged to organization fund
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rapport_gestion_remis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Rapport de gestion remis à la FINMA"
    reference = "SR 961.01 Art. 25 al. 1"


class date_remise_rapport_jour_annee(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jour de l'année de remise du rapport (1-365, 120 = 30 avril)"
    reference = "SR 961.01 Art. 25 al. 3"


class rapport_gestion_dans_delai(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Rapport de gestion remis dans le délai légal (au plus tard le 30 avril)"
    reference = "SR 961.01 Art. 25 al. 3"

    def formula(person, period, parameters):
        jour = person('date_remise_rapport_jour_annee', period)
        delai = parameters(period).sr_961_01.delai_rapport_gestion_jour
        remis = person('rapport_gestion_remis', period)
        return remis * (jour <= delai)


class est_entreprise_assurance_etrangere(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Entreprise d'assurance étrangère active en Suisse"
    reference = "SR 961.01 Art. 25 al. 4"


class rapport_distinct_suisse_requis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Rapport de gestion distinct pour les activités en Suisse requis"
    reference = "SR 961.01 Art. 25 al. 4"

    def formula(person, period, parameters):
        return person('est_entreprise_assurance_etrangere', period)
