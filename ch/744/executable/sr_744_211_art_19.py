"""SR 744.211 Art. 19

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_fuehrerausweis_ausbildungsbescheinigung_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bescheinigung über absolvierte Ausbildung gemäss Art. 18 liegt vor"
    reference = "SR 744.211 Art. 19 Abs. 1 lit. a"

    def formula(person, period, parameters):
        return person('trolleybus_ausbildung_absolviert', period)


class trolleybus_fuehrerausweis_technischer_pruefungsbericht_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Prüfungsbericht über technische Kenntnisse und elektrische Einrichtungen liegt vor"
    reference = "SR 744.211 Art. 19 Abs. 1 lit. b"

    def formula(person, period, parameters):
        return person('technische_kenntnisse_fahrzeuge_geprueft', period) * \
               person('elektrische_einrichtungen_vertrautheit_geprueft', period)


class trolleybus_zulassung_fuehrerprüfung_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen für Zulassung zur Führerprüfung oder zweiten Teilprüfung erfüllt (Art. 19 Abs. 1)"
    reference = "SR 744.211 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        bescheinigung = person('trolleybus_fuehrerausweis_ausbildungsbescheinigung_vorhanden', period)
        pruefungsbericht = person('trolleybus_fuehrerausweis_technischer_pruefungsbericht_vorhanden', period)
        return bescheinigung * pruefungsbericht


class trolleybus_fuehrerprüfung_durch_kanton_durchgefuehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Führerprüfung wird von kantonalen Motorfahrzeugsachverständigen durchgeführt"
    reference = "SR 744.211 Art. 19 Abs. 2"

    def formula(person, period, parameters):
        return person('kantonaler_motorfahrzeugsachverstaendiger_zustaendig', period)


class trolleybus_verkehrsvorschriften_kenntnis_nachgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kenntnis der Verkehrsvorschriften nachgewiesen"
    reference = "SR 744.211 Art. 19 Abs. 3"

    def formula(person, period, parameters):
        return person('verkehrsvorschriften_geprueft_bestanden', period)


class trolleybus_lenkvorrichtung_bremsen_kenntnis_nachgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kenntnis der Funktionen von Lenkvorrichtung und Bremsen des Trolleybusses nachgewiesen"
    reference = "SR 744.211 Art. 19 Abs. 3"

    def formula(person, period, parameters):
        return person('trolleybus_lenkvorrichtung_geprueft', period) * \
               person('trolleybus_bremsen_geprueft', period)


class trolleybus_fahrzeugbeherrschung_nachgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beherrschung des Trolleybusses in jeder Lage sowie störungs- und gefahrfreie Führung nachgewiesen"
    reference = "SR 744.211 Art. 19 Abs. 3"

    def formula(person, period, parameters):
        return person('trolleybus_fahrzeugbeherrschung_geprueft', period) * \
               person('trolleybus_verkehrssicheres_fuehren_nachgewiesen', period)


class trolleybus_fuehrerprüfung_anforderungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Anforderungen der Führerprüfung gemäss Art. 19 Abs. 3 erfüllt"
    reference = "SR 744.211 Art. 19 Abs. 3"

    def formula(person, period, parameters):
        verkehrsvorschriften = person('trolleybus_verkehrsvorschriften_kenntnis_nachgewiesen', period)
        lenkung_bremsen = person('trolleybus_lenkvorrichtung_bremsen_kenntnis_nachgewiesen', period)
        fahrzeugbeherrschung = person('trolleybus_fahrzeugbeherrschung_nachgewiesen', period)
        return verkehrsvorschriften * lenkung_bremsen * fahrzeugbeherrschung


class trolleybus_erste_teilprüfung_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erste Teilprüfung bestanden: Verkehrsvorschriften und Führung eines schweren Lastwagens"
    reference = "SR 744.211 Art. 19 Abs. 4"

    def formula(person, period, parameters):
        verkehrsvorschriften = person('verkehrsvorschriften_geprueft_bestanden', period)
        lastwagen_befahigung = person('schwerer_lastwagen_befaehigung_nachgewiesen', period)
        return verkehrsvorschriften * lastwagen_befahigung


class trolleybus_zweite_teilprüfung_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zweite Teilprüfung bestanden: Führung eines Trolleybusses gemäss Art. 19 Abs. 3"
    reference = "SR 744.211 Art. 19 Abs. 4"

    def formula(person, period, parameters):
        return person('trolleybus_fuehrerprüfung_anforderungen_erfuellt', period)


class trolleybus_fuehrerausweis_erteilt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybus-Führerausweis kann erteilt werden (alle Voraussetzungen nach Art. 19 erfüllt)"
    reference = "SR 744.211 Art. 19"

    def formula(person, period, parameters):
        zulassungsvoraussetzungen = person('trolleybus_zulassung_fuehrerprüfung_voraussetzungen_erfuellt', period)
        pruefung_durch_kanton = person('trolleybus_fuehrerprüfung_durch_kanton_durchgefuehrt', period)
        zwei_teilpruefungen = person('trolleybus_pruefung_in_zwei_teilen', period)

        pruefung_einteilig_bestanden = person('trolleybus_fuehrerprüfung_anforderungen_erfuellt', period)

        pruefung_zweiteilig_bestanden = (
            person('trolleybus_erste_teilprüfung_bestanden', period) *
            person('trolleybus_zweite_teilprüfung_bestanden', period)
        )

        pruefung_bestanden = where(
            zwei_teilpruefungen,
            pruefung_zweiteilig_bestanden,
            pruefung_einteilig_bestanden
        )

        return zulassungsvoraussetzungen * pruefung_durch_kanton * pruefung_bestanden


class trolleybus_pruefung_in_zwei_teilen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Führerprüfung wird in zwei Teilprüfungen durchgeführt"
    reference = "SR 744.211 Art. 19 Abs. 4"


class trolleybus_ausbildung_absolviert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorgeschriebene Ausbildung gemäss Art. 18 absolviert"
    reference = "SR 744.211 Art. 19 Abs. 1 lit. a"


class technische_kenntnisse_fahrzeuge_geprueft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gründliche Kenntnisse der technischen Beschaffenheit der Fahrzeuge geprüft"
    reference = "SR 744.211 Art. 19 Abs. 1 lit. b"


class elektrische_einrichtungen_vertrautheit_geprueft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Genügende Vertrautheit mit Besonderheiten der elektrischen Einrichtungen geprüft"
    reference = "SR 744.211 Art. 19 Abs. 1 lit. b"


class kantonaler_motorfahrzeugsachverstaendiger_zustaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kantonaler Motorfahrzeugsachverständiger für die Prüfung zuständig"
    reference = "SR 744.211 Art. 19 Abs. 2"


class verkehrsvorschriften_geprueft_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Prüfung der Verkehrsvorschriften bestanden"
    reference = "SR 744.211 Art. 19 Abs. 3"


class trolleybus_lenkvorrichtung_geprueft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kenntnis der Lenkvorrichtungsfunktionen des Trolleybusses geprüft"
    reference = "SR 744.211 Art. 19 Abs. 3"


class trolleybus_bremsen_geprueft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kenntnis der Bremsenfunktionen des Trolleybusses geprüft"
    reference = "SR 744.211 Art. 19 Abs. 3"


class trolleybus_fahrzeugbeherrschung_geprueft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beherrschung des Trolleybusses in jeder Lage geprüft"
    reference = "SR 744.211 Art. 19 Abs. 3"


class trolleybus_verkehrssicheres_fuehren_nachgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Störungs- und gefahrfreies Führen des Trolleybusses nachgewiesen"
    reference = "SR 744.211 Art. 19 Abs. 3"


class schwerer_lastwagen_befaehigung_nachgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befähigung zur Führung eines schweren Lastwagens nachgewiesen (erste Teilprüfung)"
    reference = "SR 744.211 Art. 19 Abs. 4"
