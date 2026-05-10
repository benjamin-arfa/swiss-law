"""SR 235.1 Art. 12

Generated from: ch/235/de/235.1.md

Persoenlichkeitsverletzungen: Verbot widerrechtlicher Verletzung
der Persoenlichkeit bei Datenbearbeitung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_bearbeitung_gegen_ausdruecklichen_willen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten einer Person werden gegen deren ausdruecklichen Willen bearbeitet"
    reference = "SR 235.1 Art. 12 Abs. 2 lit. b"


class dsg_besondere_daten_dritten_bekanntgegeben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Besonders schuetzenswerte Daten oder Profile an Dritte bekannt gegeben"
    reference = "SR 235.1 Art. 12 Abs. 2 lit. c"


class dsg_rechtfertigungsgrund_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ein Rechtfertigungsgrund nach Art. 13 liegt vor"
    reference = "SR 235.1 Art. 12 Abs. 2"


class dsg_daten_allgemein_zugaenglich_gemacht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Betroffene Person hat Daten allgemein zugaenglich gemacht und Bearbeitung nicht untersagt"
    reference = "SR 235.1 Art. 12 Abs. 3"


class dsg_persoenlichkeitsverletzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Widerrechtliche Persoenlichkeitsverletzung durch Datenbearbeitung"
    reference = "SR 235.1 Art. 12"

    def formula(person, period, parameters):
        grundsaetze = person('dsg_grundsaetze_eingehalten', period)
        gegen_willen = person('dsg_bearbeitung_gegen_ausdruecklichen_willen', period)
        besondere_dritte = person('dsg_besondere_daten_dritten_bekanntgegeben', period)
        rechtfertigung = person('dsg_rechtfertigungsgrund_vorhanden', period)
        zugaenglich = person('dsg_daten_allgemein_zugaenglich_gemacht', period)

        # Verletzung liegt vor bei: Verstoss gegen Grundsaetze (Abs. 2a),
        # Bearbeitung gegen Willen ohne Rechtfertigung (Abs. 2b),
        # Bekanntgabe besonderer Daten ohne Rechtfertigung (Abs. 2c)
        # Keine Verletzung wenn allgemein zugaenglich gemacht (Abs. 3)
        verletzung_grund = (
            not_(grundsaetze) +
            (gegen_willen * not_(rechtfertigung)) +
            (besondere_dritte * not_(rechtfertigung))
        ) > 0
        return verletzung_grund * not_(zugaenglich)
