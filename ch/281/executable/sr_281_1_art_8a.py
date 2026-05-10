"""SR 281.1 Art. 8a

Generated from: ch/281/de/281.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class interesse_an_einsicht_glaubhaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Interesse an Einsicht in Protokolle und Register ist glaubhaft gemacht"
    reference = "SR 281.1 Art. 8a Abs. 1"


class einsichtsgesuch_im_zusammenhang_mit_vertrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Auskunftsgesuch steht in unmittelbarem Zusammenhang mit Abschluss oder Abwicklung eines Vertrages"
    reference = "SR 281.1 Art. 8a Abs. 2"


class betreibung_ist_nichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Betreibung ist nichtig oder aufgrund Beschwerde/gerichtlichem Entscheid aufgehoben"
    reference = "SR 281.1 Art. 8a Abs. 3 lit. a"


class schuldner_mit_rueckforderungsklage_obsiegt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schuldner hat mit einer Rückforderungsklage obsiegt"
    reference = "SR 281.1 Art. 8a Abs. 3 lit. b"


class glaeubiger_betreibung_zurueckgezogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gläubiger hat die Betreibung zurückgezogen"
    reference = "SR 281.1 Art. 8a Abs. 3 lit. c"


class schuldner_rechtsvorschlag_mit_gesuch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schuldner hat Rechtsvorschlag erhoben und Nichtbekanntgabe-Gesuch gestellt"
    reference = "SR 281.1 Art. 8a Abs. 3 lit. d"


class betreibung_dritten_nicht_bekanntgegeben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Betreibung wird Dritten nicht zur Kenntnis gebracht"
    reference = "SR 281.1 Art. 8a Abs. 3"

    def formula(person, period, parameters):
        nichtig = person('betreibung_ist_nichtig', period)
        rueckforderung = person('schuldner_mit_rueckforderungsklage_obsiegt', period)
        zurueckgezogen = person('glaeubiger_betreibung_zurueckgezogen', period)
        rechtsvorschlag = person('schuldner_rechtsvorschlag_mit_gesuch', period)
        return nichtig + rueckforderung + zurueckgezogen + rechtsvorschlag


class jahre_seit_verfahrensabschluss(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahre seit Abschluss des Betreibungsverfahrens"
    reference = "SR 281.1 Art. 8a Abs. 4"


class einsichtsrecht_dritter_erloschen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einsichtsrecht Dritter ist erloschen (5 Jahre nach Verfahrensabschluss)"
    reference = "SR 281.1 Art. 8a Abs. 4"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_verfahrensabschluss', period)
        return jahre > 5
