"""AG 290.100 § 5

Generated from: ch/ag/de/290.100.md

§ 5 Anwaltstarif: The Grosse Rat regulates by decree the compensation
in proceedings before Aargau courts and administrative authorities for:
a) unentgeltliche Rechtsvertretung (legal aid representation)
b) amtliche Verteidigung (official defense counsel)
c) state compensation to a represented party upon winning or remand
d) party compensation for opposing counsel costs
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ag_unentgeltliche_rechtsvertretung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hat unentgeltliche Rechtsvertretung (AG 290.100 § 5 Bst. a)"
    reference = "AG 290.100 § 5 Abs. 1 Bst. a"


class ag_amtliche_verteidigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hat amtliche Verteidigung (AG 290.100 § 5 Bst. b)"
    reference = "AG 290.100 § 5 Abs. 1 Bst. b"


class ag_obsiegend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Partei hat im Verfahren obsiegt oder Sache wurde zurueckgewiesen (AG 290.100 § 5 Bst. c)"
    reference = "AG 290.100 § 5 Abs. 1 Bst. c"


class ag_anwaltlich_vertreten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Partei ist anwaltlich vertreten (AG 290.100 § 5 Bst. c)"
    reference = "AG 290.100 § 5 Abs. 1 Bst. c"


class ag_entschaedigung_staat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Entschaedigung des Staates an anwaltlich vertretene Partei bei Obsiegen (AG 290.100 § 5 Bst. c)"
    reference = "AG 290.100 § 5 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        obsiegend = person('ag_obsiegend', period)
        vertreten = person('ag_anwaltlich_vertreten', period)
        return obsiegend * vertreten


class ag_parteikostenersatz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Parteikostenersatz fuer Anwaltskosten der Gegenpartei (AG 290.100 § 5 Bst. d)"
    reference = "AG 290.100 § 5 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        return person('ag_obsiegend', period)
