"""SR 672.3 Art. 5 — Veröffentlichung

Bundesgesetz über die Anerkennung privater Vereinbarungen zur Vermeidung der Doppelbesteuerung.
Generated from: ch/de/672/672.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class beschluss_anerkennung_oder_entzug(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegt ein Beschluss des Bundesrates über Anerkennung oder Entzug vor"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_5"


class veroeffentlichung_im_bundesblatt_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beschluss muss im Bundesblatt veröffentlicht werden (SR 672.3 Art. 5 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_5"

    def formula(person, period, parameters):
        # Art. 5 Abs. 1: Jeder Beschluss über Anerkennung oder Entzug
        # wird im Bundesblatt veröffentlicht.
        return person('beschluss_anerkennung_oder_entzug', period)


class vereinbarung_mit_anerkennungsbeschluss_veroeffentlicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Vereinbarung wird mit dem Anerkennungsbeschluss veröffentlicht (SR 672.3 Art. 5 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_5"

    def formula(person, period, parameters):
        # Art. 5 Abs. 2: Die Vereinbarung wird mit dem Anerkennungsbeschluss veröffentlicht.
        return person('vereinbarung_anerkannt_durch_bundesrat', period)


class vereinbarung_anerkannt_durch_bundesrat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Vereinbarung wurde durch den Bundesrat anerkannt"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_5"
