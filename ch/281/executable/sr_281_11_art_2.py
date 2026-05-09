"""SR 281.11 Art. 2 — Berichterstattung

Oberaufsicht über Schuldbetreibung und Konkurs (OAV-SchKG).
Generated from: ch/de/281/281.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_obere_kantonale_aufsichtsbehoerde_schkg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine obere oder einzige kantonale Aufsichtsbehörde im Bereich SchKG"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_2"


class berichterstattungspflicht_schkg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterliegt der jährlichen Berichterstattungspflicht an die Dienststelle Oberaufsicht SchKG (SR 281.11 Art. 2 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_2"

    def formula(person, period, parameters):
        # Art. 2 Abs. 1: Die oberen oder einzigen kantonalen Aufsichtsbehörden
        # berichten der Dienststelle Oberaufsicht SchKG jährlich.
        return person('ist_obere_kantonale_aufsichtsbehoerde_schkg', period)


class bericht_inspektionen_durchgefuehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat über durchgeführte Inspektionen bei Betreibungs- und Konkursämtern berichtet (SR 281.11 Art. 2 Abs. 1 lit. a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_2"


class bericht_taetigkeit_aufsichtsbehoerden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat über Tätigkeit der Aufsichtsbehörden samt statistischer Übersicht berichtet (SR 281.11 Art. 2 Abs. 1 lit. b)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_2"


class bericht_disziplinarstrafen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat über Aussprechung von Disziplinarstrafen berichtet (SR 281.11 Art. 2 Abs. 1 lit. c)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_2"


class berichterstattung_vollstaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berichterstattung nach SR 281.11 Art. 2 ist vollständig (alle Pflichtangaben enthalten)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_2"

    def formula(person, period, parameters):
        pflicht = person('berichterstattungspflicht_schkg', period)
        inspektionen = person('bericht_inspektionen_durchgefuehrt', period)
        taetigkeit = person('bericht_taetigkeit_aufsichtsbehoerden', period)
        disziplinar = person('bericht_disziplinarstrafen', period)
        return pflicht * inspektionen * taetigkeit * disziplinar
