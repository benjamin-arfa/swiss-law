"""SR 744.211 Art. 9

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_744_211_art_9_elektrische_einrichtungen_eisenbahnverordnung_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "SR 744.211 Art. 9 – Für elektrische Einrichtungen der Fahrzeuge "
        "(inkl. galvanisch mit der Fahrleitung verbundene Teile) gilt die "
        "Eisenbahnverordnung vom 23. November 1983 (SR 742.141.1)."
    )
    reference = "https://www.fedlex.admin.ch/eli/cc/744.211/art/9"

    def formula(person, period, parameters):
        # Art. 9 is a blanket regulatory reference: whenever a person is
        # responsible for creating, operating, or maintaining electrical
        # equipment on trolley/tram vehicles (especially parts galvanically
        # connected to the overhead line), the Swiss Railway Ordinance
        # SR 742.141.1 applies. The variable is True when that responsibility
        # exists; actual compliance rules live in SR 742.141.1.
        betreibt_fahrzeug_elektrische_einrichtungen = person(
            'betreibt_fahrzeug_elektrische_einrichtungen', period
        )
        return betreibt_fahrzeug_elektrische_einrichtungen


class betreibt_fahrzeug_elektrische_einrichtungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Person ist verantwortlich für Erstellung, Betrieb oder Instandhaltung "
        "elektrischer Einrichtungen eines Fahrzeugs (insbesondere galvanisch mit "
        "der Fahrleitung verbundene Teile) gemäss SR 744.211 Art. 9."
    )
    reference = "https://www.fedlex.admin.ch/eli/cc/744.211/art/9"
