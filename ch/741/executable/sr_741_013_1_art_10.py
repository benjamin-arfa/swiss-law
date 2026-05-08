"""SR 741.013.1 Art. 10

Generated from: ch/741/de/741.013.1.md

VSKV-ASTRA: Rotlichtueberwachungssysteme
Red light monitoring systems serve primarily to detect violations of
the stop requirement by traffic signals. They may be combined with
speed measurement systems.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class rotlichtueberwachung_widerhandlung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Widerhandlung gegen das Haltegebot durch Lichtsignale festgestellt (Art. 10 Abs. 1 VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 10"

    def formula(person, period, parameters):
        return person("rotlicht_ueberfahren", period)


class rotlicht_mit_geschwindigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Rotlichtueberwachung kombiniert mit Geschwindigkeitsmessung (Art. 10 Abs. 2 VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 10"

    def formula(person, period, parameters):
        return (
            person("rotlicht_ueberfahren", period) *
            person("geschwindigkeit_gemessen", period)
        )
