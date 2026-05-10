"""SR 416.211 Art. 4

Generated from: ch/416/de/416.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_buerger_in_ausserhalb_eu_efta(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Buerger/in eines Landes ausserhalb der EU und der EFTA"
    reference = "SR 416.211 Art. 4 Abs. 1"


class ist_stipendiat_in(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Stipendiat/in des Bundes"
    reference = "SR 416.211 Art. 4 Abs. 1"


class rueckflug_ist_endgueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Rueckflug ist endgueltig (keine Rueckkehr geplant)"
    reference = "SR 416.211 Art. 4 Abs. 1"


class rueckflug_in_herkunftsland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rueckflug erfolgt in das Herkunftsland"
    reference = "SR 416.211 Art. 4 Abs. 2"


class rueckreise_innerhalb_sechs_monate_nach_stipendienende(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rueckreise wird spaetestens 6 Monate nach Ende des Stipendiums angetreten"
    reference = "SR 416.211 Art. 4 Abs. 3"


class schriftliches_gesuch_eingereicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schriftliches Gesuch mit Kopie des Flugscheins und Zahlungsquittung beim SBFI eingereicht"
    reference = "SR 416.211 Art. 4 Abs. 4"


class anspruch_zulage_rueckflug(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf einmalige Zulage (Pauschale) fuer den endgueltigen Rueckflug"
    reference = "SR 416.211 Art. 4"

    def formula(person, period, parameters):
        ist_stipendiat = person('ist_stipendiat_in', period)
        ausserhalb_eu_efta = person('ist_buerger_in_ausserhalb_eu_efta', period)
        endgueltig = person('rueckflug_ist_endgueltig', period)
        herkunftsland = person('rueckflug_in_herkunftsland', period)
        innerhalb_frist = person('rueckreise_innerhalb_sechs_monate_nach_stipendienende', period)
        gesuch = person('schriftliches_gesuch_eingereicht', period)
        return (ist_stipendiat * ausserhalb_eu_efta * endgueltig *
                herkunftsland * innerhalb_frist * gesuch)
