"""SR 744.211 Art. 26

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_verordnung_anwendbar_auf_vorkonzessionierte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verordnung findet Anwendung auf vor Inkrafttreten konzessionierte Trolleybusunternehmungen"
    reference = "SR 744.211 Art. 26 Abs. 1"

    def formula(person, period, parameters):
        # Ordinance applies to all trolleybus companies, including those licensed before it entered into force
        return person('ist_konzessionierte_trolleybusunternehmung', period)


class fahrzeug_numerierung_meldepflicht_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konzessionierte Unternehmung hat Fahrzeugnumerierung dem Bundesamt innert Jahresfrist gemeldet"
    reference = "SR 744.211 Art. 26 Abs. 2"

    def formula(person, period, parameters):
        ist_konzessioniert = person('ist_konzessionierte_trolleybusunternehmung', period)
        meldung_erfolgt = person('fahrzeug_numerierung_gemeldet', period)
        return ist_konzessioniert * meldung_erfolgt


class inverkehrsetzungsbewilligung_weiterhin_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vor Inkrafttreten erteilte Bewilligung für die Inverkehrsetzung von Fahrzeugen bleibt gültig"
    reference = "SR 744.211 Art. 26 Abs. 3"

    def formula(person, period, parameters):
        # Permits issued before the law or ordinance entered into force remain valid
        return person('bewilligung_inverkehrsetzung_vor_inkrafttreten_erteilt', period)


class fuehrerausweis_weiterhin_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vor Inkrafttreten erteilter Führerausweis bleibt weiterhin gültig"
    reference = "SR 744.211 Art. 26 Abs. 3"

    def formula(person, period, parameters):
        # Driver's licenses issued before the law or ordinance entered into force remain valid
        return person('fuehrerausweis_vor_inkrafttreten_erteilt', period)


class fuehrerausweis_anpassung_an_neue_bestimmungen_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Führerausweis ist bei nächster Gelegenheit den neuen Bestimmungen anzupassen"
    reference = "SR 744.211 Art. 26 Abs. 3"

    def formula(person, period, parameters):
        # Adaptation required for all previously issued driver's licenses still in use
        ausweis_noch_gueltig = person('fuehrerausweis_weiterhin_gueltig', period)
        noch_nicht_angepasst = person('fuehrerausweis_noch_nicht_an_neue_bestimmungen_angepasst', period)
        return ausweis_noch_gueltig * noch_nicht_angepasst
