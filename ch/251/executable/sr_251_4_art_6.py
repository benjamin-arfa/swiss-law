"""SR 251.4 Art. 6

Generated from: ch/251/de/251.4.md

Berechnung der Bruttoprämieneinnahmen bei Versicherungsgesellschaften:
In Rechnung gestellte Praemien im Erst- und Rueckversicherungsgeschaeft,
einschliesslich Rueckdeckungsanteile, abzueglich Steuern.
Schweizer Anteil basiert auf Praemien von in der Schweiz ansaessigen Personen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class praemien_erstversicherung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "In Rechnung gestellte Praemien im Erstversicherungsgeschaeft"
    reference = "SR 251.4 Art. 6 Abs. 1"


class praemien_rueckversicherung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "In Rechnung gestellte Praemien im Rueckversicherungsgeschaeft"
    reference = "SR 251.4 Art. 6 Abs. 1"


class rueckdeckung_anteile(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "In Rueckdeckung gegebene Anteile"
    reference = "SR 251.4 Art. 6 Abs. 1"


class steuern_abgaben_praemien(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuern und sonstige Abgaben auf den Erstversicherungspraemien"
    reference = "SR 251.4 Art. 6 Abs. 1"


class bruttopaemieneinnahmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bruttopraemieneinnahmen der Versicherungsgesellschaft"
    reference = "SR 251.4 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('praemien_erstversicherung', period)
            + person('praemien_rueckversicherung', period)
            + person('rueckdeckung_anteile', period)
            - person('steuern_abgaben_praemien', period)
        )


class bruttopaemieneinnahmen_schweiz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Auf die Schweiz entfallender Anteil der Bruttopraemieneinnahmen"
    reference = "SR 251.4 Art. 6 Abs. 1"
