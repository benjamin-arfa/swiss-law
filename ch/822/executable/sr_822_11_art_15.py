"""SR 822.11 Art. 15

Generated from: ch/822/de/822.11.md

Art. 15: Pausen
- Abs. 1: Mindestpausen:
  a. 15 Minuten bei mehr als 5.5 Stunden taeglicher Arbeitszeit
  b. 30 Minuten bei mehr als 7 Stunden taeglicher Arbeitszeit
  c. 60 Minuten bei mehr als 9 Stunden taeglicher Arbeitszeit
- Abs. 2: Pausen gelten als Arbeitszeit wenn AN Arbeitsplatz nicht
  verlassen duerfen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arg_taegliche_arbeitszeit_netto_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegliche Arbeitszeit ohne Pausen in Stunden"
    reference = "SR 822.11 Art. 15 Abs. 1"


class arg_mindestpause_minuten(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesetzliche Mindestpause in Minuten"
    reference = "SR 822.11 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        arbeitszeit = person('arg_taegliche_arbeitszeit_netto_stunden', period)
        # > 9h -> 60min; > 7h -> 30min; > 5.5h -> 15min; else 0
        return (
            where(arbeitszeit > 9.0, 60,
            where(arbeitszeit > 7.0, 30,
            where(arbeitszeit > 5.5, 15, 0)))
        )


class arg_arbeitsplatz_verlassen_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Arbeitnehmer darf waehrend Pausen den Arbeitsplatz nicht verlassen"
    reference = "SR 822.11 Art. 15 Abs. 2"


class arg_pausen_als_arbeitszeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Pausen gelten als Arbeitszeit"
    reference = "SR 822.11 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        return person('arg_arbeitsplatz_verlassen_verboten', period)
