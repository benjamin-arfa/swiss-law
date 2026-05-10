"""SR 251 Art. 7

Generated from: ch/de/251.md

Inadmissible conduct of market-dominant and relatively market-powerful
enterprises: refusal to deal, discrimination, exploitative pricing,
predatory pricing, restriction of production/sales/development,
tying, and restricting parallel imports.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verweigerung_geschaeftsbeziehungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Verweigerung von Geschaeftsbeziehungen vorliegt"
    reference = "SR 251 Art. 7 Abs. 2 Bst. a"


class diskriminierung_handelspartner(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Handelspartner bei Preisen oder Geschaeftsbedingungen diskriminiert werden"
    reference = "SR 251 Art. 7 Abs. 2 Bst. b"


class erzwingung_unangemessener_preise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob unangemessene Preise oder Geschaeftsbedingungen erzwungen werden"
    reference = "SR 251 Art. 7 Abs. 2 Bst. c"


class preisunterbietung_gegen_wettbewerber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine gegen bestimmte Wettbewerber gerichtete Preisunterbietung vorliegt"
    reference = "SR 251 Art. 7 Abs. 2 Bst. d"


class einschraenkung_erzeugung_absatz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Einschraenkung der Erzeugung, des Absatzes oder der technischen Entwicklung vorliegt"
    reference = "SR 251 Art. 7 Abs. 2 Bst. e"


class koppelungsgeschaeft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Koppelungsgeschaeft vorliegt"
    reference = "SR 251 Art. 7 Abs. 2 Bst. f"


class einschraenkung_parallelimport(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Moeglichkeit zum Bezug im Ausland eingeschraenkt wird"
    reference = "SR 251 Art. 7 Abs. 2 Bst. g"


class missbrauch_marktstellung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Missbrauch der marktbeherrschenden oder relativ marktmaechtigen Stellung vorliegt"
    reference = "SR 251 Art. 7"

    def formula(person, period, parameters):
        marktmacht = (
            person('ist_marktbeherrschend', period)
            + person('ist_relativ_marktmaechtig', period)
        ) > 0
        missbrauch = (
            person('verweigerung_geschaeftsbeziehungen', period)
            + person('diskriminierung_handelspartner', period)
            + person('erzwingung_unangemessener_preise', period)
            + person('preisunterbietung_gegen_wettbewerber', period)
            + person('einschraenkung_erzeugung_absatz', period)
            + person('koppelungsgeschaeft', period)
            + person('einschraenkung_parallelimport', period)
        ) > 0
        return marktmacht * missbrauch
