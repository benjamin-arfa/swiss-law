"""SR 419.1 Art. 12

Generated from: ch/419/de/419.1.md

Finanzhilfen an Organisationen der Weiterbildung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class organisation_gesamtschweizerisch_taetig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist gesamtschweizerisch taetig"
    reference = "SR 419.1 Art. 12 Abs. 2 Bst. a"


class organisation_nicht_gewinnorientiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist nicht gewinnorientiert"
    reference = "SR 419.1 Art. 12 Abs. 2 Bst. b"


class finanzhilfe_an_weiterbildungsorganisation_berechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigung fuer Finanzhilfe an Weiterbildungsorganisation"
    reference = "SR 419.1 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('organisation_gesamtschweizerisch_taetig', period) *
            person('organisation_nicht_gewinnorientiert', period)
        )
