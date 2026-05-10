"""SR 741.013.1 Art. 2

Generated from: ch/741/de/741.013.1.md

VSKV-ASTRA: Kontroll- und Auswertungspersonal
Measurement systems for official determinations during road traffic
controls may only be set up, configured, operated and maintained by
trained personnel.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kontrollpersonal_fachkenntnisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kontrollpersonal verfuegt ueber noetige Fachkenntnisse (Art. 2 Abs. 3 lit. a VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 2"

    def formula(person, period, parameters):
        return person("theoretische_fachkenntnisse", period) * person("praktische_fachkenntnisse", period)


class kontrollpersonal_ermaechtigtet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kontrollpersonal ist durch zustaendige Behoerde ermaechtigtet (Art. 2 Abs. 3 lit. b VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 2"

    def formula(person, period, parameters):
        return person("behoerdliche_ermaechtigtetung", period)


class kontrollpersonal_zugelassen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kontrollpersonal erfuellt alle Anforderungen nach Art. 2 VSKV-ASTRA"
    reference = "SR 741.013.1 Art. 2"

    def formula(person, period, parameters):
        return (
            person("kontrollpersonal_fachkenntnisse", period) *
            person("kontrollpersonal_ermaechtigtet", period)
        )
