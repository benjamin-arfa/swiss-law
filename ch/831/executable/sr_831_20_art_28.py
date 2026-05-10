"""SR 831.20 Art. 28

Generated from: ch/831/de/831.20.md

Art. 28: Grundsatz - Entitlement to a pension requires:
a. inability to restore/maintain/improve earning capacity through reasonable
   integration measures
b. average incapacity to work of at least 40% during one year without
   significant interruption
c. at least 40% disability after expiry of that year
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_eingliederung_ausgeschoepft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Eingliederungsmassnahmen koennen Erwerbsfaehigkeit nicht wiederherstellen, "
        "erhalten oder verbessern (Art. 28 Abs. 1 Bst. a IVG)"
    )
    reference = "SR 831.20 Art. 28 Abs. 1 Bst. a"


class iv_arbeitsunfaehigkeit_ein_jahr_mindestens_40(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Waehrend eines Jahres ohne wesentlichen Unterbruch durchschnittlich "
        "mindestens 40% arbeitsunfaehig gewesen (Art. 28 Abs. 1 Bst. b IVG)"
    )
    reference = "SR 831.20 Art. 28 Abs. 1 Bst. b"


class iv_invaliditaetsgrad_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Invaliditaetsgrad in Prozent (0-100)"
    reference = "SR 831.20 Art. 28 Abs. 1 Bst. c"


class iv_rentenanspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf IV-Rente nach Art. 28 IVG"
    reference = "SR 831.20 Art. 28"

    def formula(person, period, parameters):
        eingliederung = person('iv_eingliederung_ausgeschoepft', period)
        wartezeit = person('iv_arbeitsunfaehigkeit_ein_jahr_mindestens_40', period)
        iv_grad = person('iv_invaliditaetsgrad_prozent', period.this_year)
        # All three conditions must be met, and IV degree >= 40%
        return eingliederung * wartezeit * (iv_grad >= 40)
