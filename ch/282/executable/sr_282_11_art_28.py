"""SR 282.11 Art. 28 - Anordnung der Beiratschaft

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class gemeinwesen_zahlungsunfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Gemeinwesen hat sich zahlungsunfaehig erklaert oder ist voraussichtlich laenger nicht zahlungsfaehig"
    reference = "SR 282.11 Art. 28 Abs. 1"


class zwangsverwaltung_nicht_angeordnet_oder_ungenuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine administrative Zwangsverwaltung wird nicht angeordnet oder erweist sich als ungenuegend"
    reference = "SR 282.11 Art. 28 Abs. 1"


class glaeubigergemeinschaftsverfahren_moeglich_und_genuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Durchfuehrung des Glaeubigergemeinschaftsverfahrens ist moeglich und genuegend"
    reference = "SR 282.11 Art. 28 Abs. 2"


class interessen_glaeubiger_anderweitig_gewahrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Interessen der Glaeubiger koennen auf andere Weise hinreichend gewahrt werden"
    reference = "SR 282.11 Art. 28 Abs. 2"


# Computed variables

class beiratschaft_anzuordnen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Aufsichtsbehoerde hat die Beiratschaft anzuordnen"
    reference = "SR 282.11 Art. 28"

    def formula(self, period, parameters):
        zahlungsunfaehig = self('gemeinwesen_zahlungsunfaehig', period)
        keine_zwangsverwaltung = self('zwangsverwaltung_nicht_angeordnet_oder_ungenuegend', period)
        ggv = self('glaeubigergemeinschaftsverfahren_moeglich_und_genuegend', period)
        anderweitig = self('interessen_glaeubiger_anderweitig_gewahrt', period)
        # Beiratschaft wenn zahlungsunfaehig, keine Zwangsverwaltung, und keine Alternative genuegt
        return zahlungsunfaehig * keine_zwangsverwaltung * (1 - ggv) * (1 - anderweitig)
