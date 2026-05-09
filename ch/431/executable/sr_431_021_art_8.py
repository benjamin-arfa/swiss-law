"""SR 431.021 Art. 8

Generated from: ch/431/de/431.021.md

Datenlieferung der kantonalen Register an das BFS - vierteljährlich,
Stichtage 31.3, 30.6, 30.9, 31.12, Lieferung bis Ende Folgemonat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_registerfuehrende_stelle_kanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist kantonale registerfuehrende Stelle nach Art. 2 Abs. 2 RHG"
    reference = "SR 431.021 Art. 8 Abs. 1"


class anzahl_datenlieferungen_pro_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Datenlieferungen pro Jahr an das BFS"
    reference = "SR 431.021 Art. 8 Abs. 2"
    default_value = 4


class lieferfrist_tage_nach_stichtag(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Maximale Lieferfrist in Tagen nach dem Stichtag"
    reference = "SR 431.021 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        # Frist bis Ende des Folgemonats (ca. 30 Tage)
        return person('ist_registerfuehrende_stelle_kanton', period) * 30


class datenlieferung_enthaelt_angemeldete(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Datenlieferung enthaelt alle am Stichtag angemeldeten Personen"
    reference = "SR 431.021 Art. 8 Abs. 3 Bst. a"


class datenlieferung_enthaelt_verstorbene(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Datenlieferung enthaelt die in den letzten 12 Monaten verstorbenen Personen"
    reference = "SR 431.021 Art. 8 Abs. 3 Bst. b"


class datenlieferung_enthaelt_weggezogene(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Datenlieferung enthaelt die in den letzten 12 Monaten weggezogenen Personen"
    reference = "SR 431.021 Art. 8 Abs. 3 Bst. c"


class datenlieferung_vollstaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Datenlieferung ist vollstaendig (alle Kategorien enthalten)"
    reference = "SR 431.021 Art. 8 Abs. 3"

    def formula(person, period, parameters):
        return (
            person('datenlieferung_enthaelt_angemeldete', period) *
            person('datenlieferung_enthaelt_verstorbene', period) *
            person('datenlieferung_enthaelt_weggezogene', period)
        )


class voranmeldung_datentraeger_frist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Voranmeldefrist in Monaten fuer Datenlieferung mittels Datentraeger"
    reference = "SR 431.021 Art. 8 Abs. 4"
    default_value = 3
