"""SR 935.01 Art. 1

Generated from: ch/935/de/935.01.md

Gegenstand und Geltungsbereich des BGMD:
- Regelt Meldepflicht und Nachprüfung der Berufsqualifikationen
- Gilt für Personen mit im Ausland erworbenen Qualifikationen
- Höchstens 90 Arbeitstage pro Kalenderjahr in der Schweiz
- Muss sich auf Richtlinie 2005/36/EG berufen können
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class qualifikation_im_ausland_erworben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Berufsqualifikation im Ausland erworben wurde"
    reference = "SR 935.01 Art. 1 Abs. 2 Bst. a"


class geplante_arbeitstage_schweiz(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Geplante Arbeitstage pro Kalenderjahr in der Schweiz"
    reference = "SR 935.01 Art. 1 Abs. 2 Bst. b"


class kann_sich_auf_rl_2005_36_berufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich die Person auf Richtlinie 2005/36/EG berufen kann (FZA/EFTA)"
    reference = "SR 935.01 Art. 1 Abs. 2 Bst. c"


class beruf_ist_reglementiert_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Beruf in der Schweiz reglementiert ist"
    reference = "SR 935.01 Art. 1 Abs. 2"


class unterliegt_bgmd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person dem BGMD (Meldepflicht/Nachprüfung) unterliegt"
    reference = "SR 935.01 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        ausland = person('qualifikation_im_ausland_erworben', period)
        tage = person('geplante_arbeitstage_schweiz', period)
        rl = person('kann_sich_auf_rl_2005_36_berufen', period)
        reglementiert = person('beruf_ist_reglementiert_schweiz', period)
        max_tage = parameters(period).sr_935_01.max_arbeitstage_pro_jahr

        return (
            ausland *
            (tage <= max_tage) *
            rl *
            reglementiert
        )
