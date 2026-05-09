"""SR 832.312.15 Art. 5 – Anforderungen an das Bedienungspersonal

Generated from: ch/832/de/832.312.15.md

Hebearbeiten dürfen nur von körperlich/geistig geeigneten Personen
durchgeführt werden. Fahrzeug- und Turmdrehkrane erfordern einen
Kranführerausweis. Mindestalter für Lernfahrausweis: 17 Jahre (Art. 9).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class koerperlich_geistig_geeignet_kran(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Körperliche und geistige Eignung zur sicheren Bedienung des Krans"
    reference = "SR 832.312.15 Art. 5 Abs. 1 lit. a"


class kann_sich_am_arbeitsplatz_verstaendigen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kann sich am Arbeitsplatz verständigen"
    reference = "SR 832.312.15 Art. 5 Abs. 1 lit. b"


class ausgebildet_fuer_kranbedienung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Für die Bedienung des benützten Krans ausgebildet"
    reference = "SR 832.312.15 Art. 5 Abs. 1 lit. c"


class hat_kranfuehrerausweis(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Besitzt einen Kranführerausweis (Kategorie A oder B)"
    reference = "SR 832.312.15 Art. 5 Abs. 2 lit. a"


class hat_lernfahrausweis_kran(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Besitzt einen Lernfahrausweis für Krane"
    reference = "SR 832.312.15 Art. 5 Abs. 2 lit. b/c"


class ist_im_grundkurs_oder_pruefung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Führt Hebearbeiten im Rahmen von Grundkursen und Prüfungen durch"
    reference = "SR 832.312.15 Art. 5 Abs. 3"


class ist_fahrzeug_oder_turmdrehkran(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zu bedienender Kran ist Fahrzeugkran (Kat. A) oder Turmdrehkran (Kat. B)"
    reference = "SR 832.312.15 Art. 2 Abs. 2 lit. a/b"


class darf_hebearbeiten_ausfuehren(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person darf Hebearbeiten mit dem Kran durchführen"
    reference = "SR 832.312.15 Art. 5"

    def formula(person, period, parameters):
        geeignet = person('koerperlich_geistig_geeignet_kran', period.this_year)
        verstaendigung = person('kann_sich_am_arbeitsplatz_verstaendigen', period.this_year)
        ausgebildet = person('ausgebildet_fuer_kranbedienung', period.this_year)
        ist_fz_td = person('ist_fahrzeug_oder_turmdrehkran', period.this_year)

        ausweis = person('hat_kranfuehrerausweis', period)
        lernfahr = person('hat_lernfahrausweis_kran', period)
        grundkurs = person('ist_im_grundkurs_oder_pruefung', period)

        # Abs. 1: Grundvoraussetzungen für alle Krane
        grundvoraussetzung = geeignet * verstaendigung * ausgebildet

        # Abs. 2: Bei Fahrzeug-/Turmdrehkranen zusätzlich Ausweis erforderlich
        # Abs. 3: Kein Ausweis bei Grundkursen/Prüfungen
        ausweis_ok = ausweis + lernfahr + grundkurs
        fahrzeug_td_ok = not_(ist_fz_td) + (ist_fz_td * ausweis_ok)

        return grundvoraussetzung * fahrzeug_td_ok
