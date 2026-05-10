"""SR 128.51 Art. 6

Generated from: ch/128/de/128.51.md

Offenlegung von Schwachstellen: BACS coordinates disclosure with a default
90-day deadline. The deadline can be shortened or extended under specific
conditions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schwachstelle_gefunden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Schwachstelle an Hard- oder Software gefunden wurde"
    reference = "SR 128.51 Art. 6 Abs. 1"


class schwachstelle_gefaehrdet_kritische_infrastruktur(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schwachstelle die Funktionsfaehigkeit kritischer Infrastrukturen gefaehrdet"
    reference = "SR 128.51 Art. 6 Abs. 3 Bst. a"


class schwachstelle_betrifft_verbreitete_systeme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schwachstelle weit verbreitete Systeme betrifft"
    reference = "SR 128.51 Art. 6 Abs. 3 Bst. b"


class schwachstelle_wird_fuer_angriff_genutzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schwachstelle fuer einen Cyberangriff verwendet wird oder leicht ausgenutzt werden kann"
    reference = "SR 128.51 Art. 6 Abs. 3 Bst. c"


class behebung_besonders_aufwendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Behebung der Schwachstelle besonders aufwendig ist"
    reference = "SR 128.51 Art. 6 Abs. 4"


class offenlegungsfrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist in Tagen fuer die Offenlegung der Schwachstelle"
    reference = "SR 128.51 Art. 6"

    def formula(person, period, parameters):
        standard_frist = 90
        verkuerzung = (
            person('schwachstelle_gefaehrdet_kritische_infrastruktur', period)
            + person('schwachstelle_betrifft_verbreitete_systeme', period)
            + person('schwachstelle_wird_fuer_angriff_genutzt', period)
        ) > 0
        verlaengerung = person('behebung_besonders_aufwendig', period)
        # Shortened or extended deadline; exact values are at BACS discretion.
        # Model: shortened = 45 days, extended = 180 days as reasonable defaults.
        import numpy as np
        return np.where(verkuerzung, 45, np.where(verlaengerung, 180, standard_frist))
