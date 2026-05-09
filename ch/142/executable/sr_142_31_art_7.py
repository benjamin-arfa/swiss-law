"""SR 142.31 Art. 7 - Preuve de la qualite de refugie (Proof of Refugee Status)

Generated from: ch/142/fr/142.31.md

Burden and standard of proof for refugee status:
- Applicant must prove or at least render plausible their refugee status
- Status is plausible when the authority considers it highly probable
- NOT plausible when allegations are:
  - Insufficiently substantiated on essential points
  - Contradictory
  - Not consistent with facts
  - Based on false or falsified evidence
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lasi_allegations_suffisamment_fondees(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les allegations sont suffisamment fondees sur les points essentiels"
    reference = "SR 142.31 Art. 7 al. 3"


class lasi_allegations_coherentes(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les allegations ne sont pas contradictoires"
    reference = "SR 142.31 Art. 7 al. 3"


class lasi_allegations_conformes_faits(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les allegations correspondent aux faits"
    reference = "SR 142.31 Art. 7 al. 3"


class lasi_preuves_authentiques(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les moyens de preuve ne sont pas faux ou falsifies"
    reference = "SR 142.31 Art. 7 al. 3"


class lasi_qualite_refugie_vraisemblable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La qualite de refugie est rendue vraisemblable"
    reference = "SR 142.31 Art. 7"

    def formula(person, period, parameters):
        fondees = person('lasi_allegations_suffisamment_fondees', period)
        coherentes = person('lasi_allegations_coherentes', period)
        conformes = person('lasi_allegations_conformes_faits', period)
        authentiques = person('lasi_preuves_authentiques', period)

        # Toutes les conditions doivent etre remplies pour que ce soit vraisemblable
        return fondees * coherentes * conformes * authentiques
