"""SR 832.112.31 Art. 3c

Generated from: ch/832/de/832.112.31.md

Art. 3c: Einschraenkung der Kostenuebernahme bei bestimmten elektiven
Eingriffen.
- Abs. 1: Wird ein elektiver Eingriff stationaer durchgefuehrt, uebernimmt
  die Versicherung die Kosten nur, wenn eine ambulante Durchfuehrung wegen
  besonderer Umstaende nicht zweckmaessig oder nicht wirtschaftlich ist.
- Abs. 2: Ambulante Durchfuehrung ist nicht zweckmaessig/wirtschaftlich,
  wenn eines der Kriterien nach Anhang 1a Ziffer II erfuellt ist.
- Abs. 3: Bei anderen Umstaenden ist vorgaengig die besondere Gutsprache
  des Versicherers einzuholen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class klv_elektiver_eingriff(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Eingriff ist ein elektiver Eingriff nach Anhang 1a Ziffer I KLV"
    reference = "SR 832.112.31 Art. 3c Abs. 1"


class klv_eingriff_stationaer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Eingriff wird stationaer durchgefuehrt"
    reference = "SR 832.112.31 Art. 3c Abs. 1"


class klv_ambulant_nicht_zweckmaessig_anhang1a(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ambulante Durchfuehrung nicht zweckmaessig gemaess Anhang 1a Ziffer II"
    reference = "SR 832.112.31 Art. 3c Abs. 2"


class klv_gutsprache_versicherer_erhalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Besondere Gutsprache des Versicherers fuer stationaere Durchfuehrung erhalten"
    reference = "SR 832.112.31 Art. 3c Abs. 3"


class klv_stationaere_kostenuebernahme_elektiv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kostenuebernahme fuer stationaeren elektiven Eingriff durch OKP"
    reference = "SR 832.112.31 Art. 3c"

    def formula(person, period, parameters):
        elektiv = person('klv_elektiver_eingriff', period)
        stationaer = person('klv_eingriff_stationaer', period)
        anhang_kriterium = person('klv_ambulant_nicht_zweckmaessig_anhang1a', period)
        gutsprache = person('klv_gutsprache_versicherer_erhalten', period)

        # Nicht-elektive oder ambulante Eingriffe: normale Kostenuebernahme
        nicht_betroffen = not_(elektiv) + not_(stationaer)

        # Stationaerer elektiver Eingriff: nur wenn Anhang-1a-Kriterium oder Gutsprache
        stationaer_zulaessig = elektiv * stationaer * (anhang_kriterium + gutsprache)

        return nicht_betroffen + stationaer_zulaessig
