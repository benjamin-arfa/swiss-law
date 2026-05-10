"""SR 442.121.1 Art. 11

Generated from: ch/442/de/442.121.1.md

Hoechst- und Mindestansaetze der Beitraege:
- Betriebsbeitraege Museen/Sammlungen: max 30% Gesamtaufwand, min 150'000 CHF
- Projektbeitraege: max 50% Kosten, max 100'000 CHF, min 20'000 CHF
- Versicherungsbeitraege: max 50% Praemien, max 150'000 CHF, min 20'000 CHF
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesamtaufwand_museum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Gesamtaufwand des Museums oder der Sammlung (CHF)"
    reference = "SR 442.121.1 Art. 11 Bst. a"


class kosten_vorhaben_museum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte Kosten eines Vorhabens (CHF)"
    reference = "SR 442.121.1 Art. 11 Bst. b"


class versicherungspraemien_ausstellung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte Versicherungspraemien einer Ausstellung (CHF)"
    reference = "SR 442.121.1 Art. 11 Bst. c"


class betriebsbeitrag_museum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betriebsbeitrag an Museum/Sammlung (max 30% Aufwand, min 150'000 CHF)"
    reference = "SR 442.121.1 Art. 11 Bst. a"

    def formula(person, period, parameters):
        aufwand = person('gesamtaufwand_museum', period)
        max_beitrag = aufwand * 0.30
        # Minimum 150'000 CHF - wenn max_beitrag unter 150k, kein Beitrag moeglich
        return max_beitrag * (max_beitrag >= 150000)


class projektbeitrag_museum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Projektbeitrag (max 50% Kosten, max 100'000, min 20'000 CHF)"
    reference = "SR 442.121.1 Art. 11 Bst. b"

    def formula(person, period, parameters):
        kosten = person('kosten_vorhaben_museum', period)
        import numpy as np
        beitrag = np.minimum(kosten * 0.50, 100000)
        return beitrag * (beitrag >= 20000)


class versicherungsbeitrag_museum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherungsbeitrag (max 50% Praemien, max 150'000, min 20'000 CHF)"
    reference = "SR 442.121.1 Art. 11 Bst. c"

    def formula(person, period, parameters):
        praemien = person('versicherungspraemien_ausstellung', period)
        import numpy as np
        beitrag = np.minimum(praemien * 0.50, 150000)
        return beitrag * (beitrag >= 20000)
