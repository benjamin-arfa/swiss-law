"""SR 961.011 Art. 1f-1h — Libération de la surveillance et intermédiaires

Generated from: ch/961/fr/961.011.md

OS — Exemption from supervision and intermediary rules:
- Art. 1f: Insurer exempt from supervision if: Swiss seat, SA or cooperative,
  subject to ordinary audit, branches B3-B9/B14-B18, max 5000 policies,
  max 5M CHF total premiums, informs policyholders of non-supervision
- Art. 1g: 1-year grace period after exceeding Art. 1f limits;
  must apply for FINMA authorization 6 months before deadline;
  FINMA decides within 3 months; if rejected, wind down in 6 months
- Art. 1h: Intermediary exempt if annual premium <= 600 CHF (excl. tax),
  insurance is subordinate to product/service, and intermediation is accessory;
  does NOT apply to supplementary health insurance
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nombre_polices_distribuees(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de polices distribuées"
    reference = "SR 961.011 Art. 1f let. e"


class volume_total_primes_distribuees(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Volume total des primes distribuées (CHF)"
    reference = "SR 961.011 Art. 1f let. e"


class est_sa_ou_cooperative(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Est constituée en SA ou en coopérative"
    reference = "SR 961.011 Art. 1f let. b"


class soumis_controle_ordinaire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Soumis au contrôle ordinaire (CO Art. 727)"
    reference = "SR 961.011 Art. 1f let. c"


class branches_b3_b9_b14_b18_uniquement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produits uniquement dans les branches B3 à B9 et B14 à B18"
    reference = "SR 961.011 Art. 1f let. d"


class informe_preneurs_non_surveillance(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "S'engage à informer les preneurs de la non-surveillance FINMA"
    reference = "SR 961.011 Art. 1f let. f"


class liberee_surveillance_os(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Libérée de la surveillance au sens de l'OS Art. 1f"
    reference = "SR 961.011 Art. 1f"

    def formula(person, period, parameters):
        p = parameters(period).sr_961_011
        siege = person('a_siege_en_suisse', period)
        forme = person('est_sa_ou_cooperative', period)
        audit = person('soumis_controle_ordinaire', period)
        branches = person('branches_b3_b9_b14_b18_uniquement', period)
        polices = person('nombre_polices_distribuees', period) <= p.max_polices_exemption
        primes = person('volume_total_primes_distribuees', period) <= p.max_primes_exemption
        info = person('informe_preneurs_non_surveillance', period)
        return siege * forme * audit * branches * polices * primes * info


class depasse_limites_exemption(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "A dépassé les limites de l'exemption (polices ou primes)"
    reference = "SR 961.011 Art. 1g al. 1"

    def formula(person, period, parameters):
        p = parameters(period).sr_961_011
        polices = person('nombre_polices_distribuees', period) > p.max_polices_exemption
        primes = person('volume_total_primes_distribuees', period) > p.max_primes_exemption
        return polices + primes


class prime_annuelle_intermediaire(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prime annuelle pour l'assurance procurée par l'intermédiaire (CHF, hors impôts)"
    reference = "SR 961.011 Art. 1h al. 1 let. a"


class assurance_subordonnee_produit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'assurance est subordonnée à un produit ou service"
    reference = "SR 961.011 Art. 1h al. 1 let. b"


class intermediation_activite_accessoire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'intermédiation constitue une activité accessoire"
    reference = "SR 961.011 Art. 1h al. 1 let. c"


class est_assurance_complementaire_maladie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'assurance est complémentaire à l'assurance-maladie sociale"
    reference = "SR 961.011 Art. 1h al. 2"


class intermediaire_exempt_surveillance(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Intermédiaire exempté de la surveillance"
    reference = "SR 961.011 Art. 1h"

    def formula(person, period, parameters):
        p = parameters(period).sr_961_011
        prime_ok = person('prime_annuelle_intermediaire', period) <= p.seuil_prime_intermediaire
        subordonne = person('assurance_subordonnee_produit', period)
        accessoire = person('intermediation_activite_accessoire', period)
        pas_maladie = 1 - person('est_assurance_complementaire_maladie', period)
        return prime_ok * subordonne * accessoire * pas_maladie
