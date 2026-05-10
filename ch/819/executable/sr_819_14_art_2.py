"""SR 819.14 Art. 2

Generated from: ch/819/de/819.14.md

Art. 2 Voraussetzungen fuer das Inverkehrbringen:
1. Machinery may only be placed on the market if:
   a. it does not endanger safety/health of persons when properly installed,
      maintained, and used as intended or reasonably foreseeable;
   b. requirements of EU Machinery Directive Art. 5(1)(a-e), (2), (3),
      Art. 12 and Art. 13 are met;
   c. an economic operator fulfills obligations per EU Market Surveillance
      Regulation Art. 4(2) and Art. 4a.
2. Commissioning is equivalent to placing on market if no prior placing occurred.
3. For demonstrations at fairs/exhibitions: EU Machinery Directive Art. 6(3) applies.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class maschv_maschine_sicher(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Maschine bei bestimmungsgemaesser Verwendung sicher ist"
    reference = "SR 819.14 Art. 2 Abs. 1 Bst. a"


class maschv_konformitaetsanforderungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Konformitaetsanforderungen der EU-Maschinenrichtlinie erfuellt sind"
    reference = "SR 819.14 Art. 2 Abs. 1 Bst. b"


class maschv_wirtschaftsakteur_pflichten_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Wirtschaftsakteur seine Pflichten nach Art. 4a erfuellt"
    reference = "SR 819.14 Art. 2 Abs. 1 Bst. c"


class maschv_inverkehrbringen_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Maschine in Verkehr gebracht werden darf"
    reference = "SR 819.14 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        sicher = person('maschv_maschine_sicher', period)
        konform = person('maschv_konformitaetsanforderungen_erfuellt', period)
        pflichten = person('maschv_wirtschaftsakteur_pflichten_erfuellt', period)
        return sicher * konform * pflichten


class maschv_inbetriebnahme_gleichgestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Inbetriebnahme dem Inverkehrbringen gleichgestellt ist"
    reference = "SR 819.14 Art. 2 Abs. 2"


class maschv_kein_vorheriges_inverkehrbringen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob zuvor kein Inverkehrbringen stattgefunden hat"
    reference = "SR 819.14 Art. 2 Abs. 2"
