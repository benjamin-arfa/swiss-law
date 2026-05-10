"""SR 944.0 Art. 5

Generated from: ch/944/de/944.0.md

Finanzhilfe an Konsumentenorganisationen:
- Höchstens 50% der anrechenbaren Kosten
- Gilt für Organisationen von gesamtschweizerischer Bedeutung
- Ausschliesslich dem Konsumentenschutz gewidmet (statutengemäss)
- Finanzhilfe für: Information, vergleichende Tests, Deklarationsvereinbarungen
- Auch für andere Organisationen (Art. 5 Abs. 2) wenn gesamtschweizerisch bedeutend
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_konsumentenorganisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Konsumentenorganisation von gesamtschweizerischer Bedeutung handelt"
    reference = "SR 944.0 Art. 5 Abs. 1"


class widmet_sich_ausschliesslich_konsumentenschutz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation sich statutengemäss ausschliesslich dem Konsumentenschutz widmet"
    reference = "SR 944.0 Art. 5 Abs. 1"


class anrechenbare_kosten_konsumentenorg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Kosten der Konsumentenorganisation"
    reference = "SR 944.0 Art. 5 Abs. 1"


class finanzhilfe_konsumentenorg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzhilfe des Bundes an Konsumentenorganisationen"
    reference = "SR 944.0 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        ist_org = person('ist_konsumentenorganisation', period)
        widmet = person('widmet_sich_ausschliesslich_konsumentenschutz', period)
        kosten = person('anrechenbare_kosten_konsumentenorg', period)
        max_anteil = parameters(period).sr_944_0.finanzhilfe_max_anteil

        berechtigt = ist_org * widmet
        return np.where(berechtigt, kosten * max_anteil, 0)
