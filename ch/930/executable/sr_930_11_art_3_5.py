"""SR 930.11 Art. 3-5

Generated from: ch/930/de/930.11.md

Art. 3: Grundsätze - Principles for placing products on market:
- Products must not endanger safety/health (or only minimally) when used normally
- Must meet basic safety/health requirements (Art. 4) or state of the art
- Factors: durability, interaction with other products, consumer use, vulnerable groups
- Labeling, packaging, instructions, warnings must match risk potential

Art. 5: Erfüllung der Anforderungen - Meeting requirements:
- Manufacturer must prove conformity with requirements
- Products made per Art. 6 technical standards: presumption of conformity
- Non-standard products: must prove alternative compliance
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class prsg_produkt_gefaehrdet_sicherheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produkt gefährdet die Sicherheit oder Gesundheit bei normaler/vorhersehbarer Verwendung"
    reference = "SR 930.11 Art. 3 Abs. 1"


class prsg_erfuellt_sicherheitsanforderungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produkt erfüllt die grundlegenden Sicherheits- und Gesundheitsanforderungen"
    reference = "SR 930.11 Art. 3 Abs. 2"


class prsg_fuer_konsumenten_bestimmt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produkt ist für Konsumenten bestimmt oder kann von Konsumenten benutzt werden"
    reference = "SR 930.11 Art. 3 Abs. 3 Bst. c"


class prsg_fuer_vulnerable_gruppe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produkt kann von Personengruppen mit grösserem Risiko verwendet werden (Kinder, Behinderte, Ältere)"
    reference = "SR 930.11 Art. 3 Abs. 3 Bst. d"


class prsg_kennzeichnung_angemessen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kennzeichnung, Verpackung, Anleitungen und Warnhinweise entsprechen dem Gefährdungspotenzial"
    reference = "SR 930.11 Art. 3 Abs. 4"


class prsg_nach_technischer_norm_hergestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produkt wurde nach technischen Normen gemäss Art. 6 hergestellt"
    reference = "SR 930.11 Art. 5 Abs. 2"


class prsg_konformitaet_vermutet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Konformität mit Sicherheitsanforderungen wird vermutet (Konformitätsvermutung)"
    reference = "SR 930.11 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        nach_norm = person('prsg_nach_technischer_norm_hergestellt', period)
        return nach_norm


class prsg_inverkehrbringen_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Inverkehrbringen des Produkts ist zulässig"
    reference = "SR 930.11 Art. 3"

    def formula(person, period, parameters):
        im_bereich = person('prsg_im_geltungsbereich', period)
        nicht_gefaehrlich = 1 - person('prsg_produkt_gefaehrdet_sicherheit', period)
        sicherheit_ok = person('prsg_erfuellt_sicherheitsanforderungen', period)
        kennzeichnung = person('prsg_kennzeichnung_angemessen', period)
        return im_bereich * nicht_gefaehrlich * sicherheit_ok * kennzeichnung
