"""SR 231.11 Art. 16b

Generated from: ch/231/de/231.11.md

Zahlungspflicht: Die Verwertungsgesellschaft, die den Tarif vorlegt,
muss Gebuehren und Auslagen bezahlen. Bei mehreren: solidarische Haftung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_tarifvorlegende_verwertungsgesellschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verwertungsgesellschaft den Tarif zur Genehmigung vorlegt"
    reference = "SR 231.11 Art. 16b Abs. 1"


class anzahl_zahlungspflichtige_verwertungsgesellschaften(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl solidarisch zahlungspflichtiger Verwertungsgesellschaften"
    reference = "SR 231.11 Art. 16b Abs. 2"


class solidarische_haftung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob solidarische Haftung fuer Gebuehren und Auslagen besteht"
    reference = "SR 231.11 Art. 16b Abs. 2"

    def formula(person, period, parameters):
        return person('anzahl_zahlungspflichtige_verwertungsgesellschaften', period) > 1


class nutzerverband_kostenanteil(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob einem Nutzerverband ein Teil der Kosten auferlegt wird (begruendete Faelle)"
    reference = "SR 231.11 Art. 16b Abs. 3"
