"""SR 364.3 Art. 11

Generated from: ch/364/de/364.3.md

Einsatz von Destabilisierungsgeraeten und Feuerwaffen: Bedingungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class person_hat_schwere_straftat_begangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat eine schwere Straftat begangen oder steht ernsthaft im Verdacht"
    reference = "SR 364.3 Art. 11 Abs. 1"


class schwere_straftat_zu_verhindern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einsatz dient der Verhinderung einer schweren Straftat"
    reference = "SR 364.3 Art. 11 Abs. 2"


class ist_rueckfuehrung_luftweg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einsatz erfolgt bei einer Rueckfuehrung auf dem Luftweg"
    reference = "SR 364.3 Art. 11 Abs. 4"


class destabilisierungsgeraet_einsatz_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einsatz eines Destabilisierungsgeraets gegen die Person ist zulaessig"
    reference = "SR 364.3 Art. 11"

    def formula(person, period, parameters):
        schwere_tat = person('person_hat_schwere_straftat_begangen', period)
        verhindern = person('schwere_straftat_zu_verhindern', period)
        rueckfuehrung = person('ist_rueckfuehrung_luftweg', period)
        return (schwere_tat + verhindern) * not_(rueckfuehrung)


class feuerwaffe_einsatz_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einsatz einer Feuerwaffe gegen die Person ist zulaessig"
    reference = "SR 364.3 Art. 11"

    def formula(person, period, parameters):
        schwere_tat = person('person_hat_schwere_straftat_begangen', period)
        rueckfuehrung = person('ist_rueckfuehrung_luftweg', period)
        # Feuerwaffen nur bei begangener/verdaechtigter schwerer Straftat, nicht bei Rueckfuehrung
        return schwere_tat * not_(rueckfuehrung)
