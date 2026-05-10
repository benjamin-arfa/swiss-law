"""SR 784.104 Art. 7

Generated from: ch/784/de/784.104.md

Nutzungsdauer und Neuzuteilung:
- Adressierungselemente werden in der Regel unbefristet zugeteilt
- Erloschene Elemente frühestens nach 6 Monaten neu zugeteilt
- Ausnahmsweise sofortige Neuzuteilung möglich
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nutzungsberechtigung_erloschen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Nutzungsberechtigung am Adressierungselement erloschen ist"
    reference = "SR 784.104 Art. 7 Abs. 2"


class monate_seit_erloeschen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Monate seit Erlöschen der Nutzungsberechtigung"
    reference = "SR 784.104 Art. 7 Abs. 2"


class ausnahmsweise_sofortige_neuzuteilung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ausnahmsweise eine sofortige Neuzuteilung zulässig ist"
    reference = "SR 784.104 Art. 7 Abs. 2"


class neuzuteilung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Adressierungselement neu zugeteilt werden darf"
    reference = "SR 784.104 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        erloschen = person('nutzungsberechtigung_erloschen', period)
        monate = person('monate_seit_erloeschen', period)
        sofort = person('ausnahmsweise_sofortige_neuzuteilung', period)
        min_monate = parameters(period).sr_784_104.sperrfrist_neuzuteilung_monate

        return erloschen * (sofort + (monate >= min_monate))
