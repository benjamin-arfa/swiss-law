"""SR 952.0 Art. 37a, 37b (Einlagensicherung)

Generated from: ch/952/de/952.0.md

Privilegierte Einlagen und sofortige Auszahlung:
- Art. 37a: Privilegierte Einlagen bis max. CHF 100'000 pro Einleger
  und Bank bei Konkurs. Gelten als Forderungen der 2. Klasse.
- Art. 37b: Sofortige Auszahlung der privilegierten Einlagen ohne
  Abwarten des Kollokationsplans.
- Hinweis: Art. 1b Abs. 4 lit. d: Einlagensicherung gilt NICHT fuer
  Innovationsfoerderungsinstitute.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class bankg_einlage_bei_bank(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Einlage bei einer bestimmten Bank (CHF)"
    reference = "SR 952.0 Art. 37a"


class bankg_einleger_ist_natuerliche_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einleger ist natuerliche Person"
    reference = "SR 952.0 Art. 37a"


class bankg_bank_ist_innovationsfoerderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bank ist Innovationsfoerderungsinstitut nach Art. 1b"
    reference = "SR 952.0 Art. 1b Abs. 4 lit. d"


class bankg_privilegierte_einlage(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag der privilegierten Einlage bei Bankkonkurs (CHF)"
    reference = "SR 952.0 Art. 37a"

    def formula_2023(person, period, parameters):
        import numpy as np

        einlage = person('bankg_einlage_bei_bank', period)
        innovationsfoerderung = person('bankg_bank_ist_innovationsfoerderung', period)

        p = parameters(period).sr952_0
        max_privileg = p.privilegierte_einlage_max  # 100'000

        # Art. 1b Abs. 4 lit. d: keine Privilegierung bei Innovationsfoerderung
        privileg = np.where(
            innovationsfoerderung,
            0.0,
            np.minimum(einlage, max_privileg)
        )
        return privileg


class bankg_anspruch_sofortige_auszahlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf sofortige Auszahlung privilegierter Einlage"
    reference = "SR 952.0 Art. 37b"

    def formula_2023(person, period, parameters):
        import numpy as np

        privileg = person('bankg_privilegierte_einlage', period)
        innovationsfoerderung = person('bankg_bank_ist_innovationsfoerderung', period)

        return (privileg > 0) * np.logical_not(innovationsfoerderung)
