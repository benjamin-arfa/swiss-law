"""SR 311.1 Art. 25

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strafdrohung_freiheitsstrafe_min_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindeststrafe fuer das Erwachsenendelikt in Jahren Freiheitsstrafe"
    reference = "SR 311.1 Art. 25 Abs. 2 lit. a"


class besonders_skrupellos_gehandelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat der Jugendliche besonders skrupellos gehandelt (Art. 122, 140 Ziff. 3, 184 StGB)"
    reference = "SR 311.1 Art. 25 Abs. 2 lit. b"


class freiheitsentzug_max_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer des Freiheitsentzugs in Tagen"
    reference = "SR 311.1 Art. 25"

    def formula(person, period, parameters):
        alter = person('alter_bei_tat', period)
        strafdrohung = person('strafdrohung_freiheitsstrafe_min_jahre', period)
        skrupellos = person('besonders_skrupellos_gehandelt', period)
        verbrechen = person('verbrechen_oder_vergehen', period)

        # Under 15: no imprisonment
        # 15-15: up to 1 year (365 days) for crimes/misdemeanors
        # 16+: up to 4 years (1460 days) if crime threatened with 3+ years
        #       or specific offenses committed ruthlessly
        schweres_delikt = (strafdrohung >= 3) + skrupellos > 0

        return where(
            alter < 15,
            0,
            where(
                (alter >= 16) * schweres_delikt,
                1460,  # 4 years
                where(
                    verbrechen,
                    365,  # 1 year
                    0
                )
            )
        )
