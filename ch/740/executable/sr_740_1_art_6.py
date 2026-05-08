"""SR 740.1 Art. 6 - Alpentransitboerse

Generated from: ch/740/de/740.1.md

Rechte fuer alpenquerende Fahrten schwerer Gueterverkehrsfahrzeuge
werden nichtdiskriminierend nach marktwirtschaftlichen Grundsaetzen
versteigert.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class alpentransitboerse_eingefuehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Alpentransitboerse ist eingefuehrt"
    reference = "SR 740.1 Art. 6 Abs. 4"


class durchfahrtsrecht_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fuer das schwere Gueterverkehrsfahrzeug liegt ein Durchfahrtsrecht vor"
    reference = "SR 740.1 Art. 6 Abs. 4"


class alpenquerung_auf_transitstrasse_erlaubt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Fahrzeug darf die Alpen auf den Transitstrassen queren"
    reference = "SR 740.1 Art. 6 Abs. 4"

    def formula(self, period, parameters):
        boerse = self('alpentransitboerse_eingefuehrt', period)
        recht = self('durchfahrtsrecht_vorhanden', period)
        # Ohne Boerse ist die Durchfahrt erlaubt; mit Boerse braucht es ein Durchfahrtsrecht
        return (1 - boerse) + boerse * recht
