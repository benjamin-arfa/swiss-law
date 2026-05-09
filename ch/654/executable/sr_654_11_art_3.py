"""SR 654.11 Art. 3 - Schwellenwert fuer die Pflicht zur Erstellung

Generated from: ch/654/de/654.11.md

The threshold above which the obligation to prepare a CbC report
exists is CHF 900 million consolidated annual turnover.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class schwellenwert_laenderbezogener_bericht(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schwellenwert fuer die Pflicht zur Erstellung eines laenderbezogenen Berichts (CHF)"
    reference = "SR 654.11 Art. 3"
    default_value = 900_000_000.0


class konsolidierter_jahresumsatz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Konsolidierter Jahresumsatz des multinationalen Konzerns (CHF)"
    reference = "SR 654.11 Art. 3"


class pflicht_laenderbezogener_bericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der multinationale Konzern ist zur Erstellung eines laenderbezogenen Berichts verpflichtet"
    reference = "SR 654.11 Art. 3"

    def formula(self, period, parameters):
        umsatz = self('konsolidierter_jahresumsatz', period)
        schwellenwert = self('schwellenwert_laenderbezogener_bericht', period)
        return umsatz > schwellenwert
