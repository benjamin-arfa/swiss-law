"""SR 170.32 Art. 23

Generated from: ch/170/de/170.32.md

Verjährung des Schadenersatzanspruchs des Bundes gegenüber einem Beamten
aus Amtspflichtverletzung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class datum_kenntnis_schaden_und_beamter(Variable):
    value_type = date
    entity = Person
    definition_period = YEAR
    label = "Datum der Kenntnisnahme von Schaden und ersatzpflichtigem Beamten durch zuständige Stelle"
    reference = "SR 170.32, Art. 23 Abs. 1"


class schaedigendes_verhalten_ist_strafbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das schädigende Verhalten stellt eine strafbare Handlung dar (Art. 23 Abs. 2 VG)"
    reference = "SR 170.32, Art. 23 Abs. 2"


class schadenersatz_relative_verjaehrung_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Relative Verjährungsfrist des Schadenersatzanspruchs des Bundes in Jahren (Art. 23 Abs. 1 VG)"
    reference = "SR 170.32, Art. 23 Abs. 1"

    def formula(person, period, parameters):
        # 3 Jahre ab Kenntnis von Schaden und ersatzpflichtigem Beamten
        return person('datum_kenntnis_schaden_und_beamter', period) * 0 + 3


class schadenersatz_absolute_verjaehrung_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Absolute Verjährungsfrist des Schadenersatzanspruchs des Bundes in Jahren (Art. 23 Abs. 1 VG)"
    reference = "SR 170.32, Art. 23 Abs. 1"

    def formula(person, period, parameters):
        # 10 Jahre ab schädigendem Verhalten
        return person('datum_schaedigendes_verhalten', period) * 0 + 10
