"""SR 821.42 Art. 3

Generated from: ch/821/de/821.42.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class pflicht_erscheinen_einigungsstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Von der Einigungsstelle Vorgeladene sind verpflichtet zu erscheinen, "
        "zu verhandeln und Auskunft zu erteilen"
    )
    reference = "SR 821.42 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        # All summoned persons are obligated
        return person('ist_vorgeladen_einigungsstelle', period)


class ist_vorgeladen_einigungsstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist von der Einigungsstelle vorgeladen"
    reference = "SR 821.42 Art. 3 Abs. 1"


class ordnungsbusse_einigungsstelle_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Ordnungsbusse bei Widerhandlung gegen Erscheinungspflicht (CHF)"
    reference = "SR 821.42 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        # Art. 3 Abs. 1: Ordnungsbussen bis zu 500 Franken
        return person('ist_vorgeladen_einigungsstelle', period) * 500.0
