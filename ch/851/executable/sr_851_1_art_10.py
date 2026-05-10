"""SR 851.1 Art. 10

Generated from: ch/851/de/851.1.md

Art. 10: Verbot der Abschiebung
- Abs. 1: Behoerden duerfen einen Beduerftigen nicht veranlassen, aus dem
  Wohnkanton wegzuziehen, es sei denn es liegt in seinem Interesse.
- Abs. 2: Bei Widerhandlung bleibt der Unterstuetzungswohnsitz am bisherigen
  Wohnort bestehen, laengstens 5 Jahre.
- Abs. 3: Auslaenderrechtliche Bestimmungen bleiben vorbehalten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zug_abschiebung_durch_behoerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Behoerden haben den Wegzug des Beduerftigen aus dem Wohnkanton veranlasst"
    reference = "SR 851.1 Art. 10 Abs. 1"


class zug_wegzug_im_interesse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Wegzug liegt im Interesse des Beduerftigen"
    reference = "SR 851.1 Art. 10 Abs. 1"


class zug_abschiebeverbot_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Abschiebeverbot wurde verletzt (behördlicher Wegzug ohne Interesse des Beduerftigen)"
    reference = "SR 851.1 Art. 10 Abs. 1-2"

    def formula(person, period, parameters):
        abschiebung = person('zug_abschiebung_durch_behoerde', period)
        im_interesse = person('zug_wegzug_im_interesse', period)
        return abschiebung * (1 - im_interesse)


class zug_wohnsitz_fortbestand_max_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Dauer des Fortbestands des Unterstuetzungswohnsitzes bei Abschiebeverbot-Verletzung (Jahre)"
    reference = "SR 851.1 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        return parameters(period).zug.fortbestand_wohnsitz_max_jahre
