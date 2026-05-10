"""SR 745.1 Art. 1

Generated from: ch/745/de/745.1.md

Personenbefoerderungsgesetz (PBG) - Geltungsbereich.
Regelt die dem Regal unterstehende Personenbefoerderung sowie die
Nutzung der dafuer verwendeten Anlagen und Fahrzeuge.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unterliegt_personenbefoerderungsgesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetigkeit unterliegt dem Personenbefoerderungsgesetz (SR 745.1)"
    reference = "SR 745.1 Art. 1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 1-2: Das Gesetz regelt die dem Regal unterstehende
        # Personenbefoerderung. Das Regal umfasst regelmaessige und
        # gewerbsmaessige Personenbefoerderung auf Eisenbahnen, Strasse,
        # Wasser sowie mit Seilbahnen, Aufzuegen und anderen spurgefuehrten
        # Transportmitteln.
        ist_regelmaessig = person('personenbefoerderung_regelmaessig', period)
        ist_gewerbsmaessig = person('personenbefoerderung_gewerbsmaessig', period)
        return ist_regelmaessig * ist_gewerbsmaessig


class personenbefoerderung_regelmaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Personenbefoerderung ist regelmaessig (mehr als 2 Fahrten in 15 Tagen zwischen gleichen Orten)"
    reference = "SR 745.1 Art. 2 Abs. 1 lit. a"


class personenbefoerderung_gewerbsmaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Personenbefoerderung ist gewerbsmaessig (gegen Entgelt oder zur Erlangung eines geschaeftlichen Vorteils)"
    reference = "SR 745.1 Art. 2 Abs. 1 lit. b"
