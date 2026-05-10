"""SR 672.3 Art. 4 — Anwendbarkeit

Bundesgesetz über die Anerkennung privater Vereinbarungen zur Vermeidung der Doppelbesteuerung.
Generated from: ch/de/672/672.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vereinbarung_anerkannt_durch_bundesrat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Vereinbarung wurde durch den Bundesrat anerkannt"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_4"


class vereinbarung_schweizweit_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vereinbarung ist auf dem ganzen Gebiet der Schweiz anwendbar (SR 672.3 Art. 4)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_4"

    def formula(person, period, parameters):
        # Art. 4: Eine Vereinbarung wird mit ihrer Anerkennung durch den
        # Bundesrat auf dem ganzen Gebiet der Schweiz anwendbar.
        return person('vereinbarung_anerkannt_durch_bundesrat', period)
