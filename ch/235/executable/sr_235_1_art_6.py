"""SR 235.1 Art. 6

Generated from: ch/235/de/235.1.md

Grenzueberschreitende Bekanntgabe: Bedingungen fuer die Bekanntgabe
von Personendaten ins Ausland.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_ausland_angemessener_schutz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auslaendische Gesetzgebung gewaehrleistet angemessenen Datenschutz"
    reference = "SR 235.1 Art. 6 Abs. 1"


class dsg_ausland_vertragliche_garantien(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hinreichende Garantien (insb. Vertrag) gewaehrleisten angemessenen Schutz im Ausland"
    reference = "SR 235.1 Art. 6 Abs. 2 lit. a"


class dsg_ausland_einwilligung_einzelfall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Betroffene Person hat im Einzelfall in die grenzueberschreitende Bekanntgabe eingewilligt"
    reference = "SR 235.1 Art. 6 Abs. 2 lit. b"


class dsg_ausland_vertragszusammenhang(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bearbeitung steht in unmittelbarem Zusammenhang mit Vertragsabschluss/-abwicklung"
    reference = "SR 235.1 Art. 6 Abs. 2 lit. c"


class dsg_ausland_oeffentliches_interesse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bekanntgabe ist fuer oeffentliches Interesse oder Rechtsanspruchsdurchsetzung unerlaesslich"
    reference = "SR 235.1 Art. 6 Abs. 2 lit. d"


class dsg_ausland_schutz_leib_leben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bekanntgabe ist zum Schutz von Leib oder Leben erforderlich"
    reference = "SR 235.1 Art. 6 Abs. 2 lit. e"


class dsg_ausland_daten_allgemein_zugaenglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Betroffene Person hat Daten allgemein zugaenglich gemacht und Bearbeitung nicht untersagt"
    reference = "SR 235.1 Art. 6 Abs. 2 lit. f"


class dsg_ausland_konzernintern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bekanntgabe innerhalb derselben juristischen Person/Gesellschaft mit einheitlicher Leitung"
    reference = "SR 235.1 Art. 6 Abs. 2 lit. g"


class dsg_grenzueberschreitende_bekanntgabe_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Grenzueberschreitende Bekanntgabe von Personendaten ist zulaessig"
    reference = "SR 235.1 Art. 6"

    def formula(person, period, parameters):
        angemessener_schutz = person('dsg_ausland_angemessener_schutz', period)
        garantien = person('dsg_ausland_vertragliche_garantien', period)
        einwilligung = person('dsg_ausland_einwilligung_einzelfall', period)
        vertrag = person('dsg_ausland_vertragszusammenhang', period)
        oeffentlich = person('dsg_ausland_oeffentliches_interesse', period)
        leib_leben = person('dsg_ausland_schutz_leib_leben', period)
        zugaenglich = person('dsg_ausland_daten_allgemein_zugaenglich', period)
        konzernintern = person('dsg_ausland_konzernintern', period)

        # Zulaessig wenn angemessener Schutz vorhanden (Abs. 1)
        # ODER eine der Ausnahmen nach Abs. 2 lit. a-g erfuellt ist
        ausnahme = garantien + einwilligung + vertrag + oeffentlich + leib_leben + zugaenglich + konzernintern
        return angemessener_schutz + (not_(angemessener_schutz) * (ausnahme > 0))
