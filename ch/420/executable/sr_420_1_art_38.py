"""SR 420.1 Art. 38

Generated from: ch/420/de/420.1.md

Rueckforderung bei Pflichtverletzung - Verjaehrungsfristen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rueckforderung_kenntnis_datum_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre seit Kenntnis der unrechtmaessigen Auszahlung"
    reference = "SR 420.1 Art. 38 Abs. 2"


class rueckforderung_entstehung_datum_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre seit Entstehung des Rueckforderungsanspruchs"
    reference = "SR 420.1 Art. 38 Abs. 2"


class empfaenger_hat_strafbare_handlung_begangen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Empfaenger hat durch sein Verhalten eine strafbare Handlung begangen"
    reference = "SR 420.1 Art. 38 Abs. 2bis"


class strafrechtliche_verfolgungsverjaehrung_eingetreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strafrechtliche Verfolgungsverjaehrung ist eingetreten"
    reference = "SR 420.1 Art. 38 Abs. 2bis"


class erstinstanzliches_strafurteil_eroeffnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erstinstanzliches Strafurteil wurde eroeffnet"
    reference = "SR 420.1 Art. 38 Abs. 2bis"


class jahre_seit_strafurteil(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre seit Eroeffnung des erstinstanzlichen Strafurteils"
    reference = "SR 420.1 Art. 38 Abs. 2bis"


class rueckforderungsanspruch_verjaehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rueckforderungsanspruch ist verjaehrt"
    reference = "SR 420.1 Art. 38 Abs. 2"

    def formula(person, period, parameters):
        kenntnis_jahre = person('rueckforderung_kenntnis_datum_jahre', period)
        entstehung_jahre = person('rueckforderung_entstehung_datum_jahre', period)
        strafbar = person('empfaenger_hat_strafbare_handlung_begangen', period)

        # Regulaere Verjaehrung: 3 Jahre ab Kenntnis, absolut 10 Jahre
        regulaer_verjaehrt = (kenntnis_jahre >= 3) + (entstehung_jahre >= 10)

        # Bei strafbarer Handlung: verjaehrt fruehestens mit strafrechtlicher Verfolgungsverjaehrung
        straf_verjaehrung = person('strafrechtliche_verfolgungsverjaehrung_eingetreten', period)
        strafurteil = person('erstinstanzliches_strafurteil_eroeffnet', period)
        jahre_urteil = person('jahre_seit_strafurteil', period)

        # Falls Strafurteil: verjaehrt fruehestens 3 Jahre nach Eroeffnung
        straf_verjaehrt = straf_verjaehrung + strafurteil * (jahre_urteil >= 3)

        return where(
            strafbar,
            regulaer_verjaehrt * straf_verjaehrt,
            regulaer_verjaehrt
        )
