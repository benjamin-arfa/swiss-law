"""SR 744.103 Art. 8

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fahrerbescheinigung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person benötigt eine Fahrerbescheinigung für den internationalen gewerblichen Güterverkehr auf der Strasse"
    reference = "SR 744.103 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        im_internationalen_gueterverkehr = person('im_internationalen_gewerblichen_gueterverkehr', period)
        befoerderung_auf_strasse = person('befoerderung_auf_strasse_durchfuehrend', period)
        vom_erfordernis_ausgenommen = person('fahrerbescheinigung_ausnahme', period)
        return im_internationalen_gueterverkehr * befoerderung_auf_strasse * ~vom_erfordernis_ausgenommen


class im_internationalen_gewerblichen_gueterverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person führt Beförderungen im internationalen gewerblichen Güterverkehr durch"
    reference = "SR 744.103 Art. 8 Abs. 1"


class befoerderung_auf_strasse_durchfuehrend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person führt Beförderungen auf der Strasse durch"
    reference = "SR 744.103 Art. 8 Abs. 1"


class fahrerbescheinigung_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist gemäss einschlägigen Vorschriften (fremdenpolizei-, sozialversicherungs- und arbeitsrechtlicher Natur) beschäftigt oder eingesetzt"
    reference = "SR 744.103 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        fremdenpolizeilich_konform = person('fremdenpolizeilich_konform', period)
        sozialversicherungsrechtlich_konform = person('sozialversicherungsrechtlich_konform', period)
        arbeitsrechtlich_konform = person('arbeitsrechtlich_konform', period)
        return fremdenpolizeilich_konform * sozialversicherungsrechtlich_konform * arbeitsrechtlich_konform


class fremdenpolizeilich_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person erfüllt fremdenpolizeiliche Voraussetzungen für die Beschäftigung im Strassenverkehr"
    reference = "SR 744.103 Art. 8 Abs. 2"


class sozialversicherungsrechtlich_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person erfüllt sozialversicherungsrechtliche Voraussetzungen für die Beschäftigung im Strassenverkehr"
    reference = "SR 744.103 Art. 8 Abs. 2"


class arbeitsrechtlich_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person erfüllt arbeitsrechtliche Voraussetzungen für die Beschäftigung im Strassenverkehr"
    reference = "SR 744.103 Art. 8 Abs. 2"


class fahrerbescheinigung_ausnahme(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist vom Erfordernis der Fahrerbescheinigung ausgenommen (Angehörige eines Staates mit Gegenrecht)"
    reference = "SR 744.103 Art. 8 Abs. 3"

    def formula(person, period, parameters):
        staatsangehoerigkeit_gegenrechtsstaat = person('staatsangehoerigkeit_gegenrechtsstaat', period)
        return staatsangehoerigkeit_gegenrechtsstaat


class staatsangehoerigkeit_gegenrechtsstaat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Angehörige eines Staates, der gegenüber der Schweiz Gegenrecht hält (gemäss UVEK-Verfügung)"
    reference = "SR 744.103 Art. 8 Abs. 3"
