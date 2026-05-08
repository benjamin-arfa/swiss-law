"""SR 745.1 Art. 9

Generated from: ch/745/de/745.1.md

Voraussetzungen fuer die Erteilung, den Entzug und den Widerruf von
Konzessionen und Bewilligungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class erfuellt_konzessionsvoraussetzungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen erfuellt alle Voraussetzungen fuer eine Konzession oder Bewilligung"
    reference = "SR 745.1 Art. 9 Abs. 1-2"

    def formula(person, period, parameters):
        # Art. 9 Abs. 1-2: Voraussetzungen fuer Konzessionserteilung.
        hat_verkehrswege_bewilligung = person('hat_verkehrswege_bewilligung', period)
        transportleistung_zweckmaessig = person('transportleistung_zweckmaessig', period)
        kein_nachteiliger_wettbewerb = person('kein_nachteiliger_wettbewerb', period)
        hat_verkehrswege_rechte = person('hat_verkehrswege_rechte', period)
        gewaehr_gesetzeskonformitaet = person('gewaehr_gesetzeskonformitaet', period)
        einhaltung_arbeitsrecht = person('einhaltung_arbeitsrecht_pbg', period)
        return (hat_verkehrswege_bewilligung
                * transportleistung_zweckmaessig
                * kein_nachteiliger_wettbewerb
                * hat_verkehrswege_rechte
                * gewaehr_gesetzeskonformitaet
                * einhaltung_arbeitsrecht)


class hat_verkehrswege_bewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen verfuegt ueber Bewilligungen fuer Verkehrswege und Haltestellen"
    reference = "SR 745.1 Art. 9 Abs. 1"


class transportleistung_zweckmaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geplante Transportleistung ist zweckmaessig und wirtschaftlich erbringbar"
    reference = "SR 745.1 Art. 9 Abs. 2 lit. a"


class kein_nachteiliger_wettbewerb(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Keine volkswirtschaftlich nachteiligen Wettbewerbsverhaeltnisse fuer bestehende Angebote"
    reference = "SR 745.1 Art. 9 Abs. 2 lit. b"


class hat_verkehrswege_rechte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen verfuegt ueber alle Rechte fuer Benutzung der Verkehrswege"
    reference = "SR 745.1 Art. 9 Abs. 2 lit. c"


class gewaehr_gesetzeskonformitaet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen bietet Gewaehr fuer Einhaltung gesetzlicher Bestimmungen"
    reference = "SR 745.1 Art. 9 Abs. 2 lit. d"


class einhaltung_arbeitsrecht_pbg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen haelt arbeitsrechtliche Vorschriften ein und gewaehrleistet Arbeitsbedingungen der Branche"
    reference = "SR 745.1 Art. 9 Abs. 2 lit. e"


class konzession_entzogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konzession oder Bewilligung wurde entzogen"
    reference = "SR 745.1 Art. 9 Abs. 3"

    def formula(person, period, parameters):
        # Art. 9 Abs. 3: Entzug wenn Rechte nicht ausgeuebt, Voraussetzungen
        # nicht mehr erfuellt, oder Pflichten wiederholt/schwerwiegend verletzt.
        rechte_nicht_ausgeuebt = person('konzession_rechte_nicht_ausgeuebt', period)
        voraussetzungen_nicht_erfuellt = ~person('erfuellt_konzessionsvoraussetzungen', period)
        pflichten_verletzt = person('konzession_pflichten_schwer_verletzt', period)
        return rechte_nicht_ausgeuebt + voraussetzungen_nicht_erfuellt + pflichten_verletzt


class konzession_rechte_nicht_ausgeuebt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen uebt die verliehenen Rechte nicht oder nur teilweise aus"
    reference = "SR 745.1 Art. 9 Abs. 3 lit. a"


class konzession_pflichten_schwer_verletzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen hat Pflichten wiederholt oder in schwerwiegender Weise verletzt"
    reference = "SR 745.1 Art. 9 Abs. 3 lit. c"
