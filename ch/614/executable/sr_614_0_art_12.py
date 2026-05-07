"""SR 614.0 Art. 12

Generated from: ch/614/de/614.0.md

Art. 12: Prüfungsbefunde und Beanstandungen - Verfahren bei Befundmitteilung,
Beanstandungen der Ordnungsmässigkeit, Rechtmässigkeit und Wirtschaftlichkeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class efk_beanstandung_wirtschaftlichkeit_zurueckgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Geprüfte Verwaltungseinheit weist eine die Wirtschaftlichkeit "
        "berührende Beanstandung der EFK zurück (Art. 12 Abs. 3)"
    )
    reference = "SR 614.0 Art. 12 Abs. 3"


class efk_antraege_an_departement(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK unterbreitet bei zurückgewiesener Wirtschaftlichkeits-Beanstandung "
        "Anträge dem vorgesetzten Departement (Art. 12 Abs. 3)"
    )
    reference = "SR 614.0 Art. 12 Abs. 3"

    def formula(person, period, parameters):
        return person('efk_beanstandung_wirtschaftlichkeit_zurueckgewiesen', period)


class efk_beanstandung_ordnungsmaessigkeit_zurueckgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Geprüfte Verwaltungseinheit weist eine die Ordnungsmässigkeit oder "
        "Rechtmässigkeit berührende Beanstandung zurück (Art. 12 Abs. 4)"
    )
    reference = "SR 614.0 Art. 12 Abs. 4"


class efk_kann_ordnungswidrigkeit_formell_feststellen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK kann bei zurückgewiesener Beanstandung die Ordnungs- oder "
        "Rechtswidrigkeit formell feststellen und eine Weisung erlassen (Art. 12 Abs. 4)"
    )
    reference = "SR 614.0 Art. 12 Abs. 4"

    def formula(person, period, parameters):
        return person('efk_beanstandung_ordnungsmaessigkeit_zurueckgewiesen', period)


class verwaltungseinheit_kann_bundesrat_anfechten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Geprüfte Verwaltungseinheit kann Entscheid der EFK beim Bundesrat "
        "anfechten (Art. 12 Abs. 5)"
    )
    reference = "SR 614.0 Art. 12 Abs. 5"

    def formula(person, period, parameters):
        beanstandung_om = person('efk_beanstandung_ordnungsmaessigkeit_zurueckgewiesen', period)
        beanstandung_wi = person('efk_beanstandung_wirtschaftlichkeit_zurueckgewiesen', period)
        return beanstandung_om + beanstandung_wi
