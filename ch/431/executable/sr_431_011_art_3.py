"""SR 431.011 Art. 3

Generated from: ch/431/de/431.011.md

Begriffe - Definition von Statistikproduzenten und statistischen Arbeiten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_statistikproduzent_bund(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Statistikproduzent des Bundes (Verwaltungseinheit oder teilunterstellte Koerperschaft mit statistischen Arbeiten)"
    reference = "SR 431.011 Art. 3 Abs. 1"


class fuehrt_direkte_erhebungen_durch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fuehrt direkte oder indirekte statistische Erhebungen durch"
    reference = "SR 431.011 Art. 3 Abs. 2 Bst. a"


class fuehrt_synthesestatistiken_durch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Arbeitet Gesamtdarstellungen und Synthesestatistiken aus"
    reference = "SR 431.011 Art. 3 Abs. 2 Bst. b"


class fuehrt_klassifikationen_durch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erstellt oder aktualisiert Klassifikationen, Nomenklaturen und Terminologien"
    reference = "SR 431.011 Art. 3 Abs. 2 Bst. c"


class fuehrt_admin_daten_auswertung_durch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wertet administrative Daten, Register oder Beobachtungsnetze zu statistischen Zwecken aus"
    reference = "SR 431.011 Art. 3 Abs. 2 Bst. d"


class taetigkeit_ist_statistische_arbeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetigkeit gilt als statistische Arbeit im Sinne des Gesetzes"
    reference = "SR 431.011 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('fuehrt_direkte_erhebungen_durch', period) +
            person('fuehrt_synthesestatistiken_durch', period) +
            person('fuehrt_klassifikationen_durch', period) +
            person('fuehrt_admin_daten_auswertung_durch', period)
        ) > 0


class taetigkeit_nur_intern(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Arbeit dient ausschliesslich der internen administrativen Taetigkeit"
    reference = "SR 431.011 Art. 3 Abs. 3"


class resultate_bundesweit_repraesentativ(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Resultate liefern auf Bundesebene repraesentative Informationen"
    reference = "SR 431.011 Art. 3 Abs. 3"


class taetigkeit_gilt_als_statistisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetigkeit gilt als statistische Arbeit (nicht rein intern und repraesentativ)"
    reference = "SR 431.011 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        return (
            person('taetigkeit_ist_statistische_arbeit', period) *
            not_(person('taetigkeit_nur_intern', period) *
                 not_(person('resultate_bundesweit_repraesentativ', period)))
        )
