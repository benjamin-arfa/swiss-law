"""SR 744.211 Art. 5

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_anlage_plangenehmigung_nach_eisenbahnrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Plangenehmigungsverfahren für Trolleybusanlagen und Nebenanlagen richtet sich "
        "sinngemäss nach Eisenbahngesetz (SR 742.101) und PGV-Eisenbahnanlagen (SR 742.142.1)"
    )
    reference = "SR 744.211 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        # Art. 5 Abs. 1: Das Plangenehmigungsverfahren für Bauten und Anlagen,
        # die ganz oder überwiegend dem Betrieb einer Trolleybuslinie dienen
        # (Trolleybusanlagen), sowie für Bauten und Anlagen Dritter (Nebenanlagen)
        # richtet sich sinngemäss nach:
        #   - Eisenbahngesetz vom 20. Dezember 1957 (SR 742.101)
        #   - Verordnung vom 2. Februar 2000 über das Plangenehmigungsverfahren
        #     für Eisenbahnanlagen (SR 742.142.1)
        # Applicability is structural (governed by law), not person-specific.
        # Returns True for any subject within scope of the trolleybus ordinance.
        ist_trolleybus_anlage = person('ist_trolleybus_anlage', period)
        ist_nebenanlage = person('ist_nebenanlage_trolleybus', period)
        return ist_trolleybus_anlage + ist_nebenanlage


class ist_trolleybus_anlage(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Baute oder Anlage dient ganz oder überwiegend dem Betrieb einer Trolleybuslinie"
    reference = "SR 744.211 Art. 5 Abs. 1"


class ist_nebenanlage_trolleybus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Baute oder Anlage Dritter (Nebenanlage) im Sinne von SR 744.211 Art. 5"
    reference = "SR 744.211 Art. 5 Abs. 1"
