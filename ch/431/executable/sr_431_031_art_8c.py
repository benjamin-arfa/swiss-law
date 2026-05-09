"""SR 431.031 Art. 8c

Generated from: ch/431/de/431.031.md

Kosten fuer LEI - jaehrliche Berechnung in Abhaengigkeit des GLEIF-Beitrags,
Anzahl Gesuche und Betriebskosten. Kostendeckungsprinzip.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class gleif_jahresbeitrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Vom BFS zu bezahlender Jahresbeitrag an die GLEIF"
    reference = "SR 431.031 Art. 8c Abs. 1"


class anzahl_lei_gesuche(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl LEI-Zuweisungs- und Erneuerungsgesuche"
    reference = "SR 431.031 Art. 8c Abs. 1"


class lei_system_betriebskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Betriebskosten des LEI-Systems des BFS"
    reference = "SR 431.031 Art. 8c Abs. 1"


class lei_einnahmen_total(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total der jaehrlichen Einnahmen fuer LEI-Zuweisung und -Erneuerung (ohne MWST)"
    reference = "SR 431.031 Art. 8c Abs. 2"

    def formula(person, period, parameters):
        return (
            person('gleif_jahresbeitrag', period) +
            person('lei_system_betriebskosten', period)
        )


class lei_kosten_pro_gesuch(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten pro LEI-Gesuch (Kostendeckungsprinzip)"
    reference = "SR 431.031 Art. 8c Abs. 1-2"

    def formula(person, period, parameters):
        total = person('lei_einnahmen_total', period)
        anzahl = person('anzahl_lei_gesuche', period)
        return where(anzahl > 0, total / anzahl, 0)
