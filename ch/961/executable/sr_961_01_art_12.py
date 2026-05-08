"""SR 961.01 Art. 12-13 — Restrictions d'exploitation

Generated from: ch/961/fr/961.01.md

LSA — Business restrictions:
- Art. 12: Life insurers may not operate other branches except accident and health
- Art. 13: Motor liability insurers must join Bureau national d'assurance and
  Fonds national de garantie (per LCR Art. 74 and 76)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class pratique_assurance_vie_directe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Pratique l'assurance directe sur la vie"
    reference = "SR 961.01 Art. 12"


class pratique_assurance_accidents(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Pratique l'assurance-accidents"
    reference = "SR 961.01 Art. 12"


class pratique_assurance_maladie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Pratique l'assurance-maladie"
    reference = "SR 961.01 Art. 12"


class pratique_autre_branche_assurance(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Pratique une autre branche d'assurance (hors vie, accidents, maladie)"
    reference = "SR 961.01 Art. 12"


class exploitation_conjointe_licite(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'exploitation conjointe des branches est licite au sens de l'Art. 12"
    reference = "SR 961.01 Art. 12"

    def formula(person, period, parameters):
        vie = person('pratique_assurance_vie_directe', period)
        autre = person('pratique_autre_branche_assurance', period)
        # Life insurers cannot operate other branches (except accident and health)
        return 1 - (vie * autre)


class pratique_rc_vehicules_automobiles(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Pratique l'assurance RC véhicules automobiles"
    reference = "SR 961.01 Art. 13"


class adhesion_bureau_national_requise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Adhésion au Bureau national d'assurance et au Fonds national de garantie requise"
    reference = "SR 961.01 Art. 13"

    def formula(person, period, parameters):
        return person('pratique_rc_vehicules_automobiles', period)
