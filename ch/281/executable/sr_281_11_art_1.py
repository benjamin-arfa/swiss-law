"""SR 281.11 Art. 1 — Zuständige Behörde

Oberaufsicht über Schuldbetreibung und Konkurs (OAV-SchKG).
Generated from: ch/de/281/281.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_bundesamt_fuer_justiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einheit ist das Bundesamt für Justiz"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_1"


class uebt_oberaufsicht_schkg_aus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Übt die Oberaufsicht über Schuldbetreibung und Konkurs aus (SR 281.11 Art. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_1"

    def formula(person, period, parameters):
        # Art. 1: Das Bundesamt für Justiz übt die Oberaufsicht über
        # Schuldbetreibung und Konkurs aus.
        return person('ist_bundesamt_fuer_justiz', period)


class ist_dienststelle_oberaufsicht_schkg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Dienststelle Oberaufsicht SchKG im Bundesamt für Justiz"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_1"


class ermaechtigt_weisungen_schkg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ermächtigt zum Erlass von Weisungen, Kreisschreiben und Empfehlungen zur Anwendung des SchKG (SR 281.11 Art. 1 lit. a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_1"

    def formula(person, period, parameters):
        return person('ist_dienststelle_oberaufsicht_schkg', period)


class ermaechtigt_inspektion_schkg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ermächtigt zur Inspektion der kantonalen Aufsichtsbehörden und Betreibungs-/Konkursämter (SR 281.11 Art. 1 lit. c)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_1"

    def formula(person, period, parameters):
        return person('ist_dienststelle_oberaufsicht_schkg', period)
