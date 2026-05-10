"""SR 919.118 Art. 10a

Generated from: ch/919/de/919.118.md

Reduktionsziel fuer Stickstoff- und Phosphorverluste.

Im Vergleich zum Mittelwert der Jahre 2014-2016 werden bis zum Jahr 2030
die Verluste wie folgt reduziert:
  a. Stickstoff: um mindestens 15 Prozent
  b. Phosphor: um mindestens 20 Prozent
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stickstoff_verlust_aktuell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aktuelle Stickstoffverluste in der Landwirtschaft (Tonnen)"
    reference = "SR 919.118 Art. 10a Bst. a"


class phosphor_verlust_aktuell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aktuelle Phosphorverluste in der Landwirtschaft (Tonnen)"
    reference = "SR 919.118 Art. 10a Bst. b"


class stickstoff_reduktionsziel_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Stickstoff-Reduktionsziel (mind. 15% ggue. 2014-2016) erreicht ist"
    reference = "SR 919.118 Art. 10a Bst. a"

    def formula(person, period, parameters):
        verlust_aktuell = person('stickstoff_verlust_aktuell', period)
        basis = parameters(period).sr_919_118.stickstoff_verlust_basis_2014_2016
        mindest_reduktion = parameters(period).sr_919_118.stickstoff_reduktion_mindestens
        zielwert = basis * (1 - mindest_reduktion)
        return verlust_aktuell <= zielwert


class phosphor_reduktionsziel_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Phosphor-Reduktionsziel (mind. 20% ggue. 2014-2016) erreicht ist"
    reference = "SR 919.118 Art. 10a Bst. b"

    def formula(person, period, parameters):
        verlust_aktuell = person('phosphor_verlust_aktuell', period)
        basis = parameters(period).sr_919_118.phosphor_verlust_basis_2014_2016
        mindest_reduktion = parameters(period).sr_919_118.phosphor_reduktion_mindestens
        zielwert = basis * (1 - mindest_reduktion)
        return verlust_aktuell <= zielwert


class naehrstoff_reduktionsziele_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob beide Naehrstoff-Reduktionsziele (N und P) erreicht sind"
    reference = "SR 919.118 Art. 10a"

    def formula(person, period, parameters):
        n_ok = person('stickstoff_reduktionsziel_erreicht', period)
        p_ok = person('phosphor_reduktionsziel_erreicht', period)
        return n_ok * p_ok
