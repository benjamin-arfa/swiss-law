"""SR 282.11 Art. 10 - Verpfaendung

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class vermoegenswert_dient_oeffentlichen_zwecken(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vermoegenswert dient oeffentlichen Zwecken"
    reference = "SR 282.11 Art. 10 Abs. 1"


class pfaendung_erfordert_zustimmung_kantonsregierung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Pfaendung erfordert die Zustimmung der Kantonsregierung"
    reference = "SR 282.11 Art. 10 Abs. 1"


class zustimmung_kantonsregierung_verpfaendung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Kantonsregierung hat der Verpfaendung zugestimmt"
    reference = "SR 282.11 Art. 10 Abs. 1"


# Computed variables

class verpfaendung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verpfaendung ist zulaessig"
    reference = "SR 282.11 Art. 10"

    def formula(self, period, parameters):
        oeffentlich = self('vermoegenswert_dient_oeffentlichen_zwecken', period)
        erfordert_zustimmung = self('pfaendung_erfordert_zustimmung_kantonsregierung', period)
        zustimmung = self('zustimmung_kantonsregierung_verpfaendung', period)
        # Unpfaendbare Werte koennen nicht verpfaendet werden, solange sie oeffentlichen Zwecken dienen
        # Wenn Zustimmung noetig, muss sie auch fuer Verpfaendung vorliegen
        nicht_oeffentlich = 1 - oeffentlich
        zustimmung_ok = (1 - erfordert_zustimmung) + (erfordert_zustimmung * zustimmung) > 0
        return nicht_oeffentlich * zustimmung_ok
