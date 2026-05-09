"""SR 510.35 Art. 7 - Zivile seuchenpolizeiliche Massnahmen

Generated from: ch/510/de/510.35.md

Die Truppe hat den zivilen seuchenpolizeilichen Massnahmen Folge zu leisten.
Wehrmaenner, die von einer zivilen Massnahme betroffen werden, duerfen
waehrend deren Dauer weder einruecken noch an militaerischen Veranstaltungen
teilnehmen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class von_ziviler_seuchenpolizeilicher_massnahme_betroffen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in ihrem Wohn- oder Arbeitsort von einer zivilen seuchenpolizeilichen Massnahme betroffen ist"
    reference = "SR 510.35 Art. 7 Abs. 2"


class darf_nicht_einruecken_wegen_ziviler_massnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person waehrend der Dauer der zivilen seuchenpolizeilichen Massnahme nicht einruecken darf"
    reference = "SR 510.35 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        return person('von_ziviler_seuchenpolizeilicher_massnahme_betroffen', period)
