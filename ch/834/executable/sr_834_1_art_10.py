"""SR 834.1 Art. 10

Generated from: ch/834/de/834.1.md

Grundentschaedigung waehrend der anderen Dienste:
- Abs. 1: Taegl. Grundentschaedigung = 80% des durchschnittlichen
  vordienstlichen Erwerbseinkommens. Vorbehalten bleibt Art. 16 Abs. 1-3.
- Abs. 2: Nicht erwerbstaetig vor Dienst -> Mindestbetraege nach Art. 16 Abs. 1-3.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class eo_vordienstliches_erwerbseinkommen_taeglich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Durchschnittliches vordienstliches Erwerbseinkommen pro Tag (CHF)"
    reference = "SR 834.1 Art. 11"


class eo_war_vor_dienst_erwerbstaetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person war vor Dienstbeginn erwerbstaetig"
    reference = "SR 834.1 Art. 10 Abs. 2"


class eo_grundentschaedigung_andere_dienste(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegl. Grundentschaedigung waehrend anderer Dienste (CHF)"
    reference = "SR 834.1 Art. 10"

    def formula_2005(person, period, parameters):
        import numpy as np

        einkommen = person('eo_vordienstliches_erwerbseinkommen_taeglich', period)
        erwerbstaetig = person('eo_war_vor_dienst_erwerbstaetig', period)

        p = parameters(period).sr834_1
        anteil = p.anteil_grundentschaedigung_andere_dienste  # 0.80

        grundentschaedigung = einkommen * anteil

        # Abs. 2: Mindestbetraege fuer nicht Erwerbstaetige
        mindestbetrag = person('eo_mindestbetrag_gesamtentschaedigung', period)

        return np.where(erwerbstaetig, grundentschaedigung, mindestbetrag)
