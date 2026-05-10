"""SR 641.31 Art. 5

Generated from: ch/641/de/641.31.md

Tabaksteuer - Steuerbefreiung:
Von der Steuer befreit sind:
a. zollfreie Waren nach Art. 8 ZG
b. (aufgehoben)
c. Tabakfabrikate, die nicht fuer den Verbrauch bestimmt sind
d. Tabakfabrikate zur Linderung von Asthmabeschwerden, wenn als Heilmittel
   registriert
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tstg_ist_zollfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Tabakprodukt zollfrei ist nach Art. 8 ZG"
    reference = "SR 641.31 Art. 5 Bst. a"


class tstg_nicht_fuer_verbrauch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Tabakfabrikat nicht fuer den Verbrauch bestimmt ist"
    reference = "SR 641.31 Art. 5 Bst. c"


class tstg_ist_registriertes_heilmittel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Tabakfabrikat als Heilmittel (Asthma) registriert ist"
    reference = "SR 641.31 Art. 5 Bst. d"


class tstg_steuerbefreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Tabakprodukt von der Tabaksteuer befreit ist"
    reference = "SR 641.31 Art. 5"

    def formula(person, period, parameters):
        zollfrei = person('tstg_ist_zollfrei', period)
        nicht_verbrauch = person('tstg_nicht_fuer_verbrauch', period)
        heilmittel = person('tstg_ist_registriertes_heilmittel', period)
        return (zollfrei + nicht_verbrauch + heilmittel) > 0
