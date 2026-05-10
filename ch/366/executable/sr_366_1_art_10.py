"""SR 366.1 Art. 10

Generated from: ch/366/de/366.1.md

Informationssystem Verkehrszulassung (IVZ): NZB-Abfrageberechtigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fahrzeug_im_ausland_gestohlen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Im Ausland gestohlenes Fahrzeug ist in der Schweiz immatrikuliert"
    reference = "SR 366.1 Art. 10 Abs. 2"


class nzb_meldung_an_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "NZB teilt die Immatrikulation des gestohlenen Fahrzeugs den auslaendischen Behoerden mit"
    reference = "SR 366.1 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        return person('fahrzeug_im_ausland_gestohlen', period)
