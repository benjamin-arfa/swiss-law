"""SR 128.41 Art. 19

Generated from: ch/128/de/128.41.md

Internationale Betriebssicherheitsbescheinigung: Fee of CHF 100 for
issuance. Additional time-based fee of CHF 100-400/hour if a full
operational security procedure is needed first.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class internationale_bescheinigung_beantragt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine internationale Betriebssicherheitsbescheinigung beantragt wurde"
    reference = "SR 128.41 Art. 19 Abs. 1"


class betriebssicherheitsverfahren_erforderlich_fuer_bescheinigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob zuerst ein Betriebssicherheitsverfahren durchgefuehrt werden muss"
    reference = "SR 128.41 Art. 19 Abs. 2"


class grundgebuehr_bescheinigung_chf(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Grundgebuehr fuer die internationale Betriebssicherheitsbescheinigung in CHF"
    reference = "SR 128.41 Art. 19 Abs. 1"
    default_value = 100
