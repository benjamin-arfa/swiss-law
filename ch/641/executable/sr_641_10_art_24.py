"""SR 641.10 Art. 24

Generated from: ch/641/de/641.10.md

Abgabe auf Versicherungspraemien:
1. Die Abgabe betraegt 5 Prozent der Barpraemie.
   Fuer die Lebensversicherung betraegt sie 2,5 Prozent der Barpraemie.
2. Steuerpflichtige muessen in ihren Buechern steuerbare und befreite
   Praemien gesondert ausweisen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stg_versicherungspraemie_bar(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Barpraemie fuer Versicherung (CHF)"
    reference = "SR 641.10 Art. 24 Abs. 1"


class stg_ist_lebensversicherung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um eine (steuerbare) Lebensversicherung handelt"
    reference = "SR 641.10 Art. 24 Abs. 1"


class stg_versicherungspraemie_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Versicherungspraemie von der Abgabe befreit ist (Art. 22)"
    reference = "SR 641.10 Art. 22"


class stg_praemienabgabe_satz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anwendbarer Abgabesatz auf Versicherungspraemien"
    reference = "SR 641.10 Art. 24 Abs. 1"

    def formula(person, period, parameters):
        ist_leben = person('stg_ist_lebensversicherung', period)
        satz_allgemein = parameters(period).sr_641_10.praemienabgabe_satz_allgemein
        satz_leben = parameters(period).sr_641_10.praemienabgabe_satz_leben
        return where(ist_leben, satz_leben, satz_allgemein)


class stg_praemienabgabe_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag der Abgabe auf Versicherungspraemien (CHF)"
    reference = "SR 641.10 Art. 24"

    def formula(person, period, parameters):
        praemie = person('stg_versicherungspraemie_bar', period)
        satz = person('stg_praemienabgabe_satz', period)
        befreit = person('stg_versicherungspraemie_befreit', period)
        return where(befreit, 0, praemie * satz)
