"""SR 810.211 Art. 12

Generated from: ch/810/de/810.211.md

Art. 12: Aufwandersatz fuer Lebendspender.

Als anderer Aufwand, der nach Art. 14 Abs. 2 Bst. b des
Transplantationsgesetzes zu ersetzen ist, gelten alle ausgewiesenen
Kosten im Zusammenhang mit der Entnahme, namentlich:
  a. Reisekosten
  b. Kosten der Abklaerungen betreffend Eignung als Spender/in
  c. (aufgehoben)
  d. Kosten fuer notwendige entgeltliche Hilfen (Haushalt, Betreuung)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class reisekosten_lebendspende(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Ausgewiesene Reisekosten im Zusammenhang mit der Lebendspende (CHF)"
    reference = "SR 810.211 Art. 12 lit. a"


class abklaerungskosten_lebendspende(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kosten der Abklaerungen betreffend Eignung als Spender/in (CHF)"
    reference = "SR 810.211 Art. 12 lit. b"


class kosten_entgeltliche_hilfen_lebendspende(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kosten fuer notwendige entgeltliche Hilfen (Haushalt, Betreuung) (CHF)"
    reference = "SR 810.211 Art. 12 lit. d"


class aufwandersatz_lebendspende_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamter Aufwandersatz fuer Lebendspende nach Art. 12 (CHF)"
    reference = "SR 810.211 Art. 12"

    def formula(person, period, parameters):
        reise = person('reisekosten_lebendspende', period)
        abklaerung = person('abklaerungskosten_lebendspende', period)
        hilfen = person('kosten_entgeltliche_hilfen_lebendspende', period)
        return reise + abklaerung + hilfen
