"""SR 455.110.2 Art. 19

Generated from: ch/455/de/455.110.2.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class zeit_zwischen_entbluten_und_weiteren_arbeiten_minuten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zeit zwischen Beginn des Entblutens und weiteren Schlachtarbeiten in Minuten"
    reference = "SR 455.110.2 Art. 19 Abs. 3"


class ist_schlachtvieh(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier ist Schlachtvieh (nicht Gefluegel)"
    reference = "SR 455.110.2 Art. 19 Abs. 3"


class entblutung_wartefrist_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wartefrist zwischen Entbluten und weiteren Schlachtarbeiten konform (min 3 Min. fuer Schlachtvieh) nach Art. 19 Abs. 3 SR 455.110.2"
    reference = "SR 455.110.2 Art. 19 Abs. 3"

    def formula(person, period, parameters):
        zeit = person('zeit_zwischen_entbluten_und_weiteren_arbeiten_minuten', period)
        schlachtvieh = person('ist_schlachtvieh', period)
        # Mindestens 3 Minuten fuer Schlachtvieh
        return where(schlachtvieh, zeit >= 3.0, True)
