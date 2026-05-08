"""SR 746.1 Art. 4

Generated from: ch/746/de/746.1.md

Anforderungen an auslaendische Unternehmungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_auslaendische_rohrleitungsunternehmung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmung ist eine auslaendische Rohrleitungsunternehmung"
    reference = "SR 746.1 Art. 4"


class hat_schweizer_geschaeftsfuehrung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Auslaendische Unternehmung hat eine in der Schweiz ansaessige Geschaeftsfuehrung und Betriebsleitung"
    reference = "SR 746.1 Art. 4"


class auslaendische_unternehmung_erfuellt_art4(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Auslaendische Unternehmung erfuellt die Anforderungen nach Art. 4 RLG"
    reference = "SR 746.1 Art. 4"

    def formula(person, period, parameters):
        # Art. 4: Auslaendische Unternehmung muss in der Schweiz ansaessige
        # Geschaeftsfuehrung und Betriebsleitung sowie eine Betriebsorganisation
        # haben, die Einhaltung des schweizerischen Rechts gewaehrleistet.
        ist_auslaendisch = person('ist_auslaendische_rohrleitungsunternehmung', period)
        hat_ch_leitung = person('hat_schweizer_geschaeftsfuehrung', period)
        # If not foreign, requirement is automatically met
        return where(ist_auslaendisch, hat_ch_leitung, True)
