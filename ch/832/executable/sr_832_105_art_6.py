"""SR 832.105 Art. 6-7

Generated from: ch/fr/832/832.105.md

Art. 6: Etendue des donnees (Umfang der Gesundheitsdaten)
- Abs. 1: Health professionals may store on card (with patient consent):
  blood group, immune system, transplant, allergies, diseases/accident sequelae,
  medication, emergency contacts, advance directives.
Art. 7: Acces aux donnees (Zugang zu den Daten)
- Abs. 3: Access only with insured person's consent.
- Abs. 4: Person may lock data with PIN.
- Abs. 5: Emergency access without consent when urgent care required.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kvg_gesundheitsdaten_auf_karte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = False
    label = "Ob Gesundheitsdaten auf der Versichertenkarte gespeichert sind"
    reference = "SR 832.105 Art. 6 Abs. 1"


class kvg_versicherte_einwilligung_gesundheitsdaten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = False
    label = "Ob die versicherte Person der Speicherung von Gesundheitsdaten zugestimmt hat"
    reference = "SR 832.105 Art. 6 Abs. 1"


class kvg_daten_mit_pin_gesperrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = False
    label = "Ob die Gesundheitsdaten mit einem PIN gesperrt sind"
    reference = "SR 832.105 Art. 7 Abs. 4"


class kvg_notfallsituation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = False
    label = "Ob ein Notfall vorliegt und der Versicherte nicht einwilligen kann"
    reference = "SR 832.105 Art. 7 Abs. 5"


class kvg_zugang_gesundheitsdaten_erlaubt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Zugang zu den Gesundheitsdaten auf der Karte erlaubt ist"
    reference = "SR 832.105 Art. 7"

    def formula(person, period, parameters):
        daten_vorhanden = person('kvg_gesundheitsdaten_auf_karte', period)
        einwilligung = person('kvg_versicherte_einwilligung_gesundheitsdaten', period)
        notfall = person('kvg_notfallsituation', period)

        # Access allowed if: data exists AND (consent OR emergency)
        return daten_vorhanden * (einwilligung + notfall)
