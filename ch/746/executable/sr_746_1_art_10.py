"""SR 746.1 Art. 10

Generated from: ch/746/de/746.1.md

Enteignungsrecht der Rohrleitungsunternehmung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class hat_enteignungsrecht_rohrleitung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmung steht das Enteignungsrecht zu (fuer Plangenehmigung)"
    reference = "SR 746.1 Art. 10"

    def formula(person, period, parameters):
        # Art. 10: Der Unternehmung, die um eine Plangenehmigung ersucht,
        # steht das Enteignungsrecht zu.
        return person('benoetigt_plangenehmigung_rohrleitung', period)
