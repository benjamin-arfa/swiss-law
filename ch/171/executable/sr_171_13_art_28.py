"""SR 171.13 Art. 28

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mindeststunden_vorstoesse_pro_session(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestanzahl Stunden pro ordentlicher Session für parlamentarische Initiativen und Vorstösse"
    reference = "SR 171.13 Art. 28 Abs. 1"

    def formula(person, period, parameters):
        return 8


class schwelle_schriftliches_verfahren_parl_initiative(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der Kommissionsmitglieder, unter dem eine parlamentarische Initiative im schriftlichen Verfahren behandelt wird"
    reference = "SR 171.13 Art. 28 Abs. 3"

    def formula(person, period, parameters):
        return 0.2
