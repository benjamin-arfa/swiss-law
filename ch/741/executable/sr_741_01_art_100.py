"""SR 741.01 Art. 100 - Strafbarkeit

Generated from: ch/de/741/741.01.md

Criminal liability rules:
1. Negligent acts are also punishable unless law states otherwise;
   particularly light cases: no penalty
2. Employer/supervisor who causes or fails to prevent violation:
   same penalty as driver
3. Learner driver instructor responsible for violations due to
   breach of supervision duties
4. Emergency vehicle drivers exempt if exercising due care +
   warning signals (police, fire, ambulance, customs)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fahrlaessige_handlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine fahrlaessige (nicht vorsaetzliche) Handlung vorliegt"
    reference = "SR 741.01 Art. 100 Ziff. 1"


class besonders_leichter_fall_art100(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein besonders leichter Fall nach Art. 100 Ziff. 1 vorliegt"
    reference = "SR 741.01 Art. 100 Ziff. 1"


class strafbarkeit_fahrlaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Strafbarkeit bei fahrlaessiger Handlung gegeben ist"
    reference = "SR 741.01 Art. 100 Ziff. 1"

    def formula(person, period, parameters):
        fahrlaessig = person('fahrlaessige_handlung', period)
        besonders_leicht = person('besonders_leichter_fall_art100', period)
        return fahrlaessig * (1 - besonders_leicht)


class ist_arbeitgeber_oder_vorgesetzter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person als Arbeitgeber oder Vorgesetzter handelt"
    reference = "SR 741.01 Art. 100 Ziff. 2"


class arbeitgeber_hat_widerhandlung_veranlasst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Arbeitgeber die Widerhandlung veranlasst oder nicht verhindert hat"
    reference = "SR 741.01 Art. 100 Ziff. 2"


class arbeitgeber_strafbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Arbeitgeber/Vorgesetzte strafbar ist"
    reference = "SR 741.01 Art. 100 Ziff. 2"

    def formula(person, period, parameters):
        ist_ag = person('ist_arbeitgeber_oder_vorgesetzter', period)
        veranlasst = person('arbeitgeber_hat_widerhandlung_veranlasst', period)
        return ist_ag * veranlasst


class dringliche_dienstfahrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine dringliche Dienstfahrt (Polizei, Feuerwehr, Sanitaet, Zoll) vorliegt"
    reference = "SR 741.01 Art. 100 Ziff. 4"


class erforderliche_sorgfalt_angewendet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob alle erforderliche Sorgfalt angewendet wurde"
    reference = "SR 741.01 Art. 100 Ziff. 4"


class warnsignale_abgegeben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die erforderlichen Warnsignale abgegeben wurden"
    reference = "SR 741.01 Art. 100 Ziff. 4"


class dienstfahrt_strafbefreiung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Strafbefreiung fuer dringliche Dienstfahrt greift"
    reference = "SR 741.01 Art. 100 Ziff. 4"

    def formula(person, period, parameters):
        dienstfahrt = person('dringliche_dienstfahrt', period)
        sorgfalt = person('erforderliche_sorgfalt_angewendet', period)
        warnung = person('warnsignale_abgegeben', period)
        return dienstfahrt * sorgfalt * warnung
