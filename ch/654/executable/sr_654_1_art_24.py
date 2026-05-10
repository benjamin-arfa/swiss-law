"""SR 654.1 Art. 24 - Demande d'une entite declarante (suspension)

Generated from: ch/654/de/654.1.md

A reporting entity may request the EFD to suspend the automatic exchange
with a partner state if it credibly demonstrates a violation of
confidentiality or use restrictions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class demande_suspension_echange_deposee(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite declarante a depose une demande de suspension de l'echange avec un Etat partenaire"
    reference = "SR 654.1 Art. 24 al. 1"


class violation_confidentialite_rendue_vraisemblable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite rend vraisemblable que l'Etat partenaire a viole les obligations de confidentialite ou d'utilisation"
    reference = "SR 654.1 Art. 24 al. 1"


class demande_suspension_fondee(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le DFF considere la demande de suspension comme fondee"
    reference = "SR 654.1 Art. 24 al. 2"

    def formula(self, period, parameters):
        deposee = self('demande_suspension_echange_deposee', period)
        vraisemblable = self('violation_confidentialite_rendue_vraisemblable', period)
        return deposee * vraisemblable
