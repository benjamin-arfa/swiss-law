"""SR 861 Art. 3

Generated from: ch/de/861.md

Conditions for granting financial aid: long-term financing (min. 6 years),
cantonal quality requirements, conditions for family day-care and
innovation projects.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finanzierung_langfristig_gesichert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Finanzierung langfristig (mindestens 6 Jahre) gesichert erscheint"
    reference = "SR 861 Art. 3 Abs. 1 Bst. b"


class finanzierung_mindestdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestdauer der gesicherten Finanzierung in Jahren"
    reference = "SR 861 Art. 3 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return 6


class kantonale_qualitaetsanforderungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die kantonalen Qualitaetsanforderungen erfuellt sind"
    reference = "SR 861 Art. 3 Abs. 1 Bst. c"


class voraussetzungen_kindertagesstaette_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Voraussetzungen fuer Finanzhilfen an Kindertagesstaetten erfuellt sind"
    reference = "SR 861 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('finanzierung_langfristig_gesichert', period)
            * person('kantonale_qualitaetsanforderungen_erfuellt', period)
        )


class tagesfamilien_koordination_massnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Finanzhilfe fuer Koordination und Professionalisierung oder Ausbildungsfoerderung der Tagesfamilien verwendet wird"
    reference = "SR 861 Art. 3 Abs. 2"


class innovationsprojekt_modellcharakter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Projekt Modellcharakter fuer die Weiterentwicklung der familienergaenzenden Betreuung hat"
    reference = "SR 861 Art. 3 Abs. 3 Bst. a"


class innovationsprojekt_kanton_gemeinde_unterstuetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Innovationsprojekt von Kantonen oder Gemeinden finanziell unterstuetzt wird"
    reference = "SR 861 Art. 3 Abs. 3 Bst. b"


class innovationsprojekt_bestehende_unterstuetzung_beibehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Kantone/Gemeinden die familienergaenzende Betreuung mindestens im bisherigen Umfang unterstuetzen"
    reference = "SR 861 Art. 3 Abs. 3 Bst. c"


class voraussetzungen_innovationsprojekt_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Voraussetzungen fuer ein Innovationsprojekt erfuellt sind"
    reference = "SR 861 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        return (
            person('innovationsprojekt_modellcharakter', period)
            * person('innovationsprojekt_kanton_gemeinde_unterstuetzt', period)
            * person('innovationsprojekt_bestehende_unterstuetzung_beibehalten', period)
        )


class dritte_angemessen_finanziell_beteiligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Kantone, Gebietskoerperschaften, Arbeitgeber oder andere Dritte sich angemessen finanziell beteiligen"
    reference = "SR 861 Art. 3 Abs. 4"
