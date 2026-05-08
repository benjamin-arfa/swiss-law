"""SR 813.1 Art. 10

Generated from: ch/813/de/813.1.md

Zulassung fuer Biozidprodukte: Ein Biozidprodukt wird zugelassen, wenn es
hinreichend wirksam ist und keine unannehmbaren Nebenwirkungen hat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class biozid_hinreichend_wirksam(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Biozidprodukt bei vorgesehener Verwendung hinreichend wirksam ist"
    reference = "SR 813.1 Art. 10 Abs. 2 Bst. a"


class biozid_keine_unannehmbaren_nebenwirkungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Biozidprodukt keine unannehmbaren Nebenwirkungen auf die Gesundheit hat"
    reference = "SR 813.1 Art. 10 Abs. 2 Bst. b"


class biozid_alternative_mit_geringerem_risiko(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein anderer Wirkstoff mit erheblich geringerem Risiko zugelassen ist (Verweigerungsgrund)"
    reference = "SR 813.1 Art. 10 Abs. 3"


class biozid_zulassung_erteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Zulassung fuer das Biozidprodukt erteilt wird"
    reference = "SR 813.1 Art. 10"

    def formula(person, period, parameters):
        wirksam = person('biozid_hinreichend_wirksam', period)
        keine_nebenwirkungen = person('biozid_keine_unannehmbaren_nebenwirkungen', period)
        alternative = person('biozid_alternative_mit_geringerem_risiko', period)
        return wirksam * keine_nebenwirkungen * (1 - alternative)
