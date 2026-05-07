"""SR 651.1 Art. 8 - Principes d'obtention des renseignements

Generated from: ch/651/fr/651.1.md

Principles: only measures authorized under Swiss law; bank information
only if convention provides; no right of foreign authority to attend
Swiss proceedings; costs not reimbursed; attorney-client privilege.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class convention_prevoit_transmission_bancaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La convention applicable prevoit la transmission de renseignements bancaires"
    reference = "SR 651.1 Art. 8 al. 2"


class renseignements_bancaires(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Les renseignements demandes sont detenus par une banque ou etablissement financier"
    reference = "SR 651.1 Art. 8 al. 2"


class avocat_invoque_secret_professionnel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Un avocat refuse de remettre des documents couverts par le secret professionnel"
    reference = "SR 651.1 Art. 8 al. 6"


class transmission_renseignements_bancaires_autorisee(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La transmission de renseignements bancaires est autorisee"
    reference = "SR 651.1 Art. 8 al. 2"

    def formula(self, period, parameters):
        convention = self('convention_prevoit_transmission_bancaire', period)
        bancaires = self('renseignements_bancaires', period)
        return convention * bancaires
