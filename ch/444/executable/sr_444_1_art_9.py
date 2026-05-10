"""SR 444.1 Art. 9

Generated from: ch/444/de/444.1.md

Rueckfuehrungsklagen: Verjaehrung 1 Jahr ab Kenntnis, max 30 Jahre ab
rechtswidriger Ausfuhr. Gutglaeubiger Erwerber hat Anspruch auf Entschaedigung
(Kaufpreis + Aufwendungen). Retentionsrecht bis Bezahlung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_kenntnis_fundort(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit Kenntnis ueber Fundort und Besitzer des Kulturguts"
    reference = "SR 444.1 Art. 9 Abs. 4"


class jahre_seit_rechtswidriger_ausfuhr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit rechtswidriger Ausfuhr des Kulturguts"
    reference = "SR 444.1 Art. 9 Abs. 4"


class rueckfuehrungsklage_verjaehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Rueckfuehrungsklage verjaehrt ist"
    reference = "SR 444.1 Art. 9 Abs. 4"

    def formula(person, period, parameters):
        kenntnis = person('jahre_seit_kenntnis_fundort', period)
        ausfuhr = person('jahre_seit_rechtswidriger_ausfuhr', period)
        return (kenntnis > 1) + (ausfuhr > 30)


class kaufpreis_kulturgut(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kaufpreis des Kulturguts (CHF)"
    reference = "SR 444.1 Art. 9 Abs. 5"


class aufwendungen_bewahrung_kulturgut(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Notwendige und nuetzliche Aufwendungen zur Bewahrung (CHF)"
    reference = "SR 444.1 Art. 9 Abs. 5"


class gutglaeubig_erworben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Kulturgut in gutem Glauben erworben wurde"
    reference = "SR 444.1 Art. 9 Abs. 5"


class entschaedigung_rueckfuehrung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Entschaedigung bei Rueckfuehrung an gutglaeubigen Erwerber"
    reference = "SR 444.1 Art. 9 Abs. 5"

    def formula(person, period, parameters):
        kaufpreis = person('kaufpreis_kulturgut', period)
        aufwand = person('aufwendungen_bewahrung_kulturgut', period)
        gutglaeubig = person('gutglaeubig_erworben', period)
        return gutglaeubig * (kaufpreis + aufwand)
