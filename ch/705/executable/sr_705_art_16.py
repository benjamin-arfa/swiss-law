"""SR 705 Art. 16 - Zusammenarbeit mit privaten Fachorganisationen (Federal Level)

Generated from: ch/de/705.md
The Confederation may involve nationwide bicycle organizations for advisory,
resource provision, and public information tasks.
Financial assistance requires 3+ years of statutory bicycle advocacy.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class organisation_gesamtschweizerisch_velo(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist im Bereich Veloverkehr gesamtschweizerisch taetig"
    reference = "SR 705 Art. 16 Abs. 3 lit. a"
    default_value = False


class organisation_ideelle_zwecke_velo_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre, in denen die Organisation statutarisch ideelle Zwecke im Veloverkehr verfolgt"
    reference = "SR 705 Art. 16 Abs. 3 lit. b"
    default_value = 0


class finanzhilfe_berechtigt_velo_organisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation ist berechtigt, Finanzhilfen des Bundes fuer Velowegaufgaben zu erhalten"
    reference = "SR 705 Art. 16 Abs. 3"

    def formula(person, period, parameters):
        gesamt_ch = person('organisation_gesamtschweizerisch_velo', period)
        jahre = person('organisation_ideelle_zwecke_velo_jahre', period)
        return gesamt_ch * (jahre >= 3)
