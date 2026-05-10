"""SR 312.2 Art. 5

Generated from: ch/312/fr/312.2.md

Content of witness protection program: safe housing, workplace/domicile change,
auxiliary instruments, data blocking, provisional identity, financial support.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ltem_logement_lieu_sur(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Logement dans un lieu sur prevu par le programme"
    reference = "SR 312.2 Art. 5 let. a"


class ltem_changement_lieu_travail_domicile(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Changement du lieu de travail et du domicile"
    reference = "SR 312.2 Art. 5 let. b"


class ltem_blocage_communication_donnees(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Blocage de la communication de donnees concernant la personne"
    reference = "SR 312.2 Art. 5 let. d"


class ltem_nouvelle_identite_provisoire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Nouvelle identite provisoire procuree pour la duree de la protection"
    reference = "SR 312.2 Art. 5 let. e"


class ltem_soutien_financier(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Soutien financier dans le cadre du programme"
    reference = "SR 312.2 Art. 5 let. f"
