"""SR 354.1 § 11

Generated from: ch/354/de/354.1.md
Cost distribution for intermediate care during transports.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zwischenverpflegungskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten der Zwischenverpflegung, Unterkunft und aerztlicher Wartung in CHF"
    reference = "SR 354.1 § 11 Abs. 1"


class verpflegungskosten_pro_kanton(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil an Gesamtkosten der Zwischenverpflegung nach Bevoelkerungszahl in CHF"
    reference = "SR 354.1 § 11 Abs. 1"

    def formula(person, period):
        gesamtkosten = person('zwischenverpflegungskosten', period)
        bevoelkerungsanteil = person('bevoelkerungsanteil_kanton', period)
        return gesamtkosten * bevoelkerungsanteil


class bevoelkerungsanteil_kanton(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bevoelkerungsanteil des Kantons an allen beteiligten Kantonen (0-1)"
    reference = "SR 354.1 § 11 Abs. 1"


class polizeimannschaft_entschaedigung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Entschaedigung fuer Polizeimannschaft bei Verpflegung (immer 0)"
    reference = "SR 354.1 § 11 Abs. 2"

    def formula(person, period):
        # Fuer Polizeimannschaft kann keine Entschaedigung berechnet werden
        return person('zwischenverpflegungskosten', period) * 0
