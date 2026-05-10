"""SR 832.105 Art. 3-4

Generated from: ch/fr/832/832.105.md

Art. 3: Donnees imprimees (Aufgedruckte Daten)
- Abs. 1: Printed on card: name, AHV number, birth date, sex,
  insurer name/ID, card ID, expiry date.
- Abs. 2: European health insurance card data may also be printed on back.
Art. 4: Donnees electroniques (Elektronische Daten)
- Abs. 1: Data from Art. 3(1) must also be stored electronically.
- Abs. 2: May also store: address, insurer billing address, special insurance forms,
  accident suspension, supplementary insurance (with consent), EHIC data.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kvg_karte_name_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = True
    label = "Ob Name und Vorname auf der Versichertenkarte vorhanden sind"
    reference = "SR 832.105 Art. 3 Abs. 1 Bst. a"


class kvg_karte_ahv_nummer_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = True
    label = "Ob die AHV-Nummer auf der Versichertenkarte vorhanden ist"
    reference = "SR 832.105 Art. 3 Abs. 1 Bst. b"


class kvg_karte_geburtsdatum_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = True
    label = "Ob das Geburtsdatum auf der Versichertenkarte vorhanden ist"
    reference = "SR 832.105 Art. 3 Abs. 1 Bst. c"


class kvg_karte_pflichtdaten_komplett(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Pflichtdaten auf der Versichertenkarte vorhanden sind"
    reference = "SR 832.105 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        name = person('kvg_karte_name_vorhanden', period)
        ahv = person('kvg_karte_ahv_nummer_vorhanden', period)
        geburt = person('kvg_karte_geburtsdatum_vorhanden', period)
        return name * ahv * geburt


class kvg_ehic_daten_auf_rueckseite(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = False
    label = "Ob EHIC-Daten auf der Rueckseite der Karte aufgedruckt sind"
    reference = "SR 832.105 Art. 3 Abs. 2"
