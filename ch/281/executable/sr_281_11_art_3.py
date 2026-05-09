"""SR 281.11 Art. 3 — Eidgenössische Kommission für Schuldbetreibung und Konkurs

Oberaufsicht über Schuldbetreibung und Konkurs (OAV-SchKG).
Generated from: ch/de/281/281.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_mitglied_kommission_schkg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Mitglied der Eidgenössischen Kommission für Schuldbetreibung und Konkurs"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_3"


class kommission_schkg_max_mitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Anzahl Mitglieder der Eidgenössischen Kommission für Schuldbetreibung und Konkurs (SR 281.11 Art. 3 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 2: Die Kommission setzt sich aus höchstens 10 Mitgliedern zusammen.
        return 10


class kommission_beraet_bundesamt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eidgenössische Kommission berät das Bundesamt für Justiz in der Ausübung der Oberaufsicht (SR 281.11 Art. 3 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 1: Die Kommission berät das BAJ in Fragen der
        # Rechtsetzung und Rechtsanwendung.
        return person('ist_mitglied_kommission_schkg', period)


class ist_vorsitzender_kommission_schkg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat den Vorsitz der Eidgenössischen Kommission für SchKG (SR 281.11 Art. 3 Abs. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 3: Den Vorsitz hat die Leiterin oder der Leiter der
        # Dienststelle für Oberaufsicht SchKG.
        return person('ist_leiter_dienststelle_oberaufsicht_schkg', period)


class ist_leiter_dienststelle_oberaufsicht_schkg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Leiterin oder Leiter der Dienststelle für Oberaufsicht SchKG"
    reference = "https://www.fedlex.admin.ch/eli/cc/2006/720/de#art_3"
