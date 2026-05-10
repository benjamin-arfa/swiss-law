"""SR 141.0 Art. 26 - Voraussetzungen (Wiedereinbuergerung)

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class person_in_schweiz_wohnhaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person haelt sich in der Schweiz auf"
    reference = "SR 141.0 Art. 26 Abs. 1"


class erfolgreich_integriert_art26(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist erfolgreich integriert (fuer Wiedereinbuergerung)"
    reference = "SR 141.0 Art. 26 Abs. 1 lit. a"


class eng_mit_schweiz_verbunden_art26(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist eng mit der Schweiz verbunden (fuer Wiedereinbuergerung im Ausland)"
    reference = "SR 141.0 Art. 26 Abs. 1 lit. b"


class beachtet_sicherheit_ordnung_art26(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person beachtet die oeffentliche Sicherheit und Ordnung"
    reference = "SR 141.0 Art. 26 Abs. 1 lit. c"


class respektiert_bundesverfassung_art26(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person respektiert die Werte der Bundesverfassung"
    reference = "SR 141.0 Art. 26 Abs. 1 lit. d"


class keine_gefaehrdung_sicherheit_art26(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person stellt keine Gefaehrdung der Sicherheit dar"
    reference = "SR 141.0 Art. 26 Abs. 1 lit. e"


class voraussetzungen_wiedereinbuergerung_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Voraussetzungen fuer die Wiedereinbuergerung sind erfuellt"
    reference = "SR 141.0 Art. 26"

    def formula(self, period, parameters):
        in_schweiz = self('person_in_schweiz_wohnhaft', period)
        integriert = self('erfolgreich_integriert_art26', period)
        verbunden = self('eng_mit_schweiz_verbunden_art26', period)
        sicherheit = self('beachtet_sicherheit_ordnung_art26', period)
        verfassung = self('respektiert_bundesverfassung_art26', period)
        keine_gefahr = self('keine_gefaehrdung_sicherheit_art26', period)

        # In der Schweiz: integriert + c + d + e
        inland = in_schweiz * integriert * sicherheit * verfassung * keine_gefahr

        # Im Ausland: eng verbunden + c + d + e (sinngemäss)
        ausland = not_(in_schweiz) * verbunden * sicherheit * verfassung * keine_gefahr

        return inland + ausland > 0
