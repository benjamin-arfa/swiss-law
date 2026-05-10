"""SR 513.61 Art. 9

Generated from: ch/513/de/513.61.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mp_spontanhilfe_groesseres_ereignis(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Groesseres polizeiliches Ereignis im Zusammenhang mit Verbrechen oder Vergehen liegt vor"


class mp_spontanhilfe_freie_mittel_in_naehe(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "MP verfuegt in der Naehe ueber freie Mittel im Dienst"


class mp_spontanhilfe_zivile_mittel_ausgeschoepft(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Mittel der gesuchstellenden Organe ausgeschoepft oder Reaktionszeit groesser als MP"


class mp_spontanhilfe_zulässig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Spontanhilfe der MP ist zulaessig (Art. 9 Abs. 2 SR 513.61)"
    reference = "SR 513.61 Art. 9"

    def formula(person, period, parameters):
        # Spontanhilfe wird nur geleistet, wenn alle drei Bedingungen erfuellt:
        # a) groesseres polizeiliches Ereignis (Verbrechen/Vergehen)
        # b) MP verfuegt in der Naehe ueber freie Mittel
        # c) Mittel der gesuchstellenden Organe ausgeschoepft
        ereignis = person('mp_spontanhilfe_groesseres_ereignis', period)
        mittel = person('mp_spontanhilfe_freie_mittel_in_naehe', period)
        ausgeschoepft = person('mp_spontanhilfe_zivile_mittel_ausgeschoepft', period)
        return ereignis * mittel * ausgeschoepft


class mp_spontanhilfe_max_dauer_stunden(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Maximale Dauer der Spontanhilfe in Stunden (Art. 9 Abs. 3 SR 513.61)"
    reference = "SR 513.61 Art. 9"

    def formula(person, period, parameters):
        # Die Spontanhilfe dauert maximal 48 Stunden
        return 48


class mp_spontanhilfe_kostenlos(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Spontanhilfe ist kostenlos (Art. 9 Abs. 3 SR 513.61)"
    reference = "SR 513.61 Art. 9"

    def formula(person, period, parameters):
        return True
