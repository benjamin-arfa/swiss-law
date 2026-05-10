"""SR 362.2 Art. 11

Generated from: ch/362/de/362.2.md
Response deadlines for information exchange between Schengen states.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ersuchen_betrifft_straftat_anhang_1(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ersuchen betrifft eine Straftat nach Anhang 1 des SIaG"
    reference = "SR 362.2 Art. 11 Abs. 1"


class informationen_unmittelbar_verfuegbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Informationen sind durch Zugriff auf eine Datenbank unmittelbar verfuegbar"
    reference = "SR 362.2 Art. 11 Abs. 1"


class ersuchen_ist_dringend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es handelt sich um ein dringendes Ersuchen"
    reference = "SR 362.2 Art. 11 Abs. 1 lit. a"


class fristverlaengerung_begruendet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fristverlaengerung bei dringendem Ersuchen ist begruendet"
    reference = "SR 362.2 Art. 11 Abs. 2"


class antwortfrist_stunden(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Antwortfrist fuer Informationsersuchen in Stunden"
    reference = "SR 362.2 Art. 11"

    def formula(person, period):
        anhang_1 = person('ersuchen_betrifft_straftat_anhang_1', period)
        verfuegbar = person('informationen_unmittelbar_verfuegbar', period)
        dringend = person('ersuchen_ist_dringend', period)
        verlaengerung = person('fristverlaengerung_begruendet', period)

        # Standardfall: 14 Tage = 336 Stunden
        frist = 336

        # Spezialfall: Anhang-1-Straftat + sofort verfuegbar
        spezial = anhang_1 * verfuegbar

        # Dringend: 8 Stunden (oder 72 Stunden wenn begruendet verlaengert)
        frist_dringend = where(verlaengerung, 72, 8)

        # Nicht dringend: 7 Tage = 168 Stunden
        frist_nicht_dringend = 168

        frist_spezial = where(dringend, frist_dringend, frist_nicht_dringend)

        return where(spezial, frist_spezial, frist)
