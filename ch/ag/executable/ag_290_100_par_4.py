"""AG 290.100 § 4

Generated from: ch/ag/de/290.100.md

§ 4 Unerlaubte Ausubung des Anwaltsberufs: If a brief is submitted by
an unauthorized representative, the court returns it with a short deadline
for proper signature. If an unauthorized representative appears at a
hearing, they are turned away. The court reports unauthorized practice
to criminal authorities (§ 18).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ag_rechtsschrift_unzulaessige_vertretung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Rechtsschrift durch unzulaessige Vertretung eingereicht (AG 290.100 § 4 Abs. 1)"
    reference = "AG 290.100 § 4 Abs. 1"


class ag_verhandlung_unzulaessige_vertretung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unzulaessige Vertretung erscheint zu Verhandlung (AG 290.100 § 4 Abs. 2)"
    reference = "AG 290.100 § 4 Abs. 2"


class ag_rechtsschrift_zurueckgewiesen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Rechtsschrift wird zur Nachbesserung zurueckgewiesen (AG 290.100 § 4 Abs. 1)"
    reference = "AG 290.100 § 4 Abs. 1"

    def formula(person, period, parameters):
        return person('ag_rechtsschrift_unzulaessige_vertretung', period)


class ag_vertretung_zurueckgewiesen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unzulaessige Vertretung wird an Verhandlung zurueckgewiesen (AG 290.100 § 4 Abs. 2)"
    reference = "AG 290.100 § 4 Abs. 2"

    def formula(person, period, parameters):
        return person('ag_verhandlung_unzulaessige_vertretung', period)


class ag_anzeige_strafbehoerden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzeige bei Strafbehoerden wegen unerlaubter Ausuebung des Anwaltsberufs (AG 290.100 § 4 Abs. 3)"
    reference = "AG 290.100 § 4 Abs. 3; AG 290.100 § 18"

    def formula(person, period, parameters):
        rechtsschrift = person('ag_rechtsschrift_unzulaessige_vertretung', period)
        verhandlung = person('ag_verhandlung_unzulaessige_vertretung', period)
        return rechtsschrift + verhandlung > 0
