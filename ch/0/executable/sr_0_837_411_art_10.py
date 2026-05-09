"""SR 0.837.411 Art. 10 - Disqualification from benefits

Art. 10: Claimant may be disqualified for an appropriate period if:
- Par. 1: Refuses suitable employment (with definition of unsuitable work)
- Par. 2: Lost job due to industrial dispute, own fault, voluntary quit,
  fraud, non-compliance with employment office instructions
- Par. 3: Received compensation equal to lost wages from employer

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class refuse_emploi_convenable(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person refused suitable employment (Art. 10 par. 1)"
    default_value = False


class emploi_offert_sans_logement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Offered job requires moving to area without suitable housing (Art. 10 par. 1 let. a)"
    default_value = False


class emploi_offert_salaire_inferieur(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Offered job has inferior wages or conditions (Art. 10 par. 1 let. b)"
    default_value = False


class emploi_vacant_conflit_professionnel(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Offered job is vacant due to industrial dispute (Art. 10 par. 1 let. c)"
    default_value = False


class perte_emploi_conflit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Lost job directly due to industrial dispute (Art. 10 par. 2 let. a)"
    default_value = False


class perte_emploi_faute_propre(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Lost job through own fault or voluntary quit without legitimate reason (Art. 10 par. 2 let. b)"
    default_value = False


class tentative_fraude_chomage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Attempted to obtain benefits fraudulently (Art. 10 par. 2 let. c)"
    default_value = False


class non_conformite_instructions_placement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Failed to follow employment office instructions (Art. 10 par. 2 let. d)"
    default_value = False


class compensation_employeur_recue(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Received compensation from employer substantially equal to lost wages (Art. 10 par. 3)"
    default_value = False


class disqualifie_indemnite_chomage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is disqualified from unemployment benefits (Art. 10)"

    def formula(person, period, parameters):
        # Refusal of suitable employment (par. 1)
        refus = person("refuse_emploi_convenable", period)

        # Check if job was actually unsuitable (exceptions from par. 1)
        emploi_non_convenable = (
            person("emploi_offert_sans_logement", period)
            + person("emploi_offert_salaire_inferieur", period)
            + person("emploi_vacant_conflit_professionnel", period)
        )
        refus_injustifie = refus * not_(emploi_non_convenable)

        # Disqualification grounds (par. 2)
        conflit = person("perte_emploi_conflit", period)
        faute = person("perte_emploi_faute_propre", period)
        fraude = person("tentative_fraude_chomage", period)
        non_conformite = person("non_conformite_instructions_placement", period)

        # Employer compensation (par. 3)
        compensation = person("compensation_employeur_recue", period)

        return (
            refus_injustifie
            + conflit
            + faute
            + fraude
            + non_conformite
            + compensation
        )
