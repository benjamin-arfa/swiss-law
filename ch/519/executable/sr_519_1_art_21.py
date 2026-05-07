"""SR 519.1 Art. 21

Generated from: ch/519/de/519.1.md

Art. 21 Andere Entschädigungen (Other compensation):
If personal property is damaged, stolen or lost during deployment without
the person's fault, the VBS may pay compensation up to CHF 5,000, provided
no military insurance, private insurance, or liable third party covers the damage.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class pvspa_sachschaden_ohne_verschulden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether personal property was damaged/stolen/lost without the person's fault"
    reference = "SR 519.1 Art. 21"


class pvspa_versicherung_deckt_schaden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether military/private insurance or liable third party covers the damage"
    reference = "SR 519.1 Art. 21"


class pvspa_schadensbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Amount of personal property damage (CHF)"
    reference = "SR 519.1 Art. 21"


class pvspa_entschaedigung_sachschaden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Compensation for personal property damage (CHF), max 5000"
    reference = "SR 519.1 Art. 21"

    def formula(person, period, parameters):
        schaden = person('pvspa_sachschaden_ohne_verschulden', period)
        versicherung = person('pvspa_versicherung_deckt_schaden', period)
        betrag = person('pvspa_schadensbetrag', period)

        max_entschaedigung = parameters(period).sr_519_1.max_entschaedigung_sachschaden
        anspruch = schaden * not_(versicherung)
        return where(anspruch, min_(betrag, max_entschaedigung), 0)
