"""SR 831.232.51 Art. 2

Generated from: ch/831/de/831.232.51.md

Art. 2: Anspruch auf Hilfsmittel - Entitlement to aids from IV.

Abs. 1: Entitlement exists for aids listed in the annex, insofar as
they are necessary for mobility, contact with the environment, or
self-care.

Abs. 2: Aids marked with (*) require necessity for employment, activity
in one's field, schooling, training, or functional habituation.

Abs. 3: Entitlement also extends to disability-related accessories
and adaptations.

Abs. 4: Only simple, appropriate, and economical aids. Additional
costs for other versions borne by the insured person.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hvi_hilfsmittel_fuer_fortbewegung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hilfsmittel notwendig fuer Fortbewegung"
    reference = "SR 831.232.51 Art. 2 Abs. 1"


class hvi_hilfsmittel_fuer_kontakt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hilfsmittel notwendig fuer Herstellung des Kontakts mit der Umwelt"
    reference = "SR 831.232.51 Art. 2 Abs. 1"


class hvi_hilfsmittel_fuer_selbstsorge(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hilfsmittel notwendig fuer Selbstsorge"
    reference = "SR 831.232.51 Art. 2 Abs. 1"


class hvi_hilfsmittel_fuer_erwerbstaetigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hilfsmittel notwendig fuer Ausuebung einer Erwerbstaetigkeit oder Ausbildung (mit *)"
    reference = "SR 831.232.51 Art. 2 Abs. 2"


class hvi_anspruch_hilfsmittel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Hilfsmittel der IV (Art. 2 HVI)"
    reference = "SR 831.232.51 Art. 2"

    def formula(person, period, parameters):
        fortbewegung = person('hvi_hilfsmittel_fuer_fortbewegung', period)
        kontakt = person('hvi_hilfsmittel_fuer_kontakt', period)
        selbstsorge = person('hvi_hilfsmittel_fuer_selbstsorge', period)
        # At least one necessity must be present
        return (fortbewegung + kontakt + selbstsorge) > 0
