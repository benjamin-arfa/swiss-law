"""SR 744.211 Art. 22

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class trolleybus_betriebsreglemente_genehmigungspflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Betriebsreglemente und Ausführungsbestimmungen von Trolleybusunternehmungen sind dem Bundesamt zur Genehmigung einzureichen"
    reference = "SR 744.211 Art. 22"

    def formula(person, period, parameters):
        ist_trolleybusunternehmung = person('ist_trolleybusunternehmung', period)
        hat_betriebsreglement_oder_aenderung = person('hat_betriebsreglement_oder_aenderung', period)
        return ist_trolleybusunternehmung * hat_betriebsreglement_oder_aenderung


class ist_trolleybusunternehmung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person betreibt eine Trolleybusunternehmung"
    reference = "SR 744.211 Art. 22"


class hat_betriebsreglement_oder_aenderung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegt ein Betriebsreglement, Ausführungsbestimmungen, eine Änderung oder Ergänzung davon vor, oder Vorschriften über Bedienung und Unterhalt elektrischer Anlagen"
    reference = "SR 744.211 Art. 22"


class elektrische_anlagen_vorschriften_genehmigungspflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorschriften über Bedienung und Unterhalt elektrischer Anlagen sind dem Bundesamt zur Genehmigung einzureichen"
    reference = "SR 744.211 Art. 22"

    def formula(person, period, parameters):
        ist_trolleybusunternehmung = person('ist_trolleybusunternehmung', period)
        hat_vorschriften_elektrische_anlagen = person('hat_vorschriften_elektrische_anlagen', period)
        return ist_trolleybusunternehmung * hat_vorschriften_elektrische_anlagen


class hat_vorschriften_elektrische_anlagen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegen Vorschriften über Bedienung und Unterhalt elektrischer Anlagen vor"
    reference = "SR 744.211 Art. 22"
