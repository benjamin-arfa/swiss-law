"""SR 614.0 Art. 21

Generated from: ch/614/de/614.0.md

Finanzkontrollgesetz (FKG) - Art. 21: Ausfuehrungsvorschriften.
Ausfuehrungsbestimmungen durch Verordnung der Bundesversammlung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class fkg_ausfuehrungsbestimmungen_durch_bundesversammlung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Ausfuehrungsbestimmungen werden durch eine Verordnung der "
        "Bundesversammlung erlassen (Art. 21)"
    )
    reference = "SR 614.0 Art. 21"

    def formula(person, period, parameters):
        # Art. 21: Delegation provision - Bundesversammlung erlässt
        # Ausführungsbestimmungen. Vorbehalten bleibt Art. 10a Abs. 7.
        # Structural/declaratory - always applicable.
        return person('ist_eidgenoessische_finanzkontrolle', period)
