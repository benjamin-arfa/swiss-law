"""SR 672.201 Art. 1 — Geltungsbereich

Verordnung über die Anrechnung ausländischer Quellensteuern.
Art. 1: Diese Verordnung gilt für Erträge aus Vertragsstaaten (Dividenden,
Zinsen, Lizenzgebühren, Dienstleistungserträge, Renten), die einer begrenzten
Steuer unterliegen gemäss DBA.

Generated from: ch/672/de/672.201.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_switzerland.entities import Person


class ertrag_aus_vertragsstaat(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Erträge aus Vertragsstaaten, die einer begrenzten Steuer unterliegen (SR 672.201 Art. 1 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_1"
    default_value = 0


class dividenden_aus_vertragsstaat(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Dividenden aus einem Vertragsstaat (SR 672.201 Art. 1 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_1"
    default_value = 0


class zinsen_aus_vertragsstaat(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zinsen aus einem Vertragsstaat (SR 672.201 Art. 1 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_1"
    default_value = 0


class lizenzgebuehren_aus_vertragsstaat(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Lizenzgebühren aus einem Vertragsstaat (SR 672.201 Art. 1 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_1"
    default_value = 0


class dienstleistungsertraege_aus_vertragsstaat(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Dienstleistungserträge aus einem Vertragsstaat (SR 672.201 Art. 1 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_1"
    default_value = 0


class renten_aus_vertragsstaat(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Renten aus einem Vertragsstaat (SR 672.201 Art. 1 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_1"
    default_value = 0


class ertrag_unterliegt_begrenzter_steuer_vertragsstaat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ertrag unterliegt tatsächlich einer begrenzten Steuer im Vertragsstaat gemäss DBA (SR 672.201 Art. 1 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 2: Erträge gelten als begrenzt besteuert, wenn sie
        # gemäss internem Recht und DBA tatsächlich einer begrenzten Steuer unterliegen.
        total = (
            person('dividenden_aus_vertragsstaat', period) +
            person('zinsen_aus_vertragsstaat', period) +
            person('lizenzgebuehren_aus_vertragsstaat', period) +
            person('dienstleistungsertraege_aus_vertragsstaat', period) +
            person('renten_aus_vertragsstaat', period)
        )
        return total > 0
