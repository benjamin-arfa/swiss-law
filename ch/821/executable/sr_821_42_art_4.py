"""SR 821.42 Art. 4

Generated from: ch/821/de/821.42.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verfahren_kostenlos(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfahren vor der Einigungsstelle ist grundsaetzlich kostenlos"
    reference = "SR 821.42 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        mutwillig = person('mutwilliges_verhalten_einigungsverfahren', period)
        return not_(mutwillig)


class mutwilliges_verhalten_einigungsverfahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Partei hat mutwillig das Verfahren veranlasst oder erschwert"
    reference = "SR 821.42 Art. 4 Abs. 2"


class verfahrenskosten_auferlegt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Verfahrenskosten ganz oder teilweise der mutwilligen Partei auferlegt"
    )
    reference = "SR 821.42 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        return person('mutwilliges_verhalten_einigungsverfahren', period)


class vermittlung_gescheitert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vermittlung vor der Einigungsstelle ist gescheitert"
    reference = "SR 821.42 Art. 4 Abs. 3"


class oeffentlichkeit_informiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Einigungsstelle informiert Oeffentlichkeit ueber den Sachverhalt "
        "nach gescheiterter Vermittlung und fehlendem Schiedsverfahren"
    )
    reference = "SR 821.42 Art. 4 Abs. 3"

    def formula(person, period, parameters):
        gescheitert = person('vermittlung_gescheitert', period)
        schiedsbereit = person('parteien_schiedsverfahren_bereit', period)
        return gescheitert * not_(schiedsbereit)


class parteien_schiedsverfahren_bereit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Parteien erklaeren sich zur Durchfuehrung eines Schiedsverfahrens bereit"
    reference = "SR 821.42 Art. 4 Abs. 3"
