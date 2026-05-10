"""SR 744.103 Art. 1

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strassentransportunternehmen_zulassungsbewilligung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zulassungsbewilligung als Strassentransportunternehmen erforderlich"
    reference = "SR 744.103 Art. 1 Abs. 3"

    def formula(person, period, parameters):
        befoerderung_nach_anhang4 = person('befoerderung_nach_anhang4_landverkehrsabkommen', period)
        return ~befoerderung_nach_anhang4


class befoerderung_nach_anhang4_landverkehrsabkommen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Durchführung von Beförderungen nach Anhang 4 des Landverkehrsabkommens"
    reference = "SR 744.103 Art. 1 Abs. 3"


class strassentransportunternehmen_sitz_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tatsächlicher und dauerhafter Sitz in der Schweiz"
    reference = "SR 744.103 Art. 1 Abs. 2"


class strassentransportunternehmen_handelsregister_eingetragen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Im Handelsregister eingetragen"
    reference = "SR 744.103 Art. 1 Abs. 2 lit. a"


class strassentransportunternehmen_einzelfirma_befreit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Als Einzelfirma von der Pflicht zur Eintragung ins Handelsregister befreit"
    reference = "SR 744.103 Art. 1 Abs. 2 lit. b"


class strassentransportunternehmen_oeffentlich_rechtliche_korporation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Als öffentlich-rechtliche Korporation mit Transportbetrieb"
    reference = "SR 744.103 Art. 1 Abs. 2 lit. c"


class strassentransportunternehmen_zulassungsbewilligung_berechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigt zur Erteilung einer Zulassungsbewilligung als Strassentransportunternehmen"
    reference = "SR 744.103 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        sitz_in_schweiz = person('strassentransportunternehmen_sitz_in_schweiz', period)
        handelsregister = person('strassentransportunternehmen_handelsregister_eingetragen', period)
        einzelfirma_befreit = person('strassentransportunternehmen_einzelfirma_befreit', period)
        oeffentlich_rechtlich = person('strassentransportunternehmen_oeffentlich_rechtliche_korporation', period)
        rechtsform_erfuellt = handelsregister + einzelfirma_befreit + oeffentlich_rechtlich
        return sitz_in_schweiz * rechtsform_erfuellt
