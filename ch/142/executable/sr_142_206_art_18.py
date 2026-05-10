"""SR 142.206 Art. 18

Generated from: ch/142/de/142.206.md

Recht der betroffenen Personen auf Auskunft ueber die Daten:
Richtet sich nach dem Datenschutzgesetz. Das SEM bearbeitet
die Auskunftsgesuche.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ees_auskunftsrecht_betroffene_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die betroffene Person ein Auskunftsrecht ueber ihre EES-Daten hat"
    reference = "SR 142.206 Art. 18 Abs. 1"

    def formula_2022_05(person, period, parameters):
        return True
