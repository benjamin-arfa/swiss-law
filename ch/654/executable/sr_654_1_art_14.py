"""SR 654.1 Art. 14 - Prescription

Generated from: ch/654/fr/654.1.md

Prescription periods for the FTA's right to require the CbC report:
5 years ordinary, 10 years absolute.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class annees_depuis_echeance_declaration(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Nombre d'annees ecoulees depuis la fin de l'annee civile durant laquelle la declaration devait etre fournie"
    reference = "SR 654.1 Art. 14 al. 1"


class prescription_interrompue(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La prescription a ete interrompue par un acte officiel"
    reference = "SR 654.1 Art. 14 al. 2"


class droit_afc_prescrit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le droit de l'AFC de requerir la declaration est prescrit"
    reference = "SR 654.1 Art. 14"

    def formula(self, period, parameters):
        annees = self('annees_depuis_echeance_declaration', period)
        interrompue = self('prescription_interrompue', period)

        # al. 1: ordinary prescription 5 years (but restarts on interruption)
        delai_ordinaire = 5
        # al. 3: absolute prescription 10 years
        delai_absolu = 10

        prescription_ordinaire = not_(interrompue) * (annees >= delai_ordinaire)
        prescription_absolue = annees >= delai_absolu

        return prescription_ordinaire + prescription_absolue > 0
