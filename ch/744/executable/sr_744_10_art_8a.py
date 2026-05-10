"""SR 744.10 Art. 8a

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strassentransport_auftrag_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Auftrag an Strassentransportunternehmen im Güterverkehr ist zulässig (SR 744.10 Art. 8a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2003/651/de#art_8_a"

    def formula(person, period, parameters):
        hat_zulassungsbewilligung = person('strassentransportunternehmen_hat_zulassungsbewilligung', period)
        hat_fahrerbescheinigung = person('strassentransportunternehmen_hat_fahrerbescheinigung', period)
        erfuellt_kabotagevorschriften = person('strassentransportunternehmen_erfuellt_kabotagevorschriften', period)

        keine_verletzung_zulassung = hat_zulassungsbewilligung * hat_fahrerbescheinigung
        keine_verletzung_kabotage = erfuellt_kabotagevorschriften

        return keine_verletzung_zulassung * keine_verletzung_kabotage


class strassentransportunternehmen_hat_zulassungsbewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strassentransportunternehmen verfügt über erforderliche Zulassungsbewilligung gemäss SR 744.10, Landverkehrsabkommen (SR 0.740.72) oder Verordnung (EG) Nr. 1072/2009 Kapitel II"
    reference = "https://www.fedlex.admin.ch/eli/cc/2003/651/de#art_8_a"


class strassentransportunternehmen_hat_fahrerbescheinigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strassentransportunternehmen verfügt über erforderliche Fahrerbescheinigung gemäss SR 744.10, Landverkehrsabkommen (SR 0.740.72) oder Verordnung (EG) Nr. 1072/2009 Kapitel II"
    reference = "https://www.fedlex.admin.ch/eli/cc/2003/651/de#art_8_a"


class strassentransportunternehmen_erfuellt_kabotagevorschriften(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strassentransportunternehmen erfüllt Kabotagevorschriften des Landverkehrsabkommens (SR 0.740.72) oder Verordnung (EG) Nr. 1072/2009 Kapitel III"
    reference = "https://www.fedlex.admin.ch/eli/cc/2003/651/de#art_8_a"


class auftrag_verstosst_gegen_zulassungspflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Durchführung des Auftrags verstösst gegen Zulassungsbewilligungs- oder Fahrerbescheinigungspflicht (Art. 8a lit. a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2003/651/de#art_8_a"

    def formula(person, period, parameters):
        hat_zulassungsbewilligung = person('strassentransportunternehmen_hat_zulassungsbewilligung', period)
        hat_fahrerbescheinigung = person('strassentransportunternehmen_hat_fahrerbescheinigung', period)
        return not_(hat_zulassungsbewilligung) + not_(hat_fahrerbescheinigung)


class auftrag_verstosst_gegen_kabotagevorschriften(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Durchführung des Auftrags verstösst gegen Kabotagevorschriften (Art. 8a lit. b)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2003/651/de#art_8_a"

    def formula(person, period, parameters):
        erfuellt_kabotagevorschriften = person('strassentransportunternehmen_erfuellt_kabotagevorschriften', period)
        return not_(erfuellt_kabotagevorschriften)


class beauftragung_strassentransportunternehmen_verboten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beauftragung des Strassentransportunternehmens mit gewerbsmässiger Güterbeförderung ist verboten (Art. 8a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2003/651/de#art_8_a"

    def formula(person, period, parameters):
        verstoss_zulassung = person('auftrag_verstosst_gegen_zulassungspflicht', period)
        verstoss_kabotage = person('auftrag_verstosst_gegen_kabotagevorschriften', period)
        return verstoss_zulassung + verstoss_kabotage
