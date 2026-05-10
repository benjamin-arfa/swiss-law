"""SR 832.105 Art. 9-10

Generated from: ch/fr/832/832.105.md

Art. 9: Droits de la personne assuree (Rechte der versicherten Person)
- Abs. 1: Right to be informed about data on card and have it corrected.
  Can have optional data deleted at any time.
- Abs. 2: May refuse to disclose health data without giving reasons.
Art. 10: Obligations de la personne assuree (Pflichten)
- Abs. 1: Must present card to provider when using services.
- Abs. 2: If not presented and causes extra costs, insurer may charge a fee.
- Abs. 3: Must return card when insurance ends or card expires.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR


class kvg_karte_vorgezeigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = True
    label = "Ob die Versichertenkarte beim Leistungsbezug vorgezeigt wurde"
    reference = "SR 832.105 Art. 10 Abs. 1"


class kvg_mehrkosten_ohne_karte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = False
    label = "Ob Mehrkosten entstanden sind, weil die Karte nicht vorgezeigt wurde"
    reference = "SR 832.105 Art. 10 Abs. 2"


class kvg_gebuehr_wegen_fehlender_karte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Versicherer eine Gebuehr wegen fehlender Karte erheben darf"
    reference = "SR 832.105 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        karte = person('kvg_karte_vorgezeigt', period)
        mehrkosten = person('kvg_mehrkosten_ohne_karte', period)
        return not_(karte) * mehrkosten
