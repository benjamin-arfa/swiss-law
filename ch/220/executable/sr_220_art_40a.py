"""SR 220 Art. 40a

Generated from: ch/de/220.md

Widerrufsrecht bei Haustuergeschaeften: Gilt fuer Vertraege ueber
bewegliche Sachen und Dienstleistungen fuer den persoenlichen oder
familiaeren Gebrauch, wenn der Anbieter gewerblich handelt und die
Leistung des Kunden 100 Franken uebersteigt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_haustuergeschaeft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Haustuergeschaeft vorliegt (Art. 40a-40f OR)"
    reference = "SR 220 Art. 40a"

    def formula(person, period, parameters):
        ist_persoenlicher_gebrauch = person('vertrag_fuer_persoenlichen_gebrauch', period)
        anbieter_gewerblich = person('anbieter_handelt_gewerblich', period)
        leistung_betrag = person('vertrag_leistung_betrag', period)
        mindestbetrag = parameters(period).or_haustuergeschaeft.mindestbetrag

        angebot_am_arbeitsplatz = person('angebot_am_arbeitsplatz_oder_wohnung', period)
        angebot_oeffentlich = person('angebot_oeffentliche_verkehrsmittel_strassen', period)
        angebot_werbeveranstaltung = person('angebot_werbeveranstaltung_ausflug', period)
        angebot_telefon = person('angebot_am_telefon', period)

        ort_qualifiziert = (
            angebot_am_arbeitsplatz
            + angebot_oeffentlich
            + angebot_werbeveranstaltung
            + angebot_telefon
        ) > 0

        return (
            ist_persoenlicher_gebrauch
            * anbieter_gewerblich
            * (leistung_betrag > mindestbetrag)
            * ort_qualifiziert
        )


class vertrag_fuer_persoenlichen_gebrauch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vertrag fuer den persoenlichen oder familiaeren Gebrauch"
    reference = "SR 220 Art. 40a Abs. 1"


class anbieter_handelt_gewerblich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Anbieter im Rahmen einer beruflichen oder gewerblichen Taetigkeit handelt"
    reference = "SR 220 Art. 40a Abs. 1 lit. a"


class vertrag_leistung_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag der Kundenleistung in CHF"
    reference = "SR 220 Art. 40a Abs. 1 lit. b"


class angebot_am_arbeitsplatz_oder_wohnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Angebot am Arbeitsplatz, in Wohnraeumen oder in deren Umgebung"
    reference = "SR 220 Art. 40b lit. a"


class angebot_oeffentliche_verkehrsmittel_strassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Angebot in oeffentlichen Verkehrsmitteln oder auf oeffentlichen Strassen"
    reference = "SR 220 Art. 40b lit. b"


class angebot_werbeveranstaltung_ausflug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Angebot an einer Werbeveranstaltung mit Ausflugsfahrt"
    reference = "SR 220 Art. 40b lit. c"


class angebot_am_telefon(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Angebot am Telefon oder vergleichbare muendliche Telekommunikation"
    reference = "SR 220 Art. 40b lit. d"
