"""SR 821.42 Art. 1

Generated from: ch/821/de/821.42.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kollektivstreitigkeit_ueberkantonal(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kollektivstreitigkeit reicht ueber die Grenzen eines Kantons hinaus"
    reference = "SR 821.42 Art. 1 Abs. 1"


class verstaendigungsversuche_gescheitert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Verstaendigungsversuche der Parteien durch direkte Verhandlungen sind gescheitert"
    reference = "SR 821.42 Art. 1 Abs. 3"


class vertragliche_einigungsstelle_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vertragliche paritaetische Einigungs- oder Schiedsstelle besteht"
    reference = "SR 821.42 Art. 1 Abs. 3"


class streitigkeit_nur_regional(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Streitigkeit ist nur von regionaler Bedeutung"
    reference = "SR 821.42 Art. 1 Abs. 2"


class einigungsstelle_einsetzbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Eidgenoessische Einigungsstelle kann eingesetzt werden "
        "(Kollektivstreitigkeit ueberkantonal, Verstaendigungsversuche gescheitert, "
        "keine vertragliche Einigungsstelle)"
    )
    reference = "SR 821.42 Art. 1 Abs. 1, 3"

    def formula(person, period, parameters):
        ueberkantonal = person('kollektivstreitigkeit_ueberkantonal', period)
        gescheitert = person('verstaendigungsversuche_gescheitert', period)
        keine_vertragliche = not_(person('vertragliche_einigungsstelle_vorhanden', period))
        return ueberkantonal * gescheitert * keine_vertragliche


class kantonales_einigungsamt_zustaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Kantonales Einigungsamt ist mit der Vermittlung betraut "
        "(Streitigkeit ueberkantonal aber nur regional)"
    )
    reference = "SR 821.42 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        ueberkantonal = person('kollektivstreitigkeit_ueberkantonal', period)
        regional = person('streitigkeit_nur_regional', period)
        return ueberkantonal * regional
