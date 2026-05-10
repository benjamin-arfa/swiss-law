"""SR 821.42 Art. 5

Generated from: ch/821/de/821.42.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schiedsspruch_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Verbindlicher Schiedsspruch durch die Einigungsstelle ist zulaessig "
        "(Einverstaendnis beider Parteien erforderlich)"
    )
    reference = "SR 821.42 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        einverstaendnis = person('einverstaendnis_beider_parteien_schiedsgericht', period)
        zustaendig = person('einigungsstelle_einsetzbar', period)
        return einverstaendnis * zustaendig


class einverstaendnis_beider_parteien_schiedsgericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einverstaendnis beider Parteien fuer verbindlichen Schiedsspruch"
    reference = "SR 821.42 Art. 5 Abs. 1"


class schiedsspruch_endgueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schiedsstelle entscheidet endgueltig (Vollstreckbarkeit wie Gerichtsurteil)"
    reference = "SR 821.42 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        return person('schiedsspruch_zulaessig', period)
