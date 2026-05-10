"""SR 672.933.21 Art. 2 — Vorprüfung spanischer Ersuchen bei Steuerbetrug

Art. 2: Ersuchen um Informationsaustausch bei Steuerbetrug (Art. 25bis Abs. 1
lit. c DBA) werden von der ESTV vorgeprüft. Bei Nichterfüllung wird Spanien
informiert. Bei positiver Vorprüfung wird der Informationsinhaber benachrichtigt.

Generated from: ch/672/de/672.933.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ersuchen_steuerbetrug_es(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Spanisches Ersuchen um Informationsaustausch bei Steuerbetrug (Art. 25bis Abs. 1 lit. c)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_2"


class vorpruefung_ersuchen_positiv(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Vorprüfung des Ersuchens zeigt erfüllte Voraussetzungen (SR 672.933.21 Art. 2 Abs. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_2"


class informationsinhaber_benachrichtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Informationsinhaber über Ersuchen informiert (SR 672.933.21 Art. 2 Abs. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_2"

    def formula(person, period, parameters):
        # Art. 2 Abs. 3: Bei positiver Vorprüfung wird der Informationsinhaber informiert.
        return person('ersuchen_steuerbetrug_es', period) * person('vorpruefung_ersuchen_positiv', period)


class zustellungsbevollmaechtigter_zu_bezeichnen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Betroffene Person soll Zustellungsbevollmächtigten in der Schweiz bezeichnen (SR 672.933.21 Art. 2 Abs. 4)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_2"

    def formula(person, period, parameters):
        return person('informationsinhaber_benachrichtigt', period)
