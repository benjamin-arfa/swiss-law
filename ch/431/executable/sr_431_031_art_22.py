"""SR 431.031 Art. 22

Generated from: ch/431/de/431.031.md

Aufbewahrung von Daten zu geloeschten UID-Einheiten und Administrativeinheiten -
hoechstens 30 Jahre ab Loeschung, danach Archivierung anbieten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class uid_einheit_geloescht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "UID-Einheit ist im UID-Register als geloescht gekennzeichnet"
    reference = "SR 431.031 Art. 22 Abs. 1"


class jahre_seit_uid_loeschung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre seit der Loeschung der UID-Einheit"
    reference = "SR 431.031 Art. 22 Abs. 1"


class max_aufbewahrungsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Aufbewahrungsdauer fuer geloeschte UID-Daten in Jahren"
    reference = "SR 431.031 Art. 22 Abs. 1"
    default_value = 30


class uid_daten_aufbewahrung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aufbewahrung der Daten der geloeschten UID-Einheit ist zulaessig"
    reference = "SR 431.031 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('uid_einheit_geloescht', period) *
            (person('jahre_seit_uid_loeschung', period) <= person('max_aufbewahrungsdauer_jahre', period))
        )


class uid_stellen_einsichtsrecht_aktiv(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einsichtsrecht der UID-Stellen besteht waehrend der Aufbewahrungsdauer"
    reference = "SR 431.031 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        return person('uid_daten_aufbewahrung_zulaessig', period)


class uid_daten_vernichtung_faellig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten der geloeschten UID-Einheit muessen vernichtet werden (nach 30 Jahren)"
    reference = "SR 431.031 Art. 22 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('uid_einheit_geloescht', period) *
            (person('jahre_seit_uid_loeschung', period) > person('max_aufbewahrungsdauer_jahre', period))
        )
