"""SR 961.015.2 Art. 1-7 — Faillite des entreprises d'assurance

Generated from: ch/961/fr/961.015.2.md

OFA-FINMA — Insurance company bankruptcy ordinance:
- Art. 1: Implements LSA Art. 53-59 bankruptcy procedure
- Art. 3: Universality — covers all realizable assets in CH and abroad;
  all Swiss and foreign creditors participate equally
- Art. 4: Publications in FOSC and FINMA website; FOSC is authoritative for deadlines
- Art. 5: File inspection — must show direct pecuniary interest;
  may only use obtained info to protect own direct pecuniary interests
- Art. 7: FINMA appoints bankruptcy liquidator by decision
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class est_en_faillite_assurance(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Entreprise d'assurance en procédure de faillite"
    reference = "SR 961.015.2 Art. 1"


class a_interet_pecuniaire_direct(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Rend vraisemblable un intérêt pécuniaire direct dans la faillite"
    reference = "SR 961.015.2 Art. 5 al. 1"


class droit_consultation_pieces_faillite(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Droit de consulter les pièces de la faillite"
    reference = "SR 961.015.2 Art. 5 al. 1"

    def formula(person, period, parameters):
        return person('a_interet_pecuniaire_direct', period)


class faillite_universalite_applicable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le principe d'universalité s'applique (tous biens CH + étranger)"
    reference = "SR 961.015.2 Art. 3 al. 1"

    def formula(person, period, parameters):
        return person('est_en_faillite_assurance', period)
