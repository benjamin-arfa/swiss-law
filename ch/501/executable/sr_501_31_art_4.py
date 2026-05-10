"""SR 501.31 Art. 4 - Aufgaben des BABS in Bezug auf den KSD

Generated from: ch/501/de/501.31.md

Das BABS hat in Bezug auf den KSD folgende Aufgaben:
a. konsolidierte Risikoanalyse
b. Leitung der Leitungskonferenz KSD und SANKO
c. Erarbeitung des KSD-Konzepts
d. Gesamtuebersicht ueber verfuegbare Ressourcen
e. Foerderung/Koordination der Aus-/Weiter-/Fortbildung
f. Vorschlaege fuer rechtliche/organisatorische Massnahmen
g. Information des Bundesrats
h. Oekonomischer Einsatz der Ressourcen
i. Koordination der Tierseuchen-Massnahmen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class babs_risikoanalyse_erstellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BABS eine konsolidierte Risikoanalyse erstellt hat"
    reference = "SR 501.31 Art. 4 lit. a"


class babs_leitet_leitungskonferenz_und_sanko(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BABS die Leitungskonferenz KSD und das SANKO leitet"
    reference = "SR 501.31 Art. 4 lit. b"


class babs_ksd_konzept_erarbeitet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BABS das Konzept ueber den KSD erarbeitet hat"
    reference = "SR 501.31 Art. 4 lit. c"


class babs_ressourcen_uebersicht_verfuegbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine aktualisierte Gesamtuebersicht ueber verfuegbare Ressourcen im Gesundheitswesen erstellt ist"
    reference = "SR 501.31 Art. 4 lit. d"


class babs_ausbildung_koordiniert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BABS die Aus-, Weiter- und Fortbildung der Kader und Spezialisten foerdert und koordiniert"
    reference = "SR 501.31 Art. 4 lit. e"


class babs_tierseuchen_koordiniert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BABS die Massnahmen zur Praevention und Bekaempfung von Tierseuchen koordiniert"
    reference = "SR 501.31 Art. 4 lit. i"
