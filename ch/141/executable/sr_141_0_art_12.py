"""SR 141.0 Art. 12 - Integrationskriterien

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class beachtet_oeffentliche_sicherheit_und_ordnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person beachtet die oeffentliche Sicherheit und Ordnung"
    reference = "SR 141.0 Art. 12 Abs. 1 lit. a"


class respektiert_werte_bundesverfassung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person respektiert die Werte der Bundesverfassung"
    reference = "SR 141.0 Art. 12 Abs. 1 lit. b"


class sprachkompetenz_landessprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person kann sich im Alltag in Wort und Schrift in einer Landessprache verstaendigen"
    reference = "SR 141.0 Art. 12 Abs. 1 lit. c"


class teilnahme_wirtschaftsleben_oder_bildung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person nimmt am Wirtschaftsleben oder am Erwerb von Bildung teil"
    reference = "SR 141.0 Art. 12 Abs. 1 lit. d"


class foerderung_integration_familienmitglieder(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person foerdert und unterstuetzt die Integration der Familienmitglieder"
    reference = "SR 141.0 Art. 12 Abs. 1 lit. e"


class behinderung_oder_krankheit_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine Behinderung, Krankheit oder andere gewichtige persoenliche Umstaende liegen vor"
    reference = "SR 141.0 Art. 12 Abs. 2"


# Computed variables

class integrationskriterien_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Integrationskriterien sind erfuellt"
    reference = "SR 141.0 Art. 12"

    def formula(self, period, parameters):
        sicherheit = self('beachtet_oeffentliche_sicherheit_und_ordnung', period)
        verfassung = self('respektiert_werte_bundesverfassung', period)
        sprache = self('sprachkompetenz_landessprache', period)
        wirtschaft = self('teilnahme_wirtschaftsleben_oder_bildung', period)
        foerderung = self('foerderung_integration_familienmitglieder', period)
        behinderung = self('behinderung_oder_krankheit_vorhanden', period)

        # Abs. 1: Alle Kriterien muessen erfuellt sein
        alle_erfuellt = sicherheit * verfassung * sprache * wirtschaft * foerderung

        # Abs. 2: Bei Behinderung/Krankheit koennen lit. c und d erleichtert werden
        mit_erleichterung = sicherheit * verfassung * foerderung * behinderung

        return alle_erfuellt + mit_erleichterung > 0
