"""SR 362.1 Art. 11

Generated from: ch/362/de/362.1.md
Cost sharing rules for Schengen/Dublin cooperation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eigene_kosten_schengen_dublin_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Eigene Kosten der Umsetzung, Anwendung und Entwicklung des Schengen/Dublin-Besitzstands in CHF"
    reference = "SR 362.1 Art. 11 Abs. 1"


class beitrag_schengen_portal_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Angemessener Beitrag der Kantone an den Betrieb des Schengen-Portals in CHF"
    reference = "SR 362.1 Art. 11 Abs. 2"


class ist_kanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Handelt es sich um einen Kanton (vs. Bund)"
    reference = "SR 362.1 Art. 11"


class traegt_portal_beitrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Muss einen Beitrag an den Betrieb des Schengen-Portals leisten"
    reference = "SR 362.1 Art. 11 Abs. 2"

    def formula(person, period):
        # Nur Kantone leisten Beitrag
        return person('ist_kanton', period)
