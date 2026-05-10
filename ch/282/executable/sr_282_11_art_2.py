"""SR 282.11 Art. 2 - Betreibungsarten und Ausschluesse

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class betreibungsart_pfaendung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schuldbetreibung ist auf Pfaendung gerichtet"
    reference = "SR 282.11 Art. 2 Abs. 1"


class betreibungsart_pfandverwertung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schuldbetreibung ist auf Pfandverwertung gerichtet"
    reference = "SR 282.11 Art. 2 Abs. 1"


class betreibungsart_konkurs(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schuldbetreibung ist auf Konkurs gerichtet"
    reference = "SR 282.11 Art. 2 Abs. 2"


class glaeubiger_hat_ausfallschein(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Glaeubiger hat einen Ausfallschein erhalten"
    reference = "SR 282.11 Art. 2 Abs. 3"


class ungedeckter_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ungedeckt bleibender Betrag der Forderung"
    reference = "SR 282.11 Art. 2 Abs. 3"


# Computed variables

class betreibungsart_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die gewaehlte Betreibungsart ist zulaessig"
    reference = "SR 282.11 Art. 2 Abs. 1-2"

    def formula(self, period, parameters):
        pfaendung = self('betreibungsart_pfaendung', period)
        pfandverwertung = self('betreibungsart_pfandverwertung', period)
        konkurs = self('betreibungsart_konkurs', period)
        # Nur Pfaendung oder Pfandverwertung zulaessig, Konkurs ausgeschlossen
        return (pfaendung + pfandverwertung > 0) * (1 - konkurs)


class ausfallschein_gilt_als_schuldanerkennung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Ausfallschein gilt als Schuldanerkennung im Sinne von Art. 82 SchKG"
    reference = "SR 282.11 Art. 2 Abs. 3"

    def formula(self, period, parameters):
        return self('glaeubiger_hat_ausfallschein', period)
