"""SR 614.0 Art. 5

Generated from: ch/614/de/614.0.md

Art. 5: Kriterien der Finanzkontrolle - Die EFK übt die Finanzaufsicht nach
den Kriterien der Ordnungsmässigkeit, der Rechtmässigkeit und der
Wirtschaftlichkeit aus. Wirtschaftlichkeitsprüfungen umfassen Sparsamkeit,
Kosten-Nutzen-Verhältnis und Wirksamkeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class efk_prueft_ordnungsmaessigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EFK prüft die Ordnungsmässigkeit (Art. 5 Abs. 1)"
    reference = "SR 614.0 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_prueft_rechtmaessigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EFK prüft die Rechtmässigkeit (Art. 5 Abs. 1)"
    reference = "SR 614.0 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_prueft_wirtschaftlichkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EFK prüft die Wirtschaftlichkeit (Art. 5 Abs. 1)"
    reference = "SR 614.0 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class wirtschaftlichkeitspruefung_sparsamkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wirtschaftlichkeitsprüfung: Mittel werden sparsam eingesetzt (Art. 5 Abs. 2 lit. a)"
    reference = "SR 614.0 Art. 5 Abs. 2 lit. a"


class wirtschaftlichkeitspruefung_kosten_nutzen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Wirtschaftlichkeitsprüfung: Kosten und Nutzen stehen in einem günstigen "
        "Verhältnis (Art. 5 Abs. 2 lit. b)"
    )
    reference = "SR 614.0 Art. 5 Abs. 2 lit. b"


class wirtschaftlichkeitspruefung_wirksamkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Wirtschaftlichkeitsprüfung: Finanzielle Aufwendungen haben die "
        "erwartete Wirkung (Art. 5 Abs. 2 lit. c)"
    )
    reference = "SR 614.0 Art. 5 Abs. 2 lit. c"


class wirtschaftlichkeitspruefung_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wirtschaftlichkeitsprüfung nach allen drei Kriterien bestanden (Art. 5 Abs. 2)"
    reference = "SR 614.0 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        sparsamkeit = person('wirtschaftlichkeitspruefung_sparsamkeit', period)
        kosten_nutzen = person('wirtschaftlichkeitspruefung_kosten_nutzen', period)
        wirksamkeit = person('wirtschaftlichkeitspruefung_wirksamkeit', period)
        return sparsamkeit * kosten_nutzen * wirksamkeit
