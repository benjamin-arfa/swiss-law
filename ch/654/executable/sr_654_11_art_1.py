"""SR 654.11 Art. 1 - Inhalt eines laenderbezogenen Berichts

Generated from: ch/654/de/654.11.md

Defines the required content of a country-by-country report:
Table 1 (aggregate data per jurisdiction), Table 2 (entity listing with
business activities), and Table 3 (additional information).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class umsatzerloese_nicht_verbundene_unternehmen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Umsatzerloese durch Geschaeftsvorfaelle mit nicht verbundenen Unternehmen (Tabelle 1 Ziff. 1)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 1"


class umsatzerloese_verbundene_unternehmen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Umsatzerloese durch Geschaeftsvorfaelle mit verbundenen Unternehmen (Tabelle 1 Ziff. 2)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 2"


class umsatzerloese_insgesamt(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Umsatzerloese insgesamt (Tabelle 1 Ziff. 3)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 3"

    def formula(self, period, parameters):
        nicht_verbunden = self('umsatzerloese_nicht_verbundene_unternehmen', period)
        verbunden = self('umsatzerloese_verbundene_unternehmen', period)
        return nicht_verbunden + verbunden


class gewinn_oder_verlust_vor_steuern(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gewinn oder Verlust vor Steuern (Tabelle 1 Ziff. 4)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 4"


class entrichtete_gewinnsteuern_kassenbasis(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Entrichtete Gewinnsteuern auf Kassenbasis (Tabelle 1 Ziff. 5)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 5"


class aufgelaufene_gewinnsteuern_laufendes_jahr(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Aufgelaufene Gewinnsteuern im laufenden Jahr (Tabelle 1 Ziff. 6)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 6"


class ausgewiesenes_kapital(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ausgewiesenes Kapital (Tabelle 1 Ziff. 7)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 7"


class einbehaltener_gewinn(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Einbehaltener Gewinn vor Gewinnverwendung (Tabelle 1 Ziff. 8)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 8"


class beschaeftigtenzahl(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Beschaeftigtenzahl (Tabelle 1 Ziff. 9)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 9"


class materielle_vermoegenswerte(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Materielle Vermoegenswerte ohne fluessige Mittel (Tabelle 1 Ziff. 10)"
    reference = "SR 654.11 Art. 1 let. a Ziff. 10"
