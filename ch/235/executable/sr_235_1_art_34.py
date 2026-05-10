"""SR 235.1 Art. 34

Generated from: ch/235/de/235.1.md

Verletzung der Auskunfts-, Melde- und Mitwirkungspflichten.
Strafbestimmung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_vorsaetzlich_falsche_auskunft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vorsaetzlich falsche oder unvollstaendige Auskunft nach Art. 8-10, 14 erteilt"
    reference = "SR 235.1 Art. 34 Abs. 1 lit. a"


class dsg_informationspflicht_vorsaetzlich_unterlassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Informationspflicht nach Art. 14 vorsaetzlich unterlassen"
    reference = "SR 235.1 Art. 34 Abs. 1 lit. b"


class dsg_meldung_vorsaetzlich_unterlassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Meldung nach Art. 6/11a vorsaetzlich unterlassen oder falsche Angaben gemacht"
    reference = "SR 235.1 Art. 34 Abs. 2 lit. a"


class dsg_mitwirkung_verweigert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Dem Beauftragten falsche Auskuenfte erteilt oder Mitwirkung verweigert"
    reference = "SR 235.1 Art. 34 Abs. 2 lit. b"


class dsg_strafbar_art34(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Strafbarkeit nach Art. 34 DSG (Busse)"
    reference = "SR 235.1 Art. 34"

    def formula(person, period, parameters):
        falsche_auskunft = person('dsg_vorsaetzlich_falsche_auskunft', period)
        info_unterlassen = person('dsg_informationspflicht_vorsaetzlich_unterlassen', period)
        meldung = person('dsg_meldung_vorsaetzlich_unterlassen', period)
        mitwirkung = person('dsg_mitwirkung_verweigert', period)
        return (falsche_auskunft + info_unterlassen + meldung + mitwirkung) > 0
