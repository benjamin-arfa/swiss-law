"""SR 367.1 Art. 29

Generated from: ch/367/de/367.1.md

Weitergefuehrter Bezug von Produkten von HPI ohne Unterzeichnung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_hpi_leistungsbezueger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist im Verein HPI vertreten oder bezieht bestehende HPI-Produkte"
    reference = "SR 367.1 Art. 29 Abs. 1"


class hat_vereinbarung_unterzeichnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat die PTI-Vereinbarung unterzeichnet"
    reference = "SR 367.1 Art. 29 Abs. 1"


class uebergangsfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Uebergangsfrist fuer weitergefuehrten Bezug ohne Vereinbarung (in Jahren)"
    reference = "SR 367.1 Art. 29 Abs. 1"

    def formula(person, period):
        return 2
