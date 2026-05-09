"""SR 432.219 Art. 4

Generated from: ch/432/de/432.219.md

Gebuehrenzuschlag - bis zu 50% Zuschlag bei dringlichen Leistungen oder
Leistungen ausserhalb der normalen Arbeitszeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class dienstleistung_dringlich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung wird auf Ersuchen hin dringlich erbracht"
    reference = "SR 432.219 Art. 4"


class dienstleistung_ausserhalb_arbeitszeit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung wird ausserhalb der normalen Arbeitszeit erbracht"
    reference = "SR 432.219 Art. 4"


class gebuehr_grundbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Grundbetrag der Gebuehr fuer die Dienstleistung"
    reference = "SR 432.219 Art. 4"


class max_zuschlag_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Maximaler Gebuehrenzuschlag in Prozent"
    reference = "SR 432.219 Art. 4"
    default_value = 50.0


class gebuehr_mit_zuschlag(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Gebuehr einschliesslich maximalem Zuschlag bei Dringlichkeit oder Sondereinsatz"
    reference = "SR 432.219 Art. 4"

    def formula(person, period, parameters):
        grundbetrag = person('gebuehr_grundbetrag', period)
        zuschlag_berechtigt = (
            person('dienstleistung_dringlich', period) +
            person('dienstleistung_ausserhalb_arbeitszeit', period)
        ) > 0
        max_zuschlag = person('max_zuschlag_prozent', period) / 100.0
        return where(
            zuschlag_berechtigt,
            grundbetrag * (1 + max_zuschlag),
            grundbetrag
        )
