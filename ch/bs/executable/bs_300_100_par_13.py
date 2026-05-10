"""BS 300.100 § 13

Generated from: ch/bs/de/300.100.md

§ 13 Leistungen fuer Kinder und Jugendliche: For children and youth of
compulsory school age whose parents are domiciled in Basel, the canton
provides: a) promotion of dental health, b) necessary treatment of
diseased teeth, c) examination and treatment of positional anomalies.
The Regierungsrat determines which services are provided free of charge.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bs_kind_schulpflichtiges_alter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kind oder Jugendliche/r im schulpflichtigen Alter (BS 300.100 § 13 Abs. 1)"
    reference = "BS 300.100 § 13 Abs. 1"


class bs_eltern_wohnsitz_basel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Eltern haben Wohnsitz in Basel (BS 300.100 § 13 Abs. 1)"
    reference = "BS 300.100 § 13 Abs. 1"


class bs_zahngesundheitsfoerderung_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Foerderung der Zahngesundheit (BS 300.100 § 13 Abs. 1 Bst. a)"
    reference = "BS 300.100 § 13 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        schulpflichtig = person('bs_kind_schulpflichtiges_alter', period)
        eltern_bs = person('bs_eltern_wohnsitz_basel', period)
        return schulpflichtig * eltern_bs


class bs_zahnbehandlung_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf notwendige Behandlung kranker Zaehne (BS 300.100 § 13 Abs. 1 Bst. b)"
    reference = "BS 300.100 § 13 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        schulpflichtig = person('bs_kind_schulpflichtiges_alter', period)
        eltern_bs = person('bs_eltern_wohnsitz_basel', period)
        return schulpflichtig * eltern_bs


class bs_stellungsanomalie_behandlung_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Untersuchung und Behandlung von Stellungsanomalien (BS 300.100 § 13 Abs. 1 Bst. c)"
    reference = "BS 300.100 § 13 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        schulpflichtig = person('bs_kind_schulpflichtiges_alter', period)
        eltern_bs = person('bs_eltern_wohnsitz_basel', period)
        return schulpflichtig * eltern_bs
