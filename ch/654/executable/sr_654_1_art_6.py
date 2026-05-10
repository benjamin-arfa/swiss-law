"""SR 654.1 Art. 6 - Obligation d'etablir une declaration pays par pays

Generated from: ch/654/fr/654.1.md

Obligation to prepare a country-by-country report when consolidated
annual turnover exceeds the threshold.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class societe_mere_residente_suisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La societe mere du groupe est residente de Suisse"
    reference = "SR 654.1 Art. 6 al. 1"


class chiffre_affaires_annuel_consolide(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Chiffre d'affaires annuel consolide du groupe (en CHF)"
    reference = "SR 654.1 Art. 6 al. 1"


class seuil_chiffre_affaires_declaration_pays(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Seuil de chiffre d'affaires pour l'obligation de declaration pays par pays (en CHF)"
    reference = "SR 654.1 Art. 6 al. 2"
    default_value = 900_000_000.0  # EUR 750 mio approx. per OECD standard


class obligation_declaration_pays_par_pays(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le groupe est tenu d'etablir une declaration pays par pays"
    reference = "SR 654.1 Art. 6 al. 1"

    def formula(self, period, parameters):
        mere_suisse = self('societe_mere_residente_suisse', period)
        ca = self('chiffre_affaires_annuel_consolide', period)
        seuil = self('seuil_chiffre_affaires_declaration_pays', period)
        return mere_suisse * (ca > seuil)
