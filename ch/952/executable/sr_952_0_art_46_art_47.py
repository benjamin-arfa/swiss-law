"""SR 952.0 Art. 46-47 - Dispositions penales (Criminal Provisions)

Generated from: ch/952/fr/952.0.md

Criminal provisions:
Art. 46 - Banking offenses:
  - Intentional: up to 3 years imprisonment or monetary penalty for:
    a) Unduly accepting public deposits or savings
    b) Not properly keeping books/records
    c) Not establishing/publishing annual accounts per Art. 6
  - Negligent: fine up to CHF 250,000

Art. 47 - Banking secrecy violation:
  - Intentional: up to 3 years imprisonment or monetary penalty for:
    a) Revealing a secret in capacity as organ/employee/agent/liquidator
    b) Attempting to incite such violation
    c) Revealing or exploiting such secret for personal/third-party benefit
  - With pecuniary advantage (al. 1bis): up to 5 years imprisonment
  - Negligent: fine up to CHF 250,000
  - Remains punishable even after end of position/employment
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lb_type_infraction(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Type d'infraction: 0=aucune, 1=depots_indus, 2=livres, 3=comptes, 4=secret_simple, 5=incitation_secret, 6=exploitation_secret"
    reference = "SR 952.0 Art. 46-47"


class lb_infraction_intentionnelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'infraction a ete commise intentionnellement"
    reference = "SR 952.0 Art. 46-47"


class lb_avantage_pecuniaire_obtenu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Un avantage pecuniaire a ete obtenu (art. 47 al. 1bis)"
    reference = "SR 952.0 Art. 47 al. 1bis"


class lb_peine_maximale_annees(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Peine privative de liberte maximale (en annees)"
    reference = "SR 952.0 Art. 46-47"

    def formula(person, period, parameters):
        type_inf = person('lb_type_infraction', period)
        intentionnelle = person('lb_infraction_intentionnelle', period)
        avantage = person('lb_avantage_pecuniaire_obtenu', period)

        # Infractions bancaires (art. 46): max 3 ans si intentionnel
        est_art46 = (type_inf >= 1) * (type_inf <= 3)
        # Secret bancaire (art. 47): max 3 ans, ou 5 ans si avantage pecuniaire
        est_art47 = (type_inf >= 4) * (type_inf <= 6)

        peine_art46 = where(intentionnelle * est_art46, 3, 0)
        peine_art47_simple = where(intentionnelle * est_art47 * not_(avantage), 3, 0)
        peine_art47_avantage = where(intentionnelle * est_art47 * avantage, 5, 0)

        return peine_art46 + peine_art47_simple + peine_art47_avantage


class lb_amende_maximale_negligence(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Amende maximale en cas de negligence (250'000 CHF)"
    reference = "SR 952.0 Art. 46 al. 2 / Art. 47 al. 2"

    def formula(person, period, parameters):
        type_inf = person('lb_type_infraction', period)
        intentionnelle = person('lb_infraction_intentionnelle', period)

        # Negligence: amende max 250'000 CHF
        est_infraction = type_inf > 0
        return where(est_infraction * not_(intentionnelle), 250000, 0)
