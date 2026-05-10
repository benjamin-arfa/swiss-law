"""SR 282.11 Art. 22 - Voraussetzungen fuer Massnahmen

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class massnahme_zur_beseitigung_notlage_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Massnahme ist zur Beseitigung der Notlage erforderlich und geeignet"
    reference = "SR 282.11 Art. 22 Abs. 1"


class alles_billigerweise_erwartbare_getan(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zur Abwendung der Notlage ist alles getan worden, was billigerweise erwartet werden darf"
    reference = "SR 282.11 Art. 22 Abs. 1"


class obligationaere_gleichmaessig_betroffen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Obligationaere in gleicher Rechtslage werden gleichmaessig betroffen"
    reference = "SR 282.11 Art. 22 Abs. 2"


# Computed variables

class massnahme_nach_art13_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Massnahme nach Art. 13 ist materiell zulaessig"
    reference = "SR 282.11 Art. 22"

    def formula(self, period, parameters):
        erforderlich = self('massnahme_zur_beseitigung_notlage_erforderlich', period)
        alles_getan = self('alles_billigerweise_erwartbare_getan', period)
        gleichmaessig = self('obligationaere_gleichmaessig_betroffen', period)
        return erforderlich * alles_getan * gleichmaessig
