"""SR 837.0 Art. 8

Generated from: ch/837/de/837.0.md

Art. 8: Anspruchsvoraussetzungen - The insured person is entitled to
unemployment benefits if ALL of the following conditions are met:
a. wholly or partially unemployed (Art. 10)
b. has suffered a countable loss of work (Art. 11)
c. resides in Switzerland (Art. 12)
d. has completed compulsory schooling and has not yet reached the
   reference age under Art. 21(1) AHVG
e. has fulfilled the contribution period or is exempt (Art. 13, 14)
f. is available for placement (Art. 15)
g. fulfils the control requirements (Art. 17)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_ganz_oder_teilweise_arbeitslos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ganz oder teilweise arbeitslos (Art. 10 AVIG)"
    reference = "SR 837.0 Art. 8 Abs. 1 Bst. a"


class alv_anrechenbarer_arbeitsausfall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anrechenbarer Arbeitsausfall erlitten (Art. 11 AVIG)"
    reference = "SR 837.0 Art. 8 Abs. 1 Bst. b"


class alv_wohnsitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Wohnsitz in der Schweiz (Art. 12 AVIG)"
    reference = "SR 837.0 Art. 8 Abs. 1 Bst. c"


class alv_schulpflicht_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Obligatorische Schulzeit zurueckgelegt"
    reference = "SR 837.0 Art. 8 Abs. 1 Bst. d"


class alv_referenzalter_nicht_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Referenzalter nach Art. 21 Abs. 1 AHVG noch nicht erreicht"
    reference = "SR 837.0 Art. 8 Abs. 1 Bst. d"


class alv_beitragszeit_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beitragszeit erfuellt oder davon befreit (Art. 13/14 AVIG)"
    reference = "SR 837.0 Art. 8 Abs. 1 Bst. e"


class alv_vermittlungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vermittlungsfaehig (Art. 15 AVIG)"
    reference = "SR 837.0 Art. 8 Abs. 1 Bst. f"


class alv_kontrollvorschriften_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kontrollvorschriften erfuellt (Art. 17 AVIG)"
    reference = "SR 837.0 Art. 8 Abs. 1 Bst. g"


class alv_anspruch_arbeitslosenentschaedigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Arbeitslosenentschaedigung nach Art. 8 AVIG"
    reference = "SR 837.0 Art. 8"

    def formula(person, period, parameters):
        arbeitslos = person('alv_ganz_oder_teilweise_arbeitslos', period)
        arbeitsausfall = person('alv_anrechenbarer_arbeitsausfall', period)
        wohnsitz = person('alv_wohnsitz_schweiz', period)
        schulpflicht = person('alv_schulpflicht_erfuellt', period)
        alter_ok = person('alv_referenzalter_nicht_erreicht', period)
        beitragszeit = person('alv_beitragszeit_erfuellt', period)
        vermittlung = person('alv_vermittlungsfaehig', period)
        kontrolle = person('alv_kontrollvorschriften_erfuellt', period)

        return (
            arbeitslos
            * arbeitsausfall
            * wohnsitz
            * schulpflicht
            * alter_ok
            * beitragszeit
            * vermittlung
            * kontrolle
        )
