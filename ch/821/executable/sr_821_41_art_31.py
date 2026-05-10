"""SR 821.41 Art. 31

Generated from: ch/821/de/821.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einigungsstelle_vermittlung_von_amtes_wegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Einigungsstelle tritt von sich aus oder auf Begehren einer Behoerde "
        "oder Beteiligter in die Vermittlung ein"
    )
    reference = "SR 821.41 Art. 31 Abs. 1"


class pflicht_erscheinen_kantonale_einigungsstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Vorgeladene sind bei Busse verpflichtet, vor kantonaler "
        "Einigungsstelle zu erscheinen, zu verhandeln und Auskunft zu erteilen"
    )
    reference = "SR 821.41 Art. 31 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_vorgeladen_kantonale_einigungsstelle', period)


class ist_vorgeladen_kantonale_einigungsstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist von kantonaler Einigungsstelle vorgeladen"
    reference = "SR 821.41 Art. 31 Abs. 2"


class verfahren_kantonale_einigungsstelle_kostenlos(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Verfahren vor der kantonalen Einigungsstelle ist kostenlos"
    reference = "SR 821.41 Art. 31 Abs. 3"

    def formula(person, period, parameters):
        # Art. 31 Abs. 3: Das Verfahren ist kostenlos.
        return person('ist_vorgeladen_kantonale_einigungsstelle', period) + \
               person('einigungsstelle_vermittlung_von_amtes_wegen', period) > 0
