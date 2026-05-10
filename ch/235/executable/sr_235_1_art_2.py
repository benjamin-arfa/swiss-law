"""SR 235.1 Art. 2

Generated from: ch/235/de/235.1.md

Geltungsbereich: Definiert den Anwendungsbereich des DSG.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_bearbeitung_durch_private_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bearbeitung von Personendaten durch eine private Person"
    reference = "SR 235.1 Art. 2 Abs. 1 lit. a"


class dsg_bearbeitung_durch_bundesorgan(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bearbeitung von Personendaten durch ein Bundesorgan"
    reference = "SR 235.1 Art. 2 Abs. 1 lit. b"


class dsg_nur_persoenlicher_gebrauch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten werden ausschliesslich zum persoenlichen Gebrauch bearbeitet und nicht an Aussenstehende bekannt gegeben"
    reference = "SR 235.1 Art. 2 Abs. 2 lit. a"


class dsg_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "DSG ist anwendbar auf die Datenbearbeitung"
    reference = "SR 235.1 Art. 2"

    def formula(person, period, parameters):
        durch_private = person('dsg_bearbeitung_durch_private_person', period)
        durch_bund = person('dsg_bearbeitung_durch_bundesorgan', period)
        nur_persoenlich = person('dsg_nur_persoenlicher_gebrauch', period)
        return (durch_private + durch_bund) * not_(nur_persoenlich)
