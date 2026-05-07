"""SR 611.010 Art. 3

Generated from: ch/611/de/611.010.md

Art. 3: Krisenverhütung - Der Bundesrat trifft im Rahmen der Ausgabenplanung
die nötigen Vorbereitungen für den Fall einer rückläufigen wirtschaftlichen
Entwicklung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class krisenverhuetung_vorbereitung_getroffen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Bundesrat hat im Rahmen der Ausgabenplanung Vorbereitungen für den Fall "
        "einer rückläufigen wirtschaftlichen Entwicklung getroffen (Art. 3)"
    )
    reference = "SR 611.010 Art. 3"

    def formula(person, period, parameters):
        # Art. 3: Der Bundesrat trifft im Rahmen der Ausgabenplanung die
        # nötigen Vorbereitungen für den Fall einer rückläufigen
        # wirtschaftlichen Entwicklung.
        # Declaratory obligation on the Federal Council.
        return person('wirtschaftliche_entwicklung_ruecklaeufig', period)


class wirtschaftliche_entwicklung_ruecklaeufig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wirtschaftliche Entwicklung ist rückläufig"
    reference = "SR 611.010 Art. 3"
