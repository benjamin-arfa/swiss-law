"""SR 501.31 Art. 12 - Notfall- und katastrophenmedizinische Ausbildung

Generated from: ch/501/de/501.31.md

Das BABS foerdert und koordiniert die Zusammenarbeit in der notfall- und
katastrophenmedizinischen Ausbildung. Fuer die Zusammenarbeit mit Stellen
ausserhalb der Bundesverwaltung kann das BABS Leistungsvertraege abschliessen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class babs_notfallausbildung_koordiniert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BABS die Zusammenarbeit in der notfall- und katastrophenmedizinischen Ausbildung foerdert und koordiniert"
    reference = "SR 501.31 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        return True


class babs_leistungsvertrag_extern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BABS Leistungsvertraege mit Stellen ausserhalb der Bundesverwaltung abgeschlossen hat"
    reference = "SR 501.31 Art. 12 Abs. 2"
