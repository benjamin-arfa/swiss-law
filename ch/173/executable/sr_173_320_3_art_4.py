"""SR 173.320.3 Art. 4

Generated from: ch/173/de/173.320.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gebuehr_fotokopie_a4_rappen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer A4-Fotokopie in Rappen pro Seite (Art. 4 lit. a)"
    reference = "SR 173.320.3 Art. 4"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 50

class gebuehr_fotokopie_a3_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer A3-Fotokopie in CHF pro Seite (Art. 4 lit. a)"
    reference = "SR 173.320.3 Art. 4"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 1.0

class gebuehr_nachforschung_akten_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer Nachforschungen in Akten in CHF pro halbe Stunde (Art. 4 lit. c)"
    reference = "SR 173.320.3 Art. 4"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 50.0

class gebuehr_andere_nachforschungen_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer andere Nachforschungen in CHF pro halbe Stunde (Art. 4 lit. d)"
    reference = "SR 173.320.3 Art. 4"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 60.0

class gebuehr_urteilsabgabe_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer Urteilsabgabe an Dritte in CHF (Art. 4 lit. e)"
    reference = "SR 173.320.3 Art. 4"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 40.0

class gebuehr_rechtskraftbescheinigung_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer Rechtskraftbescheinigung in CHF (Art. 4 lit. f)"
    reference = "SR 173.320.3 Art. 4"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 40.0

class gebuehr_beglaubigung_unterschrift_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer Beglaubigung einer Unterschrift in CHF (Art. 4 lit. g)"
    reference = "SR 173.320.3 Art. 4"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 40.0

class gebuehr_beglaubigung_zusaetzliche_unterschrift_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zuschlag fuer jede zusaetzliche Unterschrift in CHF (Art. 4 lit. g)"
    reference = "SR 173.320.3 Art. 4"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 10.0

class gebuehr_sitzungssaal_halbtag_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer Benuetzung Sitzungssaal pro halben Tag in CHF (Art. 4 lit. i)"
    reference = "SR 173.320.3 Art. 4"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 100.0
