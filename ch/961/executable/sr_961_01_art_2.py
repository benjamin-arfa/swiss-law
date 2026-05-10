"""SR 961.01 Art. 2 — Champ d'application / Geltungsbereich

Generated from: ch/961/fr/961.01.md

LSA — Insurance Supervision Act scope and exemptions:
- Subject to supervision: Swiss insurers, foreign insurers active in CH,
  intermediaries, insurance groups/conglomerates, ad-hoc insurance entities
- Exempt: foreign reinsurers only, federally supervised institutions,
  state-backed export risk insurers, dependent intermediaries,
  qualifying cooperatives (Art. 2 al. 2 let. d — 6 cumulative conditions),
  guarantee associations/federations, minor complementary insurance intermediaries
- Cooperative exemption requires: Swiss seat, linked to non-insurance association,
  annual gross premiums never exceeded 3M CHF since 1993, Swiss-only activity,
  members-only insurance, member voting rights on premiums/benefits
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class est_entreprise_assurance_siege_suisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Entreprise d'assurance ayant son siège en Suisse"
    reference = "SR 961.01 Art. 2 al. 1 let. a"


class est_entreprise_assurance_etrangere_active_ch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Entreprise d'assurance étrangère active en Suisse ou à partir de la Suisse"
    reference = "SR 961.01 Art. 2 al. 1 let. b"


class est_intermediaire_assurance(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Intermédiaire d'assurance"
    reference = "SR 961.01 Art. 2 al. 1 let. c"


class est_cooperative_assurance_exemptee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Société coopérative d'assurance exemptée de la surveillance (Art. 2 al. 2 let. d)"
    reference = "SR 961.01 Art. 2 al. 2 let. d"

    def formula(person, period, parameters):
        siege_suisse = person('a_siege_en_suisse', period)
        liee_association = person('est_liee_association_non_assurance', period)
        primes_max = person('volume_primes_brutes_annuel', period) <= parameters(period).sr_961_01.seuil_primes_cooperative_exemptee
        activite_suisse_seule = person('activite_limitee_suisse', period)
        assure_membres_seuls = person('assure_uniquement_membres', period)
        membres_droit_vote = person('membres_decident_prestations_primes', period)
        return (
            siege_suisse * liee_association * primes_max *
            activite_suisse_seule * assure_membres_seuls * membres_droit_vote
        )


class a_siege_en_suisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "A son siège en Suisse"
    reference = "SR 961.01 Art. 2 al. 2 let. d ch. 1"


class est_liee_association_non_assurance(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Étroitement liée à une association dont le but principal n'est pas l'assurance"
    reference = "SR 961.01 Art. 2 al. 2 let. d ch. 2"


class volume_primes_brutes_annuel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Volume annuel de primes brutes en francs"
    reference = "SR 961.01 Art. 2 al. 2 let. d ch. 3"


class activite_limitee_suisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Activité limitée au territoire de la Suisse"
    reference = "SR 961.01 Art. 2 al. 2 let. d ch. 4"


class assure_uniquement_membres(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Assure uniquement les membres de l'association liée"
    reference = "SR 961.01 Art. 2 al. 2 let. d ch. 5"


class membres_decident_prestations_primes(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les assurés/membres peuvent décider eux-mêmes des prestations et primes"
    reference = "SR 961.01 Art. 2 al. 2 let. d ch. 6"


class soumis_surveillance_lsa(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Soumis à la surveillance au sens de la LSA"
    reference = "SR 961.01 Art. 2"

    def formula(person, period, parameters):
        soumis = (
            person('est_entreprise_assurance_siege_suisse', period) +
            person('est_entreprise_assurance_etrangere_active_ch', period) +
            person('est_intermediaire_assurance', period)
        )
        exempt = person('est_cooperative_assurance_exemptee', period)
        return soumis * (1 - exempt)
