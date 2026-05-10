"""SR 443.1 Art. 24c

Generated from: ch/443/de/443.1.md

Anrechenbare Aufwendungen: Aufwendungen fuer Ankauf, Produktion, Koproduktion
von Schweizer Filmen an unabhaengige Dritte. Bewerbung/Vermittlung max 500'000
CHF pro Jahr und Fernsehprogramm. Subventionen sind abzuziehen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aufwendungen_bewerbung_vermittlung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufwendungen fuer Bewerbung/Vermittlung CH-Filme (CHF)"
    reference = "SR 443.1 Art. 24c Abs. 2 Bst. d"


class subventionen_bund_kantone_gemeinden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kultur-/Filmfoerderungssubventionen von Bund, Kantonen, Gemeinden (CHF)"
    reference = "SR 443.1 Art. 24c Abs. 3"


class max_anrechenbar_bewerbung_vermittlung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Max anrechenbare Bewerbung/Vermittlung (500'000 CHF/Jahr/Programm)"
    reference = "SR 443.1 Art. 24c Abs. 2 Bst. d"

    def formula(person, period, parameters):
        aufwand = person('aufwendungen_bewerbung_vermittlung', period)
        import numpy as np
        return np.minimum(aufwand, 500000)
