"""SR 231.11 Art. 16a

Generated from: ch/231/de/231.11.md

Gebuehren und Auslagen: Die Gebuehren fuer die Pruefung und Genehmigung
der Tarife richten sich sinngemäss nach den einschlaegigen Bestimmungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tarifpruefung_gebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebuehr fuer die Pruefung und Genehmigung der Tarife der Verwertungsgesellschaften"
    reference = "SR 231.11 Art. 16a Abs. 1"


class auslagen_taggelder(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taggelder und Entschaedigungen als Auslagen der Schiedskommission"
    reference = "SR 231.11 Art. 16a Abs. 2 Bst. a"


class auslagen_beweiserhebung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten fuer Beweiserhebung, wissenschaftliche Untersuchungen und Pruefungen"
    reference = "SR 231.11 Art. 16a Abs. 2 Bst. b"


class auslagen_drittarbeiten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten fuer Arbeiten, die durch Dritte ausgefuehrt werden"
    reference = "SR 231.11 Art. 16a Abs. 2 Bst. c"


class auslagen_uebermittlung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Uebermittlungs- und Kommunikationskosten"
    reference = "SR 231.11 Art. 16a Abs. 2 Bst. d"


class auslagen_gesamt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte Auslagen der Schiedskommission"
    reference = "SR 231.11 Art. 16a Abs. 2"

    def formula(person, period, parameters):
        return (
            person('auslagen_taggelder', period)
            + person('auslagen_beweiserhebung', period)
            + person('auslagen_drittarbeiten', period)
            + person('auslagen_uebermittlung', period)
        )
