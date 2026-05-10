"""SR 821.421 Art. 9

Generated from: ch/821/de/821.421.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class persoenliches_erscheinen_pflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Parteien muessen persoenlich erscheinen und duerfen sich "
        "nicht vertreten lassen (Verbeistaendigung ist zulaessig)"
    )
    reference = "SR 821.421 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_partei_einigungsverfahren', period)


class ist_partei_einigungsverfahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Partei im Einigungsverfahren"
    reference = "SR 821.421 Art. 9"


class obmann_kann_personenzahl_beschraenken(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Der Obmann ist befugt, die Zahl der zur Verhandlung "
        "zuzulassenden Personen zu beschraenken"
    )
    reference = "SR 821.421 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        # This is always true as a structural rule
        return person('ist_partei_einigungsverfahren', period) * 0 + 1
