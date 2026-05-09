"""SR 442.132.3 Art. 16

Generated from: ch/442/de/442.132.3.md

Art. 16: Direktorin oder Direktor - Regelung der Zuständigkeit des
Stiftungsrats für das Arbeitsverhältnis der Direktion, maximaler Lohn
und weitere Vertragsbedingungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_direktor_pro_helvetia(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Direktorin oder Direktor der Stiftung Pro Helvetia"
    reference = "SR 442.132.3 Art. 16"


class stiftungsrat_zustaendig_arbeitsverhaeltnis_direktor(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Der Stiftungsrat ist zuständig für die Begründung, Änderung und "
        "Beendigung des Arbeitsverhältnisses mit der Direktorin oder "
        "dem Direktor (Art. 16 Abs. 1)"
    )
    reference = "SR 442.132.3 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_direktor_pro_helvetia', period)


class direktor_maximaler_lohn_lk33(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Der maximale Lohn der Direktorin oder des Direktors entspricht "
        "dem Höchstbetrag der Lohnklasse 33 nach Anhang 1 (Art. 16 Abs. 2)"
    )
    reference = "SR 442.132.3 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_direktor_pro_helvetia', period)


class direktor_kuendigungsfrist_6_monate(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Die Kündigungsfrist der Direktorin oder des Direktors beträgt "
        "6 Monate (Art. 16 Abs. 3 lit. a)"
    )
    reference = "SR 442.132.3 Art. 16 Abs. 3 lit. a"

    def formula(person, period, parameters):
        return person('ist_direktor_pro_helvetia', period)


class direktor_keine_bonifikationen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Keine Repräsentations-, Pauschalspesen oder Bonifikationen für "
        "die Direktorin oder den Direktor (Art. 16 Abs. 3 lit. b)"
    )
    reference = "SR 442.132.3 Art. 16 Abs. 3 lit. b"

    def formula(person, period, parameters):
        return person('ist_direktor_pro_helvetia', period)


class direktor_kein_pensionskasseneinkauf(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Die Stiftung leistet keine Beiträge an den Einkauf in die "
        "Pensionskasse der Direktorin oder des Direktors (Art. 16 Abs. 3 lit. c)"
    )
    reference = "SR 442.132.3 Art. 16 Abs. 3 lit. c"

    def formula(person, period, parameters):
        return person('ist_direktor_pro_helvetia', period)
