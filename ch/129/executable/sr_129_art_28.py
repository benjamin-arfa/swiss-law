"""SR 129 Art. 28 - Personal

Generated from: ch/de/129.md
PIU staff is half federal, half cantonal. Cantons bear salary costs
of their seconded staff. Staff is subject to fedpol's technical/operational
authority and to the seconding authority's disciplinary authority.
Staff may only use information obtained at PIU for PIU tasks.
In force since 1 January 2026.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class piu_anteil_bund_mitarbeitende(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil Bundesmitarbeitende am PIU-Personal"
    reference = "SR 129 Art. 28 Abs. 1"

    def formula(person, period, parameters):
        return 0.5


class piu_anteil_kantone_mitarbeitende(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil kantonale Mitarbeitende am PIU-Personal"
    reference = "SR 129 Art. 28 Abs. 1"

    def formula(person, period, parameters):
        return 0.5


class piu_kanton_traegt_lohnkosten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kantone tragen Lohnkosten inkl. Sozialversicherungsbeitraege der entsandten Mitarbeitenden"
    reference = "SR 129 Art. 28 Abs. 2"

    def formula(person, period, parameters):
        return True


class piu_personal_informationsverwendung_beschraenkt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "PIU-Mitarbeitende duerfen Informationen nur fuer PIU-Aufgaben verwenden"
    reference = "SR 129 Art. 28 Abs. 4"

    def formula(person, period, parameters):
        return True
