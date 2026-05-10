"""SR 172.041.0 Art. 2

Generated from: ch/172/de/172.041.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class spruchgebuehr_ohne_vermoegensinteresse_min_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Spruchgebuehr ohne Vermoegensinteresse in CHF (Art. 2 Abs. 1)"
    reference = "SR 172.041.0 Art. 2"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 100

class spruchgebuehr_ohne_vermoegensinteresse_max_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Spruchgebuehr ohne Vermoegensinteresse in CHF (Art. 2 Abs. 1)"
    reference = "SR 172.041.0 Art. 2"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 5000

class streitwert_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Streitwert / Vermoegensinteresse in CHF"
    reference = "SR 172.041.0 Art. 2"

class spruchgebuehr_max_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Spruchgebuehr basierend auf Streitwert in CHF (Art. 2 Abs. 2)"
    reference = "SR 172.041.0 Art. 2"

    def formula(person, period, parameters):
        sw = person('streitwert_chf', period)
        return where(sw <= 10000, 4000,
               where(sw <= 20000, 5000,
               where(sw <= 50000, 6000,
               where(sw <= 100000, 7000,
               where(sw <= 200000, 8000,
               where(sw <= 500000, 12000,
               where(sw <= 1000000, 20000,
               where(sw <= 5000000, 40000, 50000))))))))
