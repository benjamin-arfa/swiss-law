"""SR 511.41 Art. 7 – Wegfall der Rückerstattungspflicht

Generated from: ch/511/de/511.41.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class vorteil_nicht_mehr_nutzbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person kann nachweislich den Vorteil der Ausbildung künftig nicht mehr nutzen"
    reference = "SR 511.41 Art. 7 lit. a"
    default_value = False


class rueckerstattungspflicht_entfaellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rückerstattungspflicht entfällt"
    reference = "SR 511.41 Art. 7"

    def formula(person, period, parameters):
        # lit. a: Vorteil kann nicht mehr genutzt werden
        vorteil_weg = person('vorteil_nicht_mehr_nutzbar', period)
        # lit. b: Zuteilung ohne Einwilligung (Art. 3 Abs. 2)
        ohne_einwilligung = person('freiwillige_nicht_ausreichend', period)

        return vorteil_weg + ohne_einwilligung
