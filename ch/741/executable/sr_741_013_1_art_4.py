"""SR 741.013.1 Art. 4

Generated from: ch/741/de/741.013.1.md

VSKV-ASTRA: Durch Messsysteme festgestellte Widerhandlungen
Each violation detected by a measurement system must be recorded such
that measured values can be uniquely attributed to a specific vehicle
or driver.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class messwert_zuordnung_eindeutig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Messwerte koennen eindeutig einem Fahrzeug oder Fahrzeugfuehrer zugeordnet werden (Art. 4 Abs. 1 VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 4"

    def formula(person, period, parameters):
        return person("fahrzeug_zugeordnet", period) + person("fahrer_zugeordnet", period) > 0


class automatische_feststellung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Feststellung gestuetzt auf Bild-/Filmdokument eines automatischen Messsystems (Art. 4 Abs. 2 VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 4"

    def formula(person, period, parameters):
        return person("bild_oder_filmdokument_vorhanden", period)
