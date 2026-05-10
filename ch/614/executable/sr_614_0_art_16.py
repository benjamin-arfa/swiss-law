"""SR 614.0 Art. 16

Generated from: ch/614/de/614.0.md

Art. 16: Umfang der Bundesaufsicht - EFK führt bei Kantonen, die
Bundesleistungen erhalten, Prüfungen durch, soweit gesetzlich vorgesehen.
Zusammenarbeit mit kantonalen Finanzkontrollorganen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kanton_erhaelt_bundesleistungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kanton erhält finanzielle Zuwendungen vom Bund (Beiträge, Darlehen, Vorschüsse)"
    reference = "SR 614.0 Art. 16 Abs. 1"


class bundesgesetz_sieht_kontrolle_vor(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ein Bundesgesetz oder Bundesbeschluss sieht die Kontrolle vor"
    reference = "SR 614.0 Art. 16 Abs. 1"


class efk_pruefung_bei_kanton_gesetzlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK führt bei Kanton Prüfungen über Verwendung der Bundesleistungen "
        "durch, soweit gesetzlich vorgesehen (Art. 16 Abs. 1)"
    )
    reference = "SR 614.0 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        erhaelt_leistungen = person('kanton_erhaelt_bundesleistungen', period)
        gesetzlich = person('bundesgesetz_sieht_kontrolle_vor', period)
        return erhaelt_leistungen * gesetzlich


class einvernehmen_kantonsregierung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einvernehmen mit der Kantonsregierung liegt vor"
    reference = "SR 614.0 Art. 16 Abs. 2"


class efk_pruefung_bei_kanton_einvernehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK kann im Einvernehmen mit Kantonsregierung Verwendung von "
        "Bundesleistungen überprüfen (Art. 16 Abs. 2)"
    )
    reference = "SR 614.0 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        # Art. 16 Abs. 2: In den übrigen Fällen (ohne gesetzliche Grundlage)
        erhaelt_leistungen = person('kanton_erhaelt_bundesleistungen', period)
        gesetzlich = person('bundesgesetz_sieht_kontrolle_vor', period)
        einvernehmen = person('einvernehmen_kantonsregierung', period)
        return erhaelt_leistungen * (1 - gesetzlich) * einvernehmen
