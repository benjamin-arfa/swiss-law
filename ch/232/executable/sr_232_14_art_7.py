"""SR 232.14 Art. 7

Generated from: ch/232/de/232.14.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erfindung_oeffentlich_zugaenglich_vor_anmeldedatum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung war vor dem Anmelde- oder Prioritätsdatum der Öffentlichkeit zugänglich"
    reference = "SR 232.14 Art. 7 Abs. 2"


class erfindung_in_frueherer_anmeldung_enthalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung ist im Inhalt einer früheren Anmeldung für die Schweiz enthalten"
    reference = "SR 232.14 Art. 7 Abs. 3"


class erfindung_gehoert_zum_stand_der_technik(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfindung gehört zum Stand der Technik"
    reference = "SR 232.14 Art. 7"

    def formula(person, period, parameters):
        oeffentlich = person('erfindung_oeffentlich_zugaenglich_vor_anmeldedatum', period)
        fruehere_anmeldung = person('erfindung_in_frueherer_anmeldung_enthalten', period)
        return oeffentlich + fruehere_anmeldung
