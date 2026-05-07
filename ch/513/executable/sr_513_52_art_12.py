"""SR 513.52 Art. 12

Generated from: ch/513/de/513.52.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)
Organisation = build_entity(key='organisation', plural='organisations', label='An organisation')


class bund_traegt_rekrutierungskosten(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Bund traegt die Kosten fuer Rekrutierung der RKD-Angehoerigen (Art. 12 Abs. 1 lit. a SR 513.52)"
    reference = "SR 513.52 Art. 12"

    def formula(organisation, period, parameters):
        return True


class bund_traegt_aufgabenerfuellungskosten(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Bund traegt Kosten fuer Aufgabenerfuellung und Ausbildungsinfrastruktur (Art. 12 Abs. 1 lit. b SR 513.52)"
    reference = "SR 513.52 Art. 12"

    def formula(organisation, period, parameters):
        return True


class bund_traegt_personalbewirtschaftungskosten(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Bund traegt Kosten fuer Personalbewirtschaftung (Art. 12 Abs. 1 lit. c SR 513.52)"
    reference = "SR 513.52 Art. 12"

    def formula(organisation, period, parameters):
        return True
